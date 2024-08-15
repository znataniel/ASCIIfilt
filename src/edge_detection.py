# from PIL import Image
import numpy as np
import math as m


# Sobel operator
# Receives grayscale pixel image data
# Returns edge detected pixel data
def sobel(im: list[list], get_angle=False) -> list[list]:
    di, dj = len(im), len(im[0])

    kx = [
        [-3, 0, 3],
        [-10, 0, 10],
        [-3, 0, 3],
    ]

    ky = [
        [-3, -10, -3],
        [0, 0, 0],
        [3, 10, 3],
    ]

    gx = convolution_2d(im, kx)
    gy = convolution_2d(im, ky)
    # get_angle = False is to visualize the edges
    sobel = [
        [threshold(rounded_module(gx[i][j] / 9, gy[i][j] / 9) % 256) for j in range(dj)]
        for i in range(di)
    ]

    angles = [
        [angle(gx[i][j], gy[i][j]) if sobel[i][j] else 0 for j in range(dj)]
        for i in range(di)
    ]
    return sobel if not get_angle else angles


def angle(a, b):
    return m.atan(b / a) if a else m.pi / 2


def rounded_module(a, b):
    return m.ceil(m.sqrt(a**2 + b**2))


def threshold(val: float | int, t=64) -> int:
    return 255 if val >= t else 0


def box_blur(im: list[list], size=5) -> list[list]:
    k = [[1 / size**2] * size for _ in range(size)]
    blur = convolution_2d(im, k)
    return blur


def convolution_2d(im: list[list], k: list[list]) -> list[list]:
    # Kernel is assumed to be a square, odd side matrix
    k_dim = len(k) // 2
    res = [[0] * len(im[0]) for _ in range(len(im))]
    for i in range(len(im)):
        for j in range(len(im[0])):
            # vvvvvv this works because the kernel
            # needs to always have a center
            pixel = 0
            for a in range(-k_dim, k_dim + 1):
                for b in range(-k_dim, k_dim + 1):
                    if i + a in range(0, len(im)) and j + b in range(0, len(im[0])):
                        pixel += im[i + a][j + b] * k[a + k_dim][b + k_dim]
            res[i][j] = pixel
    return res
