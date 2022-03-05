# Roll Dice Simulator
# Mini python project
# Author : Natasha Mulumba
# last modified : 05 March 2022

import random
from random import seed


"""Roll random number from 1 to 6"""
userInput = 'y' # set default value
while userInput == 'y' or userInput == 'Y':
    userInput = input("Roll Dice?[y] 0r [n]:")
    Dice_value = random.randint(1, 6)
    print(Dice_value)
print("End of session")

