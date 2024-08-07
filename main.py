import argparse
from game_state import GameState
from ai import minmax
from utils import apply_move

def play_game(red, blue, is_misere, first_player, depth):
    state = GameState(red, blue, is_misere)
    current_player = first_player

    while not state.is_game_over():
        print(f"\nCurrent state: Red: {state.red}, Blue: {state.blue}")
        if current_player == 'human':
            move = get_human_move(state)
        else:
            _, move = minmax(state, depth, float('-inf'), float('inf'), True)
            print(f"Computer chooses: {move}")

        state = apply_move(state, move)
        current_player = 'computer' if current_player == 'human' else 'human'

    print(f"\nGame over! Final state: Red: {state.red}, Blue: {state.blue}")
    score = state.get_score()
    winner = 'Human' if current_player == 'computer' else 'Computer'
    if state.is_misere:
        winner = 'Human' if current_player == 'human' else 'Computer'
    print(f"{winner} wins! Score: {score}")

def get_human_move(state):
    while True:
        try:
            color = input("Choose color (red/blue): ").lower()
            count = int(input("Choose number of marbles to remove (1-2): "))
            if color in ['red', 'blue'] and 1 <= count <= min(2, getattr(state, color)):
                return color, count
        except ValueError:
            pass
        print("Invalid move. Try again.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument("red", type=int, help="Number of red marbles")
    parser.add_argument("blue", type=int, help="Number of blue marbles")
    parser.add_argument("--version", choices=['standard', 'misere'], default='standard', help="Game version")
    parser.add_argument("--first", choices=['computer', 'human'], default='computer', help="First player")
    parser.add_argument("--depth", type=int, default=10, help="Search depth for AI")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    play_game(args.red, args.blue, args.version == 'misere', args.first, args.depth)