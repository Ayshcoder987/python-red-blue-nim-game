from utils import get_possible_moves, apply_move

def minmax(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state.is_game_over():
        return state.get_score(), None

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(state):
            new_state = apply_move(state.clone(), move)
            eval, _ = minmax(new_state, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in get_possible_moves(state):
            new_state = apply_move(state.clone(), move)
            eval, _ = minmax(new_state, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move