import numpy as np
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw


def ascii_to_image(ascii):
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
