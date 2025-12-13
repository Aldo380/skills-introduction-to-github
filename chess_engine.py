#!/usr/bin/env python3
"""
A simple chess engine implementation.

This chess engine supports standard chess rules including:
- All piece movements (King, Queen, Rook, Bishop, Knight, Pawn)
- Turn-based gameplay
- Move validation
- Check detection
- Basic game state management
"""


class ChessEngine:
    """Main chess engine class that manages the game state and rules."""
    
    def __init__(self):
        """Initialize the chess board with pieces in starting positions."""
        self.board = self._create_initial_board()
        self.current_turn = 'white'
        self.move_history = []
        
    def _create_initial_board(self):
        """Create the initial 8x8 chess board with pieces."""
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place black pieces (row 0 and 1)
        board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        board[1] = ['p'] * 8
        
        # Place white pieces (row 6 and 7)
        board[6] = ['P'] * 8
        board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        
        return board
    
    def display_board(self):
        """Display the current board state."""
        print("\n  a b c d e f g h")
        print("  ---------------")
        for i in range(8):
            row_display = f"{8-i}|"
            for j in range(8):
                piece = self.board[i][j]
                row_display += f"{piece if piece else '.'} "
            row_display += f"|{8-i}"
            print(row_display)
        print("  ---------------")
        print("  a b c d e f g h\n")
        
    def get_piece_at(self, row, col):
        """Get the piece at the specified position."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def is_white_piece(self, piece):
        """Check if a piece belongs to white."""
        return piece and piece.isupper()
    
    def is_black_piece(self, piece):
        """Check if a piece belongs to black."""
        return piece and piece.islower()
    
    def is_valid_position(self, row, col):
        """Check if a position is within board bounds."""
        return 0 <= row < 8 and 0 <= col < 8
    
    def parse_position(self, pos):
        """Convert chess notation (e.g., 'e2') to board coordinates."""
        if len(pos) != 2:
            return None, None
        col = ord(pos[0].lower()) - ord('a')
        row = 8 - int(pos[1])
        if self.is_valid_position(row, col):
            return row, col
        return None, None
    
    def is_valid_pawn_move(self, from_row, from_col, to_row, to_col, piece):
        """Validate pawn movement."""
        direction = -1 if self.is_white_piece(piece) else 1
        start_row = 6 if self.is_white_piece(piece) else 1
        
        # Move forward one square
        if from_col == to_col and to_row == from_row + direction:
            return self.board[to_row][to_col] is None
        
        # Move forward two squares from starting position
        if from_col == to_col and from_row == start_row and to_row == from_row + 2 * direction:
            return (self.board[to_row][to_col] is None and 
                    self.board[from_row + direction][from_col] is None)
        
        # Capture diagonally
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            target = self.board[to_row][to_col]
            if target:
                return (self.is_white_piece(piece) and self.is_black_piece(target)) or \
                       (self.is_black_piece(piece) and self.is_white_piece(target))
        
        return False
    
    def is_valid_rook_move(self, from_row, from_col, to_row, to_col):
        """Validate rook movement (horizontal or vertical)."""
        if from_row != to_row and from_col != to_col:
            return False
        
        # Check path is clear
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.board[from_row][col] is not None:
                    return False
        else:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.board[row][from_col] is not None:
                    return False
        
        return True
    
    def is_valid_bishop_move(self, from_row, from_col, to_row, to_col):
        """Validate bishop movement (diagonal)."""
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        
        # Check path is clear
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if self.board[row][col] is not None:
                return False
            row += row_step
            col += col_step
        
        return True
    
    def is_valid_knight_move(self, from_row, from_col, to_row, to_col):
        """Validate knight movement (L-shape)."""
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
    
    def is_valid_queen_move(self, from_row, from_col, to_row, to_col):
        """Validate queen movement (combination of rook and bishop)."""
        return (self.is_valid_rook_move(from_row, from_col, to_row, to_col) or
                self.is_valid_bishop_move(from_row, from_col, to_row, to_col))
    
    def is_valid_king_move(self, from_row, from_col, to_row, to_col):
        """Validate king movement (one square in any direction)."""
        return abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1
    
    def is_valid_move(self, from_pos, to_pos):
        """Check if a move is valid according to chess rules."""
        from_row, from_col = self.parse_position(from_pos)
        to_row, to_col = self.parse_position(to_pos)
        
        if from_row is None or to_row is None:
            return False, "Invalid position format"
        
        if from_row == to_row and from_col == to_col:
            return False, "Source and destination are the same"
        
        piece = self.board[from_row][from_col]
        if piece is None:
            return False, "No piece at source position"
        
        # Check if it's the correct player's turn
        if (self.current_turn == 'white' and not self.is_white_piece(piece)) or \
           (self.current_turn == 'black' and not self.is_black_piece(piece)):
            return False, f"It's {self.current_turn}'s turn"
        
        # Check if destination has own piece
        target = self.board[to_row][to_col]
        if target:
            if (self.is_white_piece(piece) and self.is_white_piece(target)) or \
               (self.is_black_piece(piece) and self.is_black_piece(target)):
                return False, "Cannot capture own piece"
        
        # Validate move based on piece type
        piece_type = piece.lower()
        valid = False
        
        if piece_type == 'p':
            valid = self.is_valid_pawn_move(from_row, from_col, to_row, to_col, piece)
        elif piece_type == 'r':
            valid = self.is_valid_rook_move(from_row, from_col, to_row, to_col)
        elif piece_type == 'n':
            valid = self.is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece_type == 'b':
            valid = self.is_valid_bishop_move(from_row, from_col, to_row, to_col)
        elif piece_type == 'q':
            valid = self.is_valid_queen_move(from_row, from_col, to_row, to_col)
        elif piece_type == 'k':
            valid = self.is_valid_king_move(from_row, from_col, to_row, to_col)
        
        if not valid:
            return False, f"Invalid move for {piece_type}"
        
        return True, "Valid move"
    
    def make_move(self, from_pos, to_pos):
        """Execute a move on the board."""
        valid, message = self.is_valid_move(from_pos, to_pos)
        
        if not valid:
            return False, message
        
        from_row, from_col = self.parse_position(from_pos)
        to_row, to_col = self.parse_position(to_pos)
        
        # Record move
        piece = self.board[from_row][from_col]
        captured = self.board[to_row][to_col]
        self.move_history.append({
            'from': from_pos,
            'to': to_pos,
            'piece': piece,
            'captured': captured
        })
        
        # Execute move
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        
        # Switch turns
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        
        return True, f"Moved {piece} from {from_pos} to {to_pos}"
    
    def find_king(self, is_white):
        """Find the position of the king for the specified color."""
        king = 'K' if is_white else 'k'
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == king:
                    return row, col
        return None, None
    
    def is_position_under_attack(self, row, col, by_white):
        """Check if a position is under attack by the specified color."""
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece is None:
                    continue
                
                # Check if piece belongs to attacking color
                if (by_white and not self.is_white_piece(piece)) or \
                   (not by_white and not self.is_black_piece(piece)):
                    continue
                
                # Check if this piece can attack the position
                piece_type = piece.lower()
                if piece_type == 'p':
                    # Pawn attacks diagonally
                    direction = -1 if by_white else 1
                    if row == r + direction and abs(col - c) == 1:
                        return True
                elif piece_type == 'r':
                    if self.is_valid_rook_move(r, c, row, col):
                        return True
                elif piece_type == 'n':
                    if self.is_valid_knight_move(r, c, row, col):
                        return True
                elif piece_type == 'b':
                    if self.is_valid_bishop_move(r, c, row, col):
                        return True
                elif piece_type == 'q':
                    if self.is_valid_queen_move(r, c, row, col):
                        return True
                elif piece_type == 'k':
                    if self.is_valid_king_move(r, c, row, col):
                        return True
        
        return False
    
    def is_in_check(self, is_white):
        """Check if the specified color's king is in check."""
        king_row, king_col = self.find_king(is_white)
        if king_row is None:
            return False
        
        return self.is_position_under_attack(king_row, king_col, not is_white)
    
    def get_game_state(self):
        """Get the current game state."""
        white_in_check = self.is_in_check(True)
        black_in_check = self.is_in_check(False)
        
        state = {
            'current_turn': self.current_turn,
            'white_in_check': white_in_check,
            'black_in_check': black_in_check,
            'moves_made': len(self.move_history)
        }
        
        return state


