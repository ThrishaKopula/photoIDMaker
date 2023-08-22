from PIL import Image, ImageFilter
from rembg import remove
import os

path = './images'
pathOut = './editedImages'

fill_color = (255, 246, 243) #background color

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
    removedImg = remove(edit)

    removedImg = removedImg.convert("RGBA")
    if removedImg.mode in ('RGBA', 'LA'):
            background = Image.new(removedImg.mode[:-1], removedImg.size, fill_color)
            background.paste(removedImg, removedImg.split()[-1])
            removedImg = background
    edit = removedImg.convert("RGB")

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.png')
