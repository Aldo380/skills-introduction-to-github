"""
Example usage of the Board Representation

This file demonstrates how to use the Board class for a simple tic-tac-toe game.
"""

from board import Board


def main():
    """Demonstrate board usage with a tic-tac-toe example."""
    print("Board Representation Example")
    print("=" * 40)
    print()
    
    # Create a 3x3 board for tic-tac-toe
    print("1. Creating a 3x3 board:")
    board = Board(3, 3)
    print(board)
    print()
    
    # Make some moves
    print("2. Making some moves:")
    board.set_cell(0, 0, 'X')
    board.set_cell(1, 1, 'O')
    board.set_cell(0, 2, 'X')
    board.set_cell(2, 1, 'O')
    board.set_cell(1, 0, 'X')
    print(board)
    print()
    
    # Get a specific cell value
    print("3. Getting cell value at (0, 0):")
    print(f"Cell (0, 0) = '{board.get_cell(0, 0)}'")
    print()
    
    # Clear the board
    print("4. Clearing the board:")
    board.clear()
    print(board)
    print()
    
    # Create a larger board
    print("5. Creating a 5x5 board:")
    large_board = Board(5, 5)
    large_board.set_cell(0, 0, '♔')
    large_board.set_cell(0, 4, '♚')
    large_board.set_cell(2, 2, '♟')
    print(large_board)
    print()
    
    # Demonstrate board representation
    print("6. Board representation:")
    print(f"repr: {repr(board)}")
    print()


if __name__ == "__main__":
    main()
