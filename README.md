# png-mask-to-yolo-txt
Convert png mask segmentation labels to yolo txt format
将png掩码mask转换为yolo的txt格式

mask_to_yolo 输入为：mask png目录地址、txt保存地址、类别数、生成轮廓点数、验证生成轮廓点

```
data
|_ mask_png_dir  待转换的mask png
|  |_ 1.png
|  |_ 2.png
|  |_ ...
|  |_ 1000.png
|_ target_txt_dir  转换后的txt
|  |_ 1.txt
|  |_ ...
.......
```
png 内容： 0 背景  1~n 为对应的类别的实例掩码

只适用于png格式为h w, 若为h w c=3则需要将img_temp[img_temp != label_id] = 0改为对应颜色的判断

代码逻辑比较冗余，凑活用吧。本人用的yolov8测的可以用。
