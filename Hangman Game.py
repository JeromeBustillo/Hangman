import random

HANGMAN = (
"""
--------
|      |
|
|
|
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|      
|
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|      |     
|
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|     /|     
|
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|     /|\     
|
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|     /|\     
|     /
|
|
|
|
-----------

""",
"""
--------
|      |
|      O
|     /|\     
|     / \
|
|
|
|
-----------

""")

print (HANGMAN[0])

PlayAgain = True
while PlayAgain:
    wordbox_list = ['sword','shield','helmet','pen','paper','python','shame', 'honey', 'box', 'eye', 'leather', 'pollution', 'side', 'show' ,'cellar', 'partner', 'egg', 'bomb', 'slip', 'steam', 'start', 'cabbage', 'plot', 'oil' ,'notebook', 'sheep']
    chosenword = random.choice(wordbox_list).lower()
    guess = None #player input
    guess_letters = [] #all of player's guesses
    blank_word = [] #replace letters into dashes
    for letter in chosenword:
        blank_word.append("_")
    tries = 6
    
    while tries > 0:
    
        if(tries != 0 and "_" in blank_word):
            print(("\nYou have {} tries remaining.").format(tries))
        
        try:
            guess = str(input("\Please select a letter between A-Z")).lower()
        except:
            print("Your guess is invalid.  Please try again.")
    
        else:
            if not guess.isalpha():
                print("That is not a letter.  Please try again")
                continue
            elif len(guess) > 1:
                print("Please enter one letter.")
                continue
            elif guess in guess_letters:
                print("You have already guessed that letter")
                continue
            else:
                pass
        
            guess_letters.append(guess)
        
            if guess not in chosenword:
                tries -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - tries])
            
            else:
                searchMore = True
                startsearchIndex = 0
                while searchMore:
                    try:
                        foundAtIndex = chosenword.index(guess, startsearchIndex)
                        blank_word[foundAtIndex] = guess
                        startsearchIndex = foundAtIndex + 1
                    except:
                        searchMore = False
                    
                print("".join(blank_word))
        
        if tries == 0:
            print("Game Over! The word was " + chosenword)
            print("\nTry Again?")
            response = input("> ").lower()
            if response not in ("yes", "y"):
                play_again = False
                print("Thank you for playing!")
            break
        if "_" not in blank_word:
            print(("\nCongratulations!  You guessed '{}' right!").format(chosenword))
            print("\nTry Again?")
            response = input("> ").lower()
            if response not in ("yes", "y"):
                play_again = False
                print("Thank you for playing!")
            break
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        