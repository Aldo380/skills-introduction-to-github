"""
Tests for the Board Representation Module

This module contains tests for the Board class.
"""

import unittest
from board import Board


class TestBoard(unittest.TestCase):
    """Test cases for the Board class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.board = Board()
    
    def test_board_initialization(self):
        """Test that a board initializes with correct dimensions."""
        self.assertEqual(self.board.rows, 3)
        self.assertEqual(self.board.cols, 3)
        self.assertEqual(len(self.board.board), 3)
        self.assertEqual(len(self.board.board[0]), 3)
    
    def test_custom_dimensions(self):
        """Test board initialization with custom dimensions."""
        custom_board = Board(5, 4)
        self.assertEqual(custom_board.rows, 5)
        self.assertEqual(custom_board.cols, 4)
        self.assertEqual(len(custom_board.board), 5)
        self.assertEqual(len(custom_board.board[0]), 4)
    
    def test_initial_cells_empty(self):
        """Test that all cells are initially empty."""
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                self.assertEqual(self.board.get_cell(row, col), ' ')
    
    def test_set_and_get_cell(self):
        """Test setting and getting cell values."""
        self.board.set_cell(0, 0, 'X')
        self.assertEqual(self.board.get_cell(0, 0), 'X')
        
        self.board.set_cell(1, 2, 'O')
        self.assertEqual(self.board.get_cell(1, 2), 'O')
    
    def test_set_cell_out_of_bounds(self):
        """Test that setting a cell out of bounds raises IndexError."""
        with self.assertRaises(IndexError):
            self.board.set_cell(3, 0, 'X')
        
        with self.assertRaises(IndexError):
            self.board.set_cell(0, 3, 'X')
        
        with self.assertRaises(IndexError):
            self.board.set_cell(-1, 0, 'X')
    
    def test_get_cell_out_of_bounds(self):
        """Test that getting a cell out of bounds raises IndexError."""
        with self.assertRaises(IndexError):
            self.board.get_cell(3, 0)
        
        with self.assertRaises(IndexError):
            self.board.get_cell(0, 3)
        
        with self.assertRaises(IndexError):
            self.board.get_cell(-1, 0)
    
    def test_clear_board(self):
        """Test clearing the board."""
        self.board.set_cell(0, 0, 'X')
        self.board.set_cell(1, 1, 'O')
        self.board.set_cell(2, 2, 'X')
        
        self.board.clear()
        
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                self.assertEqual(self.board.get_cell(row, col), ' ')
    
    def test_display(self):
        """Test board display functionality."""
        self.board.set_cell(0, 0, 'X')
        self.board.set_cell(1, 1, 'O')
        self.board.set_cell(2, 2, 'X')
        
        display_output = self.board.display()
        self.assertIn('X', display_output)
        self.assertIn('O', display_output)
        self.assertIn('|', display_output)
        self.assertIn('-', display_output)
    
    def test_str_representation(self):
        """Test string representation of the board."""
        str_output = str(self.board)
        self.assertIsInstance(str_output, str)
        self.assertIn('|', str_output)
    
    def test_repr_representation(self):
        """Test detailed representation of the board."""
        repr_output = repr(self.board)
        self.assertEqual(repr_output, "Board(rows=3, cols=3)")
        
        custom_board = Board(5, 4)
        self.assertEqual(repr(custom_board), "Board(rows=5, cols=4)")


if __name__ == '__main__':
    unittest.main()
