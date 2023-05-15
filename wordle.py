'''
Wordle Simulator
Samantha Cook
5/15/2023
'''

import random
import colorama
import os


def play_game():
    '''
    Plays the game based on how many guesses the player has.
    '''
    
    guess = '' 
    word = select_word()

    attempts = 6 
    while attempts > 0 and guess != word:
        guess = input('Enter a guess >> ' ).lower()
        if check_word(guess, word):
            report_correctness(guess, word)
            attempts -= 1
        else:
            print('That is an invaild word. Enter a different word.')
    if guess != word:
        print('Out of guesses. That answer was', word)


def select_word():
    '''
    Selects the word from a file of words.
    '''
    
    file = open('wordle_words.txt', 'r')
    words = file.readlines()
    file.close()
    index = random.randint(0, len(words)-1)
    return words[index].strip()

def check_word(guess, word):
    '''
    Checks if word is vaild.
    '''
    
    if len(guess) != 5:
        return False
    file = open('wordle_words.txt', 'r')
    words = []
    for word in file:
        words.append(word.strip())
    file.close()
    if guess in words:
        return True
    return False
            
def report_correctness(guess, word):
    '''
    Checks if the word guess is correct.
    '''
    
    for i in range(0, len(guess)):
        if guess[i] == word[i]:
            print(colorama.Back.GREEN + guess[i], end='')
        elif guess[i] in word:
            print(colorama.Back.YELLOW + guess[i], end='')
        else:
            print(colorama.Back.LIGHTBLACK_EX + guess[i], end='')
    print(colorama.Back.RESET + '\n')


#main
print('Welcome to Wordle Simulator!')
repeat = 'y'
while repeat == 'y':
    play_game()
    repeat = input('Would you like to play again? (y/n) >> ')
