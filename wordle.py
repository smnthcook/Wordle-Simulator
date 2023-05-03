'''
Wordle Simulator
Samantha Cook
4/28/2023
'''

import random
import colorama
import os
from colorama import Fore, Back


def play_game():
    guess = '' 
    word = select_word()
    attempts = 6 
    while attempts > 0 and guess != word:
        guess = input('Enter a guess >> ' ).lower()
        if check_word(guess, word):
            attempts(guess,word)
            attempts -= 1
        else:
            print('That is an invaild word. Enter a different word. >> ')
            if guess != word:
                print('Out of guesses. That answer was', word.strip())


def select_word():
    word_list = []
    file = open('wordle_words.txt', )
    word_list = file.readlines()
    word = random.choice(word_list)
    print(word.strip())
    return word, file


def check_word(guess, word):
    if len(guess) != 5:
        return False
    file = open('wordle_words.txt', 'r')
    for word in file:
        word.append(word.strip())
    file.close
    if guess in word:
        return True
    return False 
            
def check_letter():
    choice = select_word()
    attempt = 6
    while attempt > 0:
        print()
        guess = str(input("Enter your guess: "))
        
        for i in range(len(choice) - 1):
            print(Back.GREEN + choice[i], end='' + Back.RESET)
        attempt = attempt - 1


#main
print('Welcome to Wordle Simulator!')
repeat = 'y'
while repeat == 'y':
    play_game()
    repeat = input('Would you like to play again? (y/n) >> ')
