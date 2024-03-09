import random

def roll_dice():
    return random.randint(1, 6)

def move_piece(piece, num_players, dice_results):
    for _ in range(dice_results):
        piece = (piece + 1) % num_players
    return piece

def simulate_game(num_games, num_players):
    win_counts = [0] * num_players
    for _ in range(num_games):
        piece = 0
        dice_results = [roll_dice() for _ in range(num_players - 1)]
        dice_results.sort(reverse=True)
        piece = move_piece(piece, num_players, dice_results)
        win_counts[piece] += 1
    return win_counts

def calculate_probabilities(win_counts, num_games):
    probabilities = [count / num_games for count in win_counts]
    return probabilities

def main():
    num_games = 10000
    num_players = 4
    win_counts = simulate_game(num_games, num_players)
    probabilities = calculate_probabilities(win_counts, num_games)
    print(f"Probabilities of winning for each of the {num_players} players: {probabilities}")

if __name__ == "__main__":
    main()
