'''This code is based on Bagels, by Al Sweigart al@inventwithpython.com
    You must guest the vowes based on clues.
    Thanks to "The Big Book of Small Python Projects, 
    https://inventwithpython.com/bigbookpython/project1.html
    '''

import random

NUM_VOWELS = 3
NUM_GUESSES = 10

def main():
    print('''I am thinking of  {} diferent vowels. 
          Try to guess what it is. Here are some clues:
          When I say:  That means:
            Pico       One vowel is correct but in the wrong position.
            Fermi      One vowel is correct and in the right position.
            Bagels     No vowel is correct.
            
    For example, if the secre vowel was 248 and your guess was 823,
    the clues would be Fermi Pico.'''.format(NUM_VOWELS))
    
    while True: # main loop
        secret_vowels = getSecretVowels()
        print("I thought up a combination of vowels")
        print(' You have {} guesses to get it'.format(NUM_GUESSES))
        
        numGuesses = 1
        while numGuesses <= NUM_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_VOWELS or guess.isnumeric():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                
                
            clues = getClues(guess, secret_vowels)
            print(clues)
            numGuesses += 1
            
            if guess == secret_vowels:
                break # There are correct, so break out of this loop
            if numGuesses > NUM_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_vowels))
                
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')    
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing') 
                    
def getSecretVowels():
    "Returna string made up of NUM_VOWELS unique combination of vowels"
    crazy_vowels = ["a","e","i","o","u"]
    random.shuffle(crazy_vowels)

    secret_vowel = ''
    for i in range(NUM_VOWELS):
        secret_vowel += str(crazy_vowels[i])
        
    return secret_vowel

def getClues(guess, secret_vowel):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret vowel pair"""
    if guess == secret_vowel:
       return "You got it!"
       
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_vowel[i]:
            clues.append("Fermi")
            
        elif guess[i] in secret_vowel:
            clues.append("Pico")
    if len(clues) == 0:
        return 'bagels'
    else: 
        clues.sort()
        
        return ' '.join(clues)
    
    
if __name__ == "__main__":
    main()