MAX_REMOVE = 2

def get_possible_moves(state):
    moves = []
    for color in ['red', 'blue']:
        for count in range(1, min(MAX_REMOVE, getattr(state, color)) + 1):
            moves.append((color, count))
    return moves if not state.is_misere else reversed(moves)

def apply_move(state, move):
    color, count = move
    setattr(state, color, getattr(state, color) - count)
    return state