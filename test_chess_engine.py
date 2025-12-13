#!/usr/bin/env python3
"""
Test suite for the chess engine.

Tests basic functionality including:
- Board initialization
- Piece movement validation
- Move execution
- Check detection
"""

import unittest
from chess_engine import ChessEngine


class TestChessEngine(unittest.TestCase):
    """Test cases for the ChessEngine class."""
    
    def setUp(self):
        """Set up a fresh chess engine for each test."""
        self.engine = ChessEngine()
    
    def test_board_initialization(self):
        """Test that the board is initialized correctly."""
        # Check that board is 8x8
        self.assertEqual(len(self.engine.board), 8)
        for row in self.engine.board:
            self.assertEqual(len(row), 8)
        
        # Check white pieces
        self.assertEqual(self.engine.board[7][0], 'R')  # White rook
        self.assertEqual(self.engine.board[7][4], 'K')  # White king
        self.assertEqual(self.engine.board[6][0], 'P')  # White pawn
        
        # Check black pieces
        self.assertEqual(self.engine.board[0][0], 'r')  # Black rook
        self.assertEqual(self.engine.board[0][4], 'k')  # Black king
        self.assertEqual(self.engine.board[1][0], 'p')  # Black pawn
        
        # Check empty squares
        self.assertIsNone(self.engine.board[3][3])
        self.assertIsNone(self.engine.board[4][4])
    
    def test_initial_turn(self):
        """Test that white goes first."""
        self.assertEqual(self.engine.current_turn, 'white')
    
    def test_parse_position(self):
        """Test position parsing from chess notation."""
        # Test valid positions
        self.assertEqual(self.engine.parse_position('a1'), (7, 0))
        self.assertEqual(self.engine.parse_position('h8'), (0, 7))
        self.assertEqual(self.engine.parse_position('e4'), (4, 4))
        
        # Test invalid positions
        self.assertEqual(self.engine.parse_position('i9'), (None, None))
        self.assertEqual(self.engine.parse_position('a0'), (None, None))
        self.assertEqual(self.engine.parse_position(''), (None, None))
        
        # Test invalid input that could cause ValueError
        self.assertEqual(self.engine.parse_position('a@'), (None, None))
        self.assertEqual(self.engine.parse_position('ez'), (None, None))
        self.assertEqual(self.engine.parse_position('1a'), (None, None))
    
    def test_valid_pawn_move(self):
        """Test pawn movement rules."""
        # Valid pawn move forward one square
        valid, msg = self.engine.is_valid_move('e2', 'e3')
        self.assertTrue(valid)
        
        # Valid pawn move forward two squares from start
        valid, msg = self.engine.is_valid_move('e2', 'e4')
        self.assertTrue(valid)
        
        # Invalid pawn move (too far)
        valid, msg = self.engine.is_valid_move('e2', 'e5')
        self.assertFalse(valid)
    
    def test_pawn_capture(self):
        """Test pawn diagonal capture."""
        # Set up a scenario where pawn can capture
        self.engine.board[5][4] = 'P'  # White pawn at e3
        self.engine.board[4][5] = 'p'  # Black pawn at f4
        
        # Pawn should be able to capture diagonally
        valid, msg = self.engine.is_valid_move('e3', 'f4')
        self.assertTrue(valid)
        
        # Pawn should not capture own piece
        self.engine.board[4][5] = 'P'  # Change to white pawn
        valid, msg = self.engine.is_valid_move('e3', 'f4')
        self.assertFalse(valid)
    
    def test_rook_movement(self):
        """Test rook movement rules."""
        # Clear path for rook
        self.engine.board[7][0] = None
        self.engine.board[4][0] = 'R'  # Place white rook at a4
        
        # Valid horizontal move
        valid, msg = self.engine.is_valid_move('a4', 'h4')
        self.assertTrue(valid)
        
        # Valid vertical move
        valid, msg = self.engine.is_valid_move('a4', 'a3')
        self.assertTrue(valid)
        
        # Invalid diagonal move
        valid, msg = self.engine.is_valid_move('a4', 'b5')
        self.assertFalse(valid)
    
    def test_knight_movement(self):
        """Test knight movement rules (L-shape)."""
        # Valid knight move
        valid, msg = self.engine.is_valid_move('b1', 'c3')
        self.assertTrue(valid)
        
        valid, msg = self.engine.is_valid_move('g1', 'f3')
        self.assertTrue(valid)
        
        # Invalid knight move
        valid, msg = self.engine.is_valid_move('b1', 'd1')
        self.assertFalse(valid)
    
    def test_bishop_movement(self):
        """Test bishop movement rules."""
        # Clear path for bishop
        self.engine.board[6][2] = None  # Remove pawn
        self.engine.board[4][2] = 'B'  # Place white bishop at c4
        
        # Valid diagonal move
        valid, msg = self.engine.is_valid_move('c4', 'f7')
        self.assertTrue(valid)
        
        # Invalid horizontal move
        valid, msg = self.engine.is_valid_move('c4', 'h4')
        self.assertFalse(valid)
    
    def test_queen_movement(self):
        """Test queen movement rules."""
        # Clear path for queen
        self.engine.board[6][3] = None  # Remove pawn
        self.engine.board[4][3] = 'Q'  # Place white queen at d4
        
        # Valid horizontal move
        valid, msg = self.engine.is_valid_move('d4', 'h4')
        self.assertTrue(valid)
        
        # Valid diagonal move
        valid, msg = self.engine.is_valid_move('d4', 'g7')
        self.assertTrue(valid)
    
    def test_king_movement(self):
        """Test king movement rules."""
        # Clear space for king
        self.engine.board[6][4] = None  # Remove pawn
        self.engine.board[5][4] = 'K'  # Place white king at e3
        
        # Valid king move (one square)
        valid, msg = self.engine.is_valid_move('e3', 'e4')
        self.assertTrue(valid)
        
        valid, msg = self.engine.is_valid_move('e3', 'f4')
        self.assertTrue(valid)
        
        # Invalid king move (too far)
        valid, msg = self.engine.is_valid_move('e3', 'e5')
        self.assertFalse(valid)
    
    def test_turn_switching(self):
        """Test that turns alternate correctly."""
        self.assertEqual(self.engine.current_turn, 'white')
        
        # Make a valid move
        success, msg = self.engine.make_move('e2', 'e4')
        self.assertTrue(success)
        self.assertEqual(self.engine.current_turn, 'black')
        
        # Try to move white piece on black's turn
        valid, msg = self.engine.is_valid_move('d2', 'd4')
        self.assertFalse(valid)
        
        # Make a black move
        success, msg = self.engine.make_move('e7', 'e5')
        self.assertTrue(success)
        self.assertEqual(self.engine.current_turn, 'white')
    
    def test_cannot_capture_own_piece(self):
        """Test that pieces cannot capture their own color."""
        valid, msg = self.engine.is_valid_move('e2', 'e1')
        self.assertFalse(valid)
    
    def test_path_blocking(self):
        """Test that pieces cannot move through other pieces."""
        # Rook cannot move through pawns
        valid, msg = self.engine.is_valid_move('a1', 'a3')
        self.assertFalse(valid)
        
        # Bishop cannot move through pawns
        valid, msg = self.engine.is_valid_move('c1', 'f4')
        self.assertFalse(valid)
    
    def test_move_history(self):
        """Test that move history is recorded."""
        self.assertEqual(len(self.engine.move_history), 0)
        
        self.engine.make_move('e2', 'e4')
        self.assertEqual(len(self.engine.move_history), 1)
        
        self.engine.make_move('e7', 'e5')
        self.assertEqual(len(self.engine.move_history), 2)
        
        # Check move details
        first_move = self.engine.move_history[0]
        self.assertEqual(first_move['from'], 'e2')
        self.assertEqual(first_move['to'], 'e4')
        self.assertEqual(first_move['piece'], 'P')
    
    def test_find_king(self):
        """Test finding king positions."""
        white_row, white_col = self.engine.find_king(True)
        self.assertEqual(white_row, 7)
        self.assertEqual(white_col, 4)
        
        black_row, black_col = self.engine.find_king(False)
        self.assertEqual(black_row, 0)
        self.assertEqual(black_col, 4)
    
    def test_check_detection(self):
        """Test check detection."""
        # Initially no check
        self.assertFalse(self.engine.is_in_check(True))
        self.assertFalse(self.engine.is_in_check(False))
        
        # Set up a check scenario
        self.engine.board[6][4] = None  # Remove white pawn
        self.engine.board[5][4] = 'r'  # Place black rook attacking white king
        
        # White should be in check
        self.assertTrue(self.engine.is_in_check(True))
        self.assertFalse(self.engine.is_in_check(False))
    
    def test_game_state(self):
        """Test game state tracking."""
        state = self.engine.get_game_state()
        
        self.assertEqual(state['current_turn'], 'white')
        self.assertEqual(state['moves_made'], 0)
        self.assertFalse(state['white_in_check'])
        self.assertFalse(state['black_in_check'])
        
        # Make a move and check state update
        self.engine.make_move('e2', 'e4')
        state = self.engine.get_game_state()
        
        self.assertEqual(state['current_turn'], 'black')
        self.assertEqual(state['moves_made'], 1)


if __name__ == '__main__':
    unittest.main()
