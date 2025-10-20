import PIL
from PIL import Image
from PIL import ImageOps
import math

value_conv = {
    " " : range(0, 21),
    "." : range(21, 42),
    ":" : range(42, 63),
    "-" : range(63, 84),
    "~" : range(84, 105),
    "=" : range(105, 126),
    "+" : range(126, 147),
    "*" : range(147, 169),
    "^" : range(169, 190),
    "#" : range(190, 211),
    "%" : range(211, 232),
    "@" : range(232, 256)
}

def convert_image():
    try:
        print("Welcome to image to ASCII converter. Type exit to quit")
        name = input("Enter full file path: ")
        if name == "exit":
            return 0

        width = input("Enter width (higher width means more resolution): ")
        if width == "exit":
            return 0



        with Image.open(name) as img:
            img = PIL.ImageOps.grayscale(img)

            print(img.size[1])

            px = img.load()

            a = ""
            for i in range(0, img.size[1], math.floor(img.size[1]//int(width) * 3)):
                for j in range(0, int(width)):
                    v = px[j*img.size[0]//int(width), i]
                    for key, value in value_conv.items():
                        if v in value:
                            a += key
                a += "\n"

        print(a)
        return 0

    except Exception as e:
        print(e)

while convert_image() != 0:
    convert_image()
