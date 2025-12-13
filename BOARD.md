# Board Representation

A simple and flexible board representation implementation in Python for grid-based games.

## Overview

This module provides a `Board` class that can represent any grid-based game board (e.g., tic-tac-toe, chess, checkers, etc.). The board is implemented as a 2D array with methods to manipulate and display the board state.

## Features

- **Flexible dimensions**: Create boards of any size (rows × columns)
- **Cell manipulation**: Get and set values at specific coordinates
- **Boundary checking**: Automatic validation of row/column indices
- **Display methods**: Pretty-print the board to console
- **Clear functionality**: Reset the board to its initial empty state

## Installation

No installation required. Simply copy the `board.py` file to your project.

## Usage

### Basic Example

```python
from board import Board

# Create a 3x3 board (default)
board = Board()

# Set some values
board.set_cell(0, 0, 'X')
board.set_cell(1, 1, 'O')

# Display the board
print(board)
```

Output:
```
X |   |  
-----------
  | O |  
-----------
  |   |  
```

### Custom Board Size

```python
# Create a 5x5 board
board = Board(5, 5)
```

### Get Cell Value

```python
value = board.get_cell(0, 0)
print(value)  # 'X'
```

### Clear Board

```python
board.clear()
print(board)  # Shows an empty board
```

## API Reference

### `Board(rows=3, cols=3)`

Create a new board with specified dimensions.

**Parameters:**
- `rows` (int): Number of rows (default: 3)
- `cols` (int): Number of columns (default: 3)

### `get_cell(row, col)`

Get the value at a specific cell.

**Parameters:**
- `row` (int): Row index (0-based)
- `col` (int): Column index (0-based)

**Returns:** The value at the specified cell

**Raises:** `IndexError` if indices are out of bounds

### `set_cell(row, col, value)`

Set the value at a specific cell.

**Parameters:**
- `row` (int): Row index (0-based)
- `col` (int): Column index (0-based)
- `value` (str): Value to set

**Raises:** `IndexError` if indices are out of bounds

### `clear()`

Clear the board by resetting all cells to empty.

### `display()`

Get a string representation of the board.

**Returns:** String representation of the board

## Running Tests

Run the test suite with:

```bash
python3 -m unittest test_board.py -v
```

## Example

See `example.py` for a complete demonstration of the board representation features.

```bash
python3 example.py
```

## License

This implementation is part of the skills-introduction-to-github repository and follows the same license.
