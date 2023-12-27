import os
import numpy as np
import cv2


def mask_to_yolo(mask_dir, save_dir, num_label, num_points):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    imgs = os.listdir(mask_dir)
    for img in imgs:
        contour_labels_all = list()  # 类别列表
        contour_coords_all = list()  # 坐标列表
        # 读取图片
        img_path = os.path.join(mask_dir, img)
        img_current = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        w, h = img_current.shape
        # 获取不同类别的轮廓
        for label_id in range(1, num_label+1, 1):
            img_temp = img_current
            img_temp = np.uint8(img_temp)
            img_temp[img_temp != label_id] = 0
            contours, _ = cv2.findContours(img_temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) != 0:  # 获取到该类别轮廓
                contour_coords_temp = list()  # 坐标列表
                for current_contours in contours:
                    current_contours = np.array(current_contours).squeeze(1)
                    if len(current_contours) >= 14:  # 如果当前轮廓点数大于14则步长采样
                        step = len(current_contours) // num_points
                        sample_ind = np.arange(0, len(current_contours), step)  # [:14]
                        resampled_contour = current_contours[sample_ind]
                    else:  # 如果小于14则需要同一点多次采样来插值
                        contour_len = current_contours.shape[0]
                        indices = np.linspace(0, contour_len - 1, num_points, dtype=int)
                        resampled_contour = current_contours[indices, :]
                    for idx in range(num_points):
                        # norm
                        contour_coords_temp.append(resampled_contour[idx][0] / h)
                        contour_coords_temp.append(resampled_contour[idx][1] / w)
                    contour_labels_all.append(label_id-1)
                    contour_coords_all.append(contour_coords_temp)
        out_file = open(save_dir + '/' + img.split('.')[0] + '.txt', 'w')
        for ln, bb in zip(contour_labels_all, contour_coords_all):
            out_file.write(str(ln) + " " + " ".join([str(round(a, 6)) for a in bb]) + '\n')
        print("convert ", img_path)


if __name__ == '__main__':
    # png mask dir ,target dir, number of class, number of points
    # mask_to_yolo("./train_mask", "./train_txt", 5, 14)
    mask_to_yolo("./val_mask", "./val_txt", 5, 14)
