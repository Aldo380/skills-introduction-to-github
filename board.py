"""
Board Representation Module

This module provides a simple board representation for grid-based games.
The board can be used for games like tic-tac-toe, chess, or any grid-based game.
"""


class Board:
    """
    A class to represent a game board.
    
    Attributes:
        rows (int): Number of rows in the board
        cols (int): Number of columns in the board
        board (list): 2D list representing the board state
    """
    
    def __init__(self, rows=3, cols=3):
        """
        Initialize a board with the specified dimensions.
        
        Args:
            rows (int): Number of rows (default: 3)
            cols (int): Number of columns (default: 3)
        """
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def get_cell(self, row, col):
        """
        Get the value at a specific cell.
        
        Args:
            row (int): Row index
            col (int): Column index
            
        Returns:
            str: The value at the specified cell
            
        Raises:
            IndexError: If row or col is out of bounds
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Row or column index out of bounds")
        return self.board[row][col]
    
    def set_cell(self, row, col, value):
        """
        Set the value at a specific cell.
        
        Args:
            row (int): Row index
            col (int): Column index
            value (str): Value to set
            
        Raises:
            IndexError: If row or col is out of bounds
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Row or column index out of bounds")
        self.board[row][col] = value
    
    def clear(self):
        """Clear the board by resetting all cells to empty."""
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
    
    def display(self):
        """
        Display the board in a readable format.
        
        Returns:
            str: String representation of the board
        """
        result = []
        for i, row in enumerate(self.board):
            result.append(' | '.join(row))
            if i < self.rows - 1:
                result.append('-' * (self.cols * 4 - 1))
        return '\n'.join(result)
    
    def __str__(self):
        """Return string representation of the board."""
        return self.display()
    
    def __repr__(self):
        """Return detailed representation of the board."""
        return f"Board(rows={self.rows}, cols={self.cols})"
