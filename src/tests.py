import unittest
import conversion as cv
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


class TestAngles(unittest.TestCase):
    def test_quantization_0(self):
        input = [
            [ed.angle(32, 19), ed.angle(2, 2), ed.angle(10, 3)],
            [ed.angle(2, 19), ed.angle(2, -2), ed.angle(-9, 3)],
            [ed.angle(-13, -7), ed.angle(-1, 2), ed.angle(10, 3)],
        ]
        quantized = [[cv.quantize_angle(a) for a in row] for row in input]
        for row in quantized:
            for i in row:
                self.assertTrue(i in range(4))

    def test_quantization_1(self):
        input = [
            [ed.angle(32, 19), ed.angle(2, 2), ed.angle(10, 3)],
            [ed.angle(2, 19), ed.angle(2, -2), ed.angle(-9, 3)],
            [ed.angle(-13, -7), ed.angle(-1, 2), ed.angle(10, 3)],
        ]
        quantized = [[cv.quantize_angle(a) for a in row] for row in input]
        rows = [any(r) for r in quantized]
        self.assertTrue(all(rows))

    def test_quantization_2(self):
        input = [
            ed.angle(0, 2),
            ed.angle(10, 10),
            ed.angle(1, 0),
            ed.angle(1, -1),
            ed.angle(1, -10),
        ]
        res = [0, 1, 2, 3, 0]
        self.assertEqual([cv.quantize_angle(a) for a in input], res)


if __name__ == "__main__":
    unittest.main()
