import math as m
import numpy as np
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw


# To convert RGB to 8 bit gamma:
# gamma = 0.2126*red + 0.7152*green + 0.0722*blue
def rgb_to_grayscale(pixels: list[list]) -> list[list]:
    def pixel_rgb_to_gray(t):
        return 0.2126 * t[0] + 0.7152 * t[1] + 0.0722 * t[2]

    return (
        [[pixel_rgb_to_gray(t) for t in col] for col in pixels]
        if type(pixels[0][0]) == tuple
        else pixels
    )


def grayscale_to_3bit(pixels: list[list[int]]) -> list[list[int]]:
    # This vvvvvvv version returns a pixel grid with the 8 quantized values
    # Useful for visualizing the quantization
    # return [[(32 * (i // 32)) for i in col] for col in pixels]

    # This one just returns the index 0-7 from darkest to brightest
    return [[int(i // 32) for i in col] for col in pixels]


# Brightest charascter -> " "
# Darkest Character -> "M"
def quantized_to_ascii(pixels: list[list[int]]) -> list[list[str]]:
    chars = ["W", "@", "?", "o", "c", ";", ",", " "]
    return [[chars[i] for i in col] for col in pixels]


def quantize_angle(ang: float) -> int:
    if m.pi / 2 <= ang < (3 * m.pi / 4) or (-3 * m.pi / 4) <= ang <= (-m.pi / 2):
        return 0
    if (3 * m.pi / 4) <= ang < (m.pi / 4):
        return 1
    if (m.pi / 4) <= ang < (-m.pi / 4):
        return 2
    if (-m.pi / 4) <= ang < (-3 * m.pi / 4):
        return 3
    return 0


def ascii_angles(pixels: list[list[int]]) -> list[list[str]]:
    chars = ["|", "/", "-", "\\"]
    return [[chars[quantize_angle(ang)] for ang in col] for col in pixels]


def ascii_to_image(ascii: list[list[str]]) -> Image.Image:
    font_size = 8  # pixels
    h, w = font_size * len(ascii), font_size * len(ascii[0])

    bg_image = np.full((h, w), 255, dtype="uint8")

    image0 = Image.fromarray(bg_image)
    draw = ImageDraw.Draw(image0)

    for i in range(0, len(ascii[0])):
        for j in range(0, len(ascii)):
            draw.text(
                (i * font_size, j * font_size),
                ascii[j][i],
                font_size=font_size,
                spacing=0,
                fill="rgb(0, 0, 0)",
            )
    return image0
