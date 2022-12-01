"""Daimler Garay
Hangman Project
Started: December 1, 2022 15:08"""

import random as rd

words = ['philathrophy', 'sole', 'statistics', 'smile']

def hangman_start():
    allowed_misses = 5
    wrong_guess = 0
    guess_list = []

    word_to_be_guessed = rd.choice(words)
    word_to_be_guessed = word_to_be_guessed.lower()

    correct_guess = '#'*len(word_to_be_guessed)

    while(wrong_guess != allowed_misses):
        letter = input('Guess a letter:' ).lower()
        if letter.isalpha():
            if letter in word_to_be_guessed:
                print(letter, 'is in the word')
                guess_list.append(letter)
                new_char = ''
                for index, char in enumerate(word_to_be_guessed):
                    if char == letter:
                        new_char += letter
                    else:
                        new_char += correct_guess[index]
                correct_guess = new_char
                if correct_guess == word_to_be_guessed:
                    print('You got the word! Good job!')
                    print(f'The word was : {word_to_be_guessed}!')
                    return True
                else:
                    print(f'Letters your dumbass has used so far:\n {guess_list}')

        else:
            print('Enter a letter idiot!')

        if letter not in word_to_be_guessed:
            print(f'{letter} was not in the word idiot LOL!')
            wrong_guess += 1
            print(f'Wrong guesses: {wrong_guess}')
            guess_list.append(letter)
            print(f'Letters your dumbass has used so far: \n {guess_list}')
        
        if wrong_guess == allowed_misses:
            print('You lost the game. As expected of your dumbass.')
            print(f'The word was: {word_to_be_guessed} fucking idiot')
            return False

hangman_start()















    
