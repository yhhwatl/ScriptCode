# -*- coding: utf-8 -*-
from PIL import Image

def find_blank_space_size(image_path):
    # 打开图像
    img = Image.open(image_path)

    # 转换为带有Alpha通道的图像（RGBA）
    img = img.convert("RGBA")

    # 获取图像的数据
    data = img.getdata()

    # 初始化空白区域的计数器
    blank_pixel_count = 0

    # 遍历图像数据
    for pixel in data:
        # 如果Alpha通道为0，表示透明像素（空白区域）
        # print(pixel[0],pixel[1],pixel[2],pixel[3])
        if pixel[3] <= 10:
            blank_pixel_count += 1

    # 获取图像的宽度和高度
    width, height = img.size

    # 计算空白区域的大小（透明像素的数量）
    blank_space_size = 100 * blank_pixel_count / (width * height)
    
    return blank_space_size

# 图像路径
image_path = "/Users/mw/Documents/baiyang/lzfishclient/Assets/Project/UI/UIPlazaRoomEnterNew.png"

# 调用函数获取空白区域的大小
blank_space_size = find_blank_space_size(image_path)

# 打印结果
print("blank area ratio ",blank_space_size)