# TO DO
# EDGE DETECTION!!
# implement my own resize function
#   resize images such that the width fits in a regular column of text (~80 characters)
# implement some unit tests after improving some of the conversion functions

from PIL import Image
import conversion as conv
from sys import argv
from edge_detection import sobel
import numpy as np


def side_by_side(
    im_1: Image.Image, im_2: Image.Image, gap=20, vertical_or=True
) -> Image.Image:
    if vertical_or:
        sbs = Image.new("RGB", (im_1.size[0], im_1.size[1] + im_2.size[1] + gap))
    else:
        sbs = Image.new("RGB", (im_1.size[0] + gap + im_2.size[0], im_1.size[1]))

    sbs.paste(im_1)
    sbs.paste(im_2, (0, im_1.size[1] + gap) if vertical_or else (im_1.size[0] + gap, 0))
    return sbs


# each sublist is a column
def get_rgb_pixels(im: Image.Image) -> list[list]:
    return [[im.getpixel((i, j)) for i in range(im.size[0])] for j in range(im.size[1])]


def main():
    if len(argv) != 2:
        print("Usage:\t asciifilt path/to/image.ext")
        exit(1)

    im = Image.open(argv[1])
    # im = im.resize((im.size[0] // 8, im.size[1] // 8))
    im = im.resize((im.size[0] // 2, im.size[1] // 2))

    #    ascii_im = conv.ascii_to_image(
    #        conv.quantized_to_ascii(
    #            conv.grayscale_to_3bit(conv.rgb_to_grayscale(get_rgb_pixels(im)))
    #        )
    #    )

    edges = Image.fromarray(
        np.array(sobel(conv.rgb_to_grayscale(get_rgb_pixels(im))), dtype="uint8")
    )

    side_by_side(im, edges).save("assets/out.jpg")
    # side_by_side(Image.open(argv[1]), ascii_im).save("assets/out.jpg")


if __name__ == "__main__":
    main()
