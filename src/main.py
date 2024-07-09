from PIL import Image
import numpy as np


# To convert RGB to 8 bit gamma:
# gamma = 0.2126*red + 0.7152*green + 0.0722*blue
def rgb_to_grayscale(pixels):
    def pixel_rgb_to_gray(t):
        return 0.2126 * t[0] + 0.7152 * t[1] + 0.0722 * t[2]

    return [[pixel_rgb_to_gray(t) for t in col] for col in pixels]


def side_by_side(im_1, im_2, gap=20):
    sbs = Image.new("RGB", (im_1.size[1], im_1.size[1] + im_2.size[1] + gap))
    sbs.paste(im_1)
    sbs.paste(im_2, (0, im_1.size[1] + gap))
    return sbs


def main():
    im = Image.open("assets/in.jpg")
    size = im.size

    # each sublist is a column
    rgb_pixels = [[im.getpixel((i, j)) for i in range(size[0])] for j in range(size[1])]

    gs_pixels = rgb_to_grayscale(rgb_pixels)

    gs = Image.fromarray(np.array(gs_pixels, dtype=np.uint8))

    side_by_side(im, gs).save("assets/out.jpg")


if __name__ == "__main__":
    main()
