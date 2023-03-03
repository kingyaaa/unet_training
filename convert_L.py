from PIL import Image
import os
# Open the image file

folder_path = 'VOCdevkit/VOC2007/SegmentationClass_Origin'
save_path = 'VOCdevkit/VOC2007/SegmentationOrigin_L'

for img_file in os.listdir(folder_path):
    if img_file.endswith(".png"):
        img = Image.open(os.path.join(folder_path, img_file))

        img = img.convert('L')

        pixels = img.load()
        width, height = img.size
        for x in range(width):
            for y in range(height):
                if pixels[x, y] == 1:
                    pixels[x, y] = 255
        img.save(os.path.join(save_path, img_file))

