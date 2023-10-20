import unittest
from isTriangle import Triangle


class test_mutationAdequate(unittest.TestCase):
    def test4(self):
        triangles = dict(eq_1=((2, 2, 2), Triangle.Type.EQUILATERAL),
                         sc_1=((2, 3, 4), Triangle.Type.SCALENE),
                         is_1=((3, 3, 5), Triangle.Type.ISOSCELES),
                         is_2=((3, 5, 3), Triangle.Type.ISOSCELES),
                         is_3=((5, 3, 3), Triangle.Type.ISOSCELES),
                         in_2=((1, 2, 5), Triangle.Type.INVALID),
                         in_3=((3, 2, 5), Triangle.Type.INVALID),
                         in_4=((3, 5, 2), Triangle.Type.INVALID),
                         in_5=((5, 3, 2), Triangle.Type.INVALID),
                         in_6=((2, 2, 5), Triangle.Type.INVALID),
                         in_7=((2, 2, 4), Triangle.Type.INVALID),
                         in_8=((2, 4, 2), Triangle.Type.INVALID),
                         in_9=((4, 2, 2), Triangle.Type.INVALID),
                         in_10=((-1, 2, 5), Triangle.Type.INVALID),
                         in_11=((2, -1, 5), Triangle.Type.INVALID),
                         in_12=((1, 2, -5), Triangle.Type.INVALID),
                         )

        for value in triangles.values():
            triangle, expected = value
            actual = Triangle.classify(*triangle)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
