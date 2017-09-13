import unittest
from Squarelotron import *

squarelotron = [[1, 6, 11, 16, 21],
                [2, 7, 8, 9, 22],
                [3, 12, 13, 14, 23],
                [4, 17, 18, 19, 24],
                [5, 10, 15, 20, 25]]

class TestSquarelotrons(unittest.TestCase):

    def test_make_squarelotron(self):
        self.assertEqual(25, make_squarelotron(range(1, 26))[4][4])
        self.assertEqual(13, make_squarelotron(range(1, 26))[2][2])
        self.assertNotEqual(1, make_squarelotron(range(1, 26))[0][1])


    def test_make_list(self):
        self.assertEqual(25, make_list(squarelotron)[0])
        self.assertEqual(1, make_list(squarelotron)[24])
        self.assertNotEqual(2, make_list(squarelotron)[23])

    def test_upside_down_flip(self):
        self.assertEqual([[5, 10, 15, 20, 25],
                          [4, 7, 8, 9, 24],
                          [3, 12, 13, 14, 23],
                          [2, 17, 18, 19, 22],
                          [1, 6, 11, 16, 21]], upside_down_flip(squarelotron, "outer"))
        
        self.assertEqual([[1, 6, 11, 16, 21],
                          [2, 17, 18, 19, 22],
                          [3, 12, 13, 14, 23],
                          [4, 7, 8, 9, 24],
                          [5, 10, 15, 20, 25]], upside_down_flip(squarelotron, "inner"))
        self.assertNotEqual([[1, 6, 11, 16, 21],
                          [2, 17, 18, 19, 22],
                          [3, 12, 13, 14, 23],
                          [4, 7, 8, 9, 24],
                          [5, 10, 15, 20, 25]], upside_down_flip(squarelotron, "outer"))

    def test_left_right_flip(self):
        self.assertEqual([[1, 6, 11, 16, 21],
                        [2, 9, 8, 7, 22],
                        [3, 14, 13, 12, 23],
                        [4, 19, 18, 17, 24],
                        [5, 10, 15, 20, 25]] ,left_right_flip(squarelotron, "inner"))
        self.assertEqual([[21, 16, 11, 6, 1],
                          [22, 7, 8, 9, 2],
                          [23, 12, 13, 14, 3],
                          [24, 17, 18, 19, 4],
                          [25, 20, 15, 10, 5]] ,left_right_flip(squarelotron, "outer"))

    def test_inverse_diagonal_flip(self):
        self.assertEqual([[1, 6, 11, 16, 21],
                          [2, 19, 14, 9, 22],
                          [3, 18, 13, 8, 23],
                          [4, 17, 12, 7, 24],
                          [5, 10, 15, 20, 25]], inverse_diagonal_flip(squarelotron, "inner"))
        self.assertEqual([[25, 24, 23, 22, 21],
                          [20, 7, 8, 9, 16],
                          [15, 12, 13, 14, 11],
                          [10, 17, 18, 19, 6],
                          [5, 4, 3, 2, 1]], inverse_diagonal_flip(squarelotron, "outer"))

    def test_main_diagonal_flip(self):
        self.assertEqual([[1, 6, 11, 16, 21],
                          [2, 7, 12, 17, 22],
                          [3, 8, 13, 18, 23],
                          [4, 9, 14, 19, 24],
                          [5, 10, 15, 20, 25]], main_diagonal_flip(squarelotron, "inner"))
        self.assertEqual([[1, 2, 3, 4, 5],
                          [6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]], main_diagonal_flip(squarelotron, "outer"))
    

unittest.main()
