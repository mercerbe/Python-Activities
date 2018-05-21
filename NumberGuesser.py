import random

def validGuess(x):
    if x.isdigit() and 1 <= int(x) <= 100:
        return True
    else:
        return False

def main():
    number = random.randint(1, 100)
    numberGuessed = False
    guess = input("Guess a number between 1 and 100: ")
    numberOfGuesses = 0
    while not numberGuessed:
        if not validGuess(guess):
            guess = input("Not a valid guess. Guess a number between 1 and 100")
            continue
        else:
            numberOfGuesses +=1
            guess = int(guess)

        if guess < number:
            guess = input("Too Low. Guess Again: ")
        elif guess > number:
            guess = input("Too High. Guess Again: ")
        else:
            print "You got it in ",numberOfGuesses,"guesses!"
            numberGuessed = True
            print("Thanks For Playing! ")

main()
