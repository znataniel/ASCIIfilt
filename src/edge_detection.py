from PIL import Image
import numpy as np


# Sobel operator
# Receives grayscale pixel image data
# Returns edge detected pixel data
def sobel(im: list[list]) -> list[list]:
    gx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    gy = [
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1],
    ]
    pass

    # im[row][column/pixel] === a_ij (like algebra matrix)
    # im = [
    # [50, 100, 100, 100, 100],
    # [50, 50, 100, 100, 100],
    # [50, 50, 50, 100, 100],
    # [50, 50, 50, 100, 100],
    # [50, 50, 50, 100, 100],
    # ]


def convolution_2d(im: list[list], k: list[list]):
    # Kernel is assumed to be a square, odd side matrix
    k_dim = len(k) // 2
    res = [[]]
    for i in range(len(im)):
        for j in range(len(im[0])):
            # vvvvvv this works because the kernel
            # needs to always have a center
            pixel = 0
            for a in range(-k_dim, k_dim + 1):
                for b in range(-k_dim, k_dim + 1):
                    pixel += im[i + a][j + b] * k[a + k_dim][b + k_dim]
            res[i][j] = pixel // len(k) ** 2
    return res