def main():
    """Main function to run the chess game."""
    print("=" * 50)
    print("         CHESS ENGINE")
    print("=" * 50)
    print("\nPiece notation:")
    print("  White: K(King) Q(Queen) R(Rook) B(Bishop) N(Knight) P(Pawn)")
    print("  Black: k(king) q(queen) r(rook) b(bishop) n(knight) p(pawn)")
    print("\nMove format: e2 e4 (from to)")
    print("Type 'quit' to exit\n")
    
    engine = ChessEngine()
    engine.display_board()
    
    while True:
        state = engine.get_game_state()
        
        # Display check status
        if state['white_in_check']:
            print("⚠️  White king is in CHECK!")
        if state['black_in_check']:
            print("⚠️  Black king is in CHECK!")
        
        # Get player move
        print(f"{state['current_turn'].capitalize()}'s turn")
        move_input = input("Enter move (e.g., 'e2 e4'): ").strip()
        
        if move_input.lower() == 'quit':
            print("Thanks for playing!")
            break
        
        parts = move_input.split()
        if len(parts) != 2:
            print("Invalid format. Use: from_pos to_pos (e.g., 'e2 e4')\n")
            continue
        
        from_pos, to_pos = parts[0], parts[1]
        success, message = engine.make_move(from_pos, to_pos)
        
        if success:
            print(f"✓ {message}")
            engine.display_board()
        else:
            print(f"✗ {message}\n")


if __name__ == "__main__":
    main()
