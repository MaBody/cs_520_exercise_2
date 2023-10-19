import unittest
from isTriangle import Triangle
from isTriangle import Type


class test_decisionCoverage(unittest.TestCase):
    def decision_tests(self):
        triangles = dict(eq_1=((2, 2, 2), Triangle.Type.EQUILATERAL),
                         sc_1=((2, 3, 4), Triangle.Type.SCALENE),
                         is_1=((3, 3, 5), Triangle.Type.ISOSCELES),
                         is_2=((3, 5, 3), Triangle.Type.ISOSCELES),
                         is_3=((5, 3, 3), Triangle.Type.ISOSCELES),
                         in_1=((1, 2, 5), Triangle.Type.INVALID),
                         )
        for value in triangles.items():
            triangle, expected = value
            actual = Triangle.classify(triangle)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
