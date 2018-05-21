print("Hello World!")

#Dice Roller
import random

def roll(sides = 6):
    numberRolled = random.randint(1, sides)
    return numberRolled

def main():
    sides = 6
    rolling = True
    while rolling:
        rollAgain = input("Let's get rolling! R=Roll, Q=Quit. ")
        if rollAgain.lower() != "q":
            numberRolled = roll(sides)
            print("You Rolled A " + str(numberRolled))
        else:
            rolling = False
            print("Thanks for Playing! ")

main()
