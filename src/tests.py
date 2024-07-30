import unittest
import edge_detection as ed


class TestConvolutionMatrix(unittest.TestCase):
    def test_2d_conv_identity_0(self):
        w = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

        im = [
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
        ]
        self.assertEqual(ed.convolution_2d(im, w), im)

    def test_2d_conv_identity_1(self):
        w = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]

        im = [
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
        ]

        res = [
            [0, 10, 10, 100],
            [0, 10, 10, 100],
            [0, 10, 10, 100],
            [0, 10, 10, 100],
        ]
        self.assertEqual(ed.convolution_2d(im, w), res)

    def test_2d_conv_identity_2(self):
        w = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
        ]

        im = [
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
            [10, 10, 100, 100],
        ]

        res = [
            [10, 100, 100, 0],
            [10, 100, 100, 0],
            [10, 100, 100, 0],
            [10, 100, 100, 0],
        ]
        self.assertEqual(ed.convolution_2d(im, w), res)

    #
    # def test_2d_conv(self):
    # gx = [
    # [-1, 0, 1],
    # [-2, 0, 2],
    # [-1, 0, 1],
    # ]
    #
    # im = [
    # [10, 10, 100, 100],
    # [10, 10, 100, 100],
    # [10, 10, 100, 100],
    # [10, 10, 100, 100],
    # ]
    #
    # res = [
    # [3, 30, 30, -33],
    # [4, 40, 40, -44],
    # [4, 40, 40, -44],
    # [3, 30, 30, -33],
    # ]
    # self.assertEqual(ed.convolution_2d(im, gx), res)
    #


if __name__ == "__main__":
    unittest.main()
