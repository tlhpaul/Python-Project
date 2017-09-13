import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-' 

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0, 0), string_to_location("A1"))
        self.assertNotEqual((0, 1), string_to_location(("A1")))


    def test_location_to_string(self):
        self.assertEqual("B1", location_to_string((1, 0)))
        self.assertNotEqual("B2", location_to_string((1, 0)))

    def test_at(self):
        self.assertEqual("-", at((1, 1)))
        self.assertNotEqual("M", at((0, 0)))
        

    def test_all_locations(self):
        self.assertEqual([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], all_locations())
        self.assertNotEqual([(0 ,0)], all_locations())
 

    def test_adjacent_location(self):
        self.assertEqual((2, 1), adjacent_location((2, 2), "left"))
        self.assertNotEqual((2, 1), adjacent_location((1, 2), "left"))
        
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((1, 3), "down"))
        self.assertFalse(is_legal_move_by_musketeer((2, 2), "down"))

        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((3, 1), "right"))
        self.assertFalse(is_legal_move_by_enemy((3, 1), "up"))
 

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((1, 3), "down"))
        self.assertFalse(is_legal_move((2, 3), "up"))

    def test_can_move_piece_at(self):
        self.assertTrue(can_move_piece_at((2, 2)))
        self.assertFalse(can_move_piece_at((0, 3)))

        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(has_some_legal_move_somewhere("R"))
        self.assertFalse(has_some_legal_move_somewhere("M"))
        
 
    def test_possible_moves_from(self):
        self.assertEqual(["up", "right", "left"], possible_moves_from((2, 2)))
        self.assertNotEqual(["left"], possible_moves_from((1, 1)))


    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((1, 4)))
        self.assertFalse(can_move_piece_at((1, 3)))
 

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((2, 2)))
        self.assertFalse(is_legal_location((5, 5)))
        
    def test_is_within_board(self):
        self.assertTrue(is_within_board((0, 0), "right"))
        self.assertFalse(is_within_board((4, 0), "down"))
                         
    
    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual([((0, 3), "right"), ((0, 3), "left"), ((1, 4), "up")], all_possible_moves_for("M"))
        self.assertNotEqual([(1, 5)], all_possible_moves_for("R"))
 
    
        
    def test_make_move(self):
        self.assertEqual((2, 2), make_move((2, 1), "right"))
        self.assertNotEqual((3, 3), make_move((2, 1), "right"))
 
        
    def test_choose_computer_move(self):
        self.assertEqual(choose_computer_move("R")[0], (1, 2))


    def test_is_enemy_win(self):
        self.assertFalse(is_enemy_win())
 

unittest.main()
