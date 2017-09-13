import unittest
from cities import *

road_map = [("Alabama", "Montgomery", 32.361538, -86.279118),
                    ("Maine", "Augusta", 44.323535, -69.765261),
                    ("West Virginia", "Charleston", 38.349497, -81.633294),
                    ("South Dakota", "Pierre", 44.367966, -100.336378)]

class TestCities(unittest.TestCase):
    
    def test_compute_total_distance(self):
    
        self.assertAlmostEqual(4126.2, compute_total_distance(road_map), 1)

        self.assertNotEqual(4707.5, compute_total_distance(road_map), 2)

    def test_swap_adjacent_cities(self):
        
        self.assertEqual(([("Alabama", "Montgomery", 32.361538, -86.279118),
                    ("Maine", "Augusta", 44.323535, -69.765261),
                    ("South Dakota", "Pierre", 44.367966, -100.336378),
                    ("West Virginia", "Charleston", 38.349497, -81.633294)]),
                         swap_adjacent_cities(road_map, 2)[0])
        
        self.assertAlmostEqual(4254.2, swap_adjacent_cities(road_map, 2)[1], 1)

    def test_swap_cities(self):
        
        self.assertEqual(([("South Dakota", "Pierre", 44.367966, -100.336378),
                    ("Maine", "Augusta", 44.323535, -69.765261),
                    ("West Virginia", "Charleston", 38.349497, -81.633294),
                    ("Alabama", "Montgomery", 32.361538, -86.279118)])
                               , swap_cities(road_map, 0, 3)[0])
        
        self.assertAlmostEqual(3851.4, swap_cities(road_map, 0, 3)[1], 1)
        
    def test_find_best_cycle(self):
        
        self.assertEqual(set([("South Dakota", "Pierre", 44.367966, -100.336378),
                    ("Maine", "Augusta", 44.323535, -69.765261),
                    ("West Virginia", "Charleston", 38.349497, -81.633294),
                    ("Alabama", "Montgomery", 32.361538, -86.279118)]), set(find_best_cycle(road_map)))
        
        self.assertNotEqual([("Maine", "Augusta", 44.323535, -69.765261),
                    ("South Dakota", "Pierre", 44.367966, -100.336378),
                    ("West Virginia", "Charleston", 38.349497, -81.633294),
                    ("Alabama", "Montgomery", 32.361538, -86.279118)], find_best_cycle(road_map))
        
unittest.main()
