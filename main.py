from hangman_codes import *

previous_moves = []
bool_user_won = None

print(f"5 lives left. \n{hangmanizer(initial_word)}")
while lives > 0:
    alphabet = input('Enter your keyword..\n> ').lower()
    previous_moves.append(alphabet)
    if (alphabet in punctuation or alphabet in digits or len(alphabet) == 0) or not find_index(initial_word, alphabet):
        lives -= 1
        print("Ouch. Wrong move.")
    current_state = hangmanizer(initial_word, indices)
    print(f"{lives} lives left. Previous moves: {' '.join(previous_moves)}\n{current_state}")
    if initial_word == current_state:
        bool_user_won = True
        break
print(user_won(bool_user_won))
