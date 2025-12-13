# Chess Engine

A simple yet functional chess engine implementation in Python that supports standard chess rules and provides an interactive command-line interface for gameplay.

## Features

- **Complete Chess Rules Implementation**
  - All standard piece movements (King, Queen, Rook, Bishop, Knight, Pawn)
  - Pawn special moves (two-square initial move, diagonal capture)
  - Turn-based gameplay
  - Move validation
  - Check detection
  - Move history tracking

- **Interactive CLI Interface**
  - Clear board visualization
  - Chess notation for moves (e.g., "e2 e4")
  - Real-time check warnings
  - Move validation feedback

## Requirements

- Python 3.6 or higher

## Usage

### Playing the Game

Run the chess engine:

```bash
python3 chess_engine.py
```

### Making Moves

Moves are entered using standard chess notation:
- Format: `from_position to_position`
- Example: `e2 e4` (moves piece from e2 to e4)

Columns are labeled a-h (left to right)
Rows are labeled 1-8 (bottom to top)

### Piece Notation

- **White pieces (uppercase):** K (King), Q (Queen), R (Rook), B (Bishop), N (Knight), P (Pawn)
- **Black pieces (lowercase):** k (king), q (queen), r (rook), b (bishop), n (knight), p (pawn)

### Example Game Session

```
  a b c d e f g h
  ---------------
8|r n b q k b n r|8
7|p p p p p p p p|7
6|. . . . . . . .|6
5|. . . . . . . .|5
4|. . . . . . . .|4
3|. . . . . . . .|3
2|P P P P P P P P|2
1|R N B Q K B N R|1
  ---------------
  a b c d e f g h

White's turn
Enter move (e.g., 'e2 e4'): e2 e4
✓ Moved P from e2 to e4
```

## Running Tests

The chess engine includes a comprehensive test suite:

```bash
python3 -m unittest test_chess_engine.py
```

Or run with verbose output:

```bash
python3 -m unittest test_chess_engine.py -v
```

## API Usage

You can also use the chess engine programmatically:

```python
from chess_engine import ChessEngine

# Create a new game
engine = ChessEngine()

# Display the board
engine.display_board()

# Make a move
success, message = engine.make_move('e2', 'e4')
if success:
    print(f"Move successful: {message}")
else:
    print(f"Invalid move: {message}")

# Check game state
state = engine.get_game_state()
print(f"Current turn: {state['current_turn']}")
print(f"White in check: {state['white_in_check']}")
print(f"Black in check: {state['black_in_check']}")
```

## Architecture

The chess engine is built with a modular design:

### Core Components

1. **Board Representation**
   - 8x8 2D array
   - Pieces represented as characters (uppercase for white, lowercase for black)

2. **Move Validation**
   - Separate validation methods for each piece type
   - Path checking for sliding pieces (Rook, Bishop, Queen)
   - Turn validation
   - Capture validation

3. **Game State Management**
   - Turn tracking
   - Move history
   - Check detection
   - King position tracking

## Limitations

This is a basic implementation focused on core chess rules. The following features are not yet implemented:

- Checkmate detection
- Stalemate detection
- Castling
- En passant
- Pawn promotion
- Draw conditions (50-move rule, threefold repetition)
- AI opponent

## Contributing

Contributions are welcome! Areas for improvement:

- Implement advanced chess rules (castling, en passant, promotion)
- Add checkmate and stalemate detection
- Implement an AI opponent
- Add a graphical user interface
- Improve performance with bitboard representation

## License

MIT License - See LICENSE file for details

## Author

Created as part of the skills-introduction-to-github repository.
