from PIL import Image
import numpy as np


def rgb_to_grayscale(pixels):
    gs_pixels = []
    for col in pixels:
        new_col = []
        for t in col:
            # just averaging RGB and converting it to 8-bit
            gs_p = (t[0] + t[1] + t[2]) % 255
            new_col.append(gs_p)
        gs_pixels.append(new_col)
    return gs_pixels


def side_by_side(im_1, im_2, gap=20):
    sbs = Image.new("RGB", (im_1.size[0] + im_2.size[0] + gap, im_1.size[0]))
    sbs.paste(im_1)
    sbs.paste(im_2, (im_1.size[0] + gap, 0))
    return sbs


def main():
    im = Image.open("assets/funny_dog.jpg")
    size = im.size

    # each sublist is a column
    rgb_pixels = [[im.getpixel((i, j)) for i in range(size[0])] for j in range(size[1])]

    gs_pixels = rgb_to_grayscale(rgb_pixels)

    gs = Image.fromarray(np.array(gs_pixels, dtype=np.uint8), "L")

    side_by_side(im, gs).show()


if __name__ == "__main__":
    main()
