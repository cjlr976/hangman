import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!']

    for line in welcome:
        print(line)

    HANGMAN = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |   | 
    |   | 
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |   | 
    |   | 
    |  |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |   | 
    |   | 
    |  | 
    |  | 
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |   | 
    |   | 
    |  | | 
    |  | 
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\\ 
    |   | 
    |   | 
    |  | | 
    |  | | 
    --------
    """)

    play_again = True

    while play_again:
        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]
        chosen_word = random.choice(words).lower()
        player_guess = None
        guessed_letters = []
        word_guessed = ["-"] * len(chosen_word)
        attempts = 10  # Set the number of attempts

        print(HANGMAN[0])  # Print the initial hangman state

        while attempts > 0 and "-" in word_guessed:
            print(f"\nYou have {attempts} attempts remaining")
            print("".join(word_guessed))

            player_guess = input("\nPlease select a letter between A-Z\n> ").lower()

            if not player_guess.isalpha() or len(player_guess) > 1 or player_guess in guessed_letters:
                print("Invalid guess. Please try again.")
                continue

            guessed_letters.append(player_guess)

            if player_guess in chosen_word:
                for i in range(len(chosen_word)):
                    if player_guess == chosen_word[i]:
                        word_guessed[i] = player_guess
            else:
                attempts -= 1
                print(HANGMAN[10 - attempts - 1])  # Show the appropriate hangman state

        if "-" not in word_guessed:
            print(f"\nCongratulations! {chosen_word} was the word.")
        else:
            print(f"\nUnlucky! The word was {chosen_word}.")

        print("\nWould you like to play again? (yes or no)")
        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
