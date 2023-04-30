'''
Wordle Simulator
Samantha Cook
4/28/2023
'''

import random, colorama, Back, init


def play_round():
    pass

colorama.init()

def select_word():
    choice_list = []
    file = open('wordle_words.txt', )
    choice_list = file.readlines()
    choice = random.choice(choice_list)
    return choice


def check_word():
    choice = select_word()
    attempt = 6
    while attempt > 0:
        guess = str(input("Enter your guess: "))
        if guess[0] == choice[0]:
            print(choice[0])
            break
        elif guess[1] == choice[1]:
            print(choice[1])
        else: 
            attempt -= 1
def check_letter():
    pass



check_word()
