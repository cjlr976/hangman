import random

def main():
        x = (1,2,3,4,5,6)

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
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
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
| /-+-\ 
|   | 
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
| /-+-\ 
|   | 
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
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
        welcome = "Welcome to hangman do instructions"
        print(welcome)

        play_again = True
        while play_again: 
                words = ("hangman", "chairs", "key", "fly", "hi")

                chosen_word = random.choice(words).lower()

                player_guess = None
                guessed_letters = []
                words_guessed = []

                for letter in chosen_word:
                        words_guessed.append("-")
                joined_word = None
                
                print(HANGMAN(0))

                play_again = False

                attempts = len(len(HANGMAN)-1)
                 while attempts > 0 and  "-" in words_guessed:
                        print(f'You have {atempts} left')
                        joined_word = "".join(words_guessed)
                        print(joined_word)
                        
                        try:
                                player_guess = str(input("Please select a letter between A - Z:")).lower()
                        except:
                                print("This is invalid input. Try again")
                        else:
                                if not player_guess.isalpha():
                                        print("That is not a letter. Please try again")
                                        continue
                                elif len(player_guess) >1:
                                        print("That is more than 1 letter")
                                        continue
                                elif player_guess in guessed_letters:
                                        print("Already guessed letter")
                                        continue
                                else:
                                        pass
                        guessed_letters.append(player_guess)
                        for letter in range(len(chosen_word)):
                                if player_guess == chosen_word
                                        words_guessed[letter] = player_guess
                        if player_guess not in chosen_word:
                                attempts -= 1
                                print(HANGMAN[len(HANGMAN)-1-attempts])
                if "-" not in words_guessed:
                        print(f"Congratulations! {chosen_word}")
                else:
                        print(f'You died. Word was {chosen_word}')
                print("Play again?")

                response = input(">").lower()
                if response = "Y":
                        
                if response = "X":
                        
                else:
                        

                        
                                        
                                

                
if __name__ == "__main__":
    main()
