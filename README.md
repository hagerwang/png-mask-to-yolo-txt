# png-mask-to-yolo-txt
Convert png mask segmentation labels to yolo txt format
将png掩码mask转换为yolo的txt格式
|——mask_png_dir  待转换的mask png
   |——mask1.png
   |—— ...
   |——mask1.png
|——target_txt_dir  转换后的txt
   |——mask1.txt
   |—— ...
   |——mask1.txt
png 内容： 0 背景  1~n 为对应的类别的实例掩码
