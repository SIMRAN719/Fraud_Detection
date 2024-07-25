"""Word Guessing Game in Python."""
import random

high_score = 0


def get_word():
    """Get a random word from the list."""
    words = ["python", "javascript", "programming", "computer", "science"]
    return random.choice(words)


def play_word_guessing_game():
    """Play the main word guessing game."""
    global high_score
    word = get_word()
    word_letters = set(word)
    alphabet = set(chr(x) for x in range(97, 123))
    used_letters = set()
    lives = 6
    score = 0

    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                score += 10
                print('Your Current Score is: ', score)
                print('')

            else:
                lives -= 1
                print('Letter is not in the word.')
                print('You have', lives, 'lives left.')
                print('')

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
            print('')

        else:
            print('Invalid character. Please try again.')
            print('')

    if lives == 0:
        print('GAME OVER! You lost the game. The word was', word, ".")
    else:
        print('Hurray! You guessed the word', word, '!')
        print('Your total score is: ', score)
        if score > high_score:
            high_score = score
            print("Congratulations! New high score:", high_score)


def play_again():
    """Prompt the user to play the game again."""
    while True:
        choice = input("Do you want to play again? (Yes/No): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def view_high_score():
    """View the current high score."""
    print("The current high score is:", high_score)


if __name__ == "__main__":
    print("Welcome to the Word Guessing Game!")
    print(
        "~~~Instructions~~~\n"
        "1. Enter one letter at a time.\n"
        "2. You have a total of 6 lives.\n"
        "3. For every wrong answer, you lose one chance.\n"
        "4. For every correct answer, you get 10 points.\n")
    while True:
        choice = input(
            "Choose an option:\n"
            "1. Play Game\n"
            "2. View High Score\n"
            "3. Exit\n"
            "Enter your choice: ")

        if choice == '1':
            while True:
                play_word_guessing_game()
                if not play_again():
                    break
        elif choice == '2':
            view_high_score()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose from 1, 2, or 3.")
