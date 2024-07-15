# TO DO
# improve lower brightness contrast
# refactor & modularize
# implement my own resize function

from PIL import Image
from text_output import ascii_to_image as asciitoi


# To convert RGB to 8 bit gamma:
# gamma = 0.2126*red + 0.7152*green + 0.0722*blue
def rgb_to_grayscale(pixels):
    def pixel_rgb_to_gray(t):
        return 0.2126 * t[0] + 0.7152 * t[1] + 0.0722 * t[2]

    return [[pixel_rgb_to_gray(t) for t in col] for col in pixels]


def grayscale_to_3bit(pixels):
    # This vvvvvvv version returns a pixel grid with the 8 quantized values
    # return [[(32 * (i // 32)) for i in col] for col in pixels]

    # This one just returns the index 0-7 from darkest to brightest
    return [[int(i // 32) for i in col] for col in pixels]


def quantized_to_ascii(pixels):
    chars = [" ", ",", ";", "l", "O", "#", "W", "M"]
    return [[chars[i] for i in col] for col in pixels]


def side_by_side(im_1, im_2, gap=20):
    sbs = Image.new("RGB", (im_1.size[0], im_1.size[1] + im_2.size[1] + gap))
    sbs.paste(im_1)
    sbs.paste(im_2, (0, im_1.size[1] + gap))
    return sbs


def main():
    im = Image.open("assets/in.jpg")
    im = im.resize((im.size[0] // 8, im.size[1] // 8))
    size = im.size

    # each sublist is a column
    rgb_pixels = [[im.getpixel((i, j)) for i in range(size[0])] for j in range(size[1])]

    gs_pixels = rgb_to_grayscale(rgb_pixels)

    q_pixels = grayscale_to_3bit(gs_pixels)

    a_pixels = quantized_to_ascii(q_pixels)

    side_by_side(Image.open("assets/in.jpg"), asciitoi(a_pixels)).save("assets/out.jpg")


if __name__ == "__main__":
    main()
