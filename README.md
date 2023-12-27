# png-mask-to-yolo-txt
Convert png mask segmentation labels to yolo txt format
将png掩码mask转换为yolo的txt格式
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
