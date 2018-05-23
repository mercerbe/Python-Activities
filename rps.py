import sys
import random
import string

player = input("What's your name?")
string.letters
'rps'
computer = random.choice(string.letters)
comp_answer = computer
player_answer = input("%s, choose r, p or s..." % player)
wins = 0
losses = 0
ties = 0

def compare(user,comp):
    if user == comp:
        return("TIE")
    elif user == "r":
        if comp == "s":
            return("WIN!")
            wins +=1
        else:
            return("LOSS...")
            losses +=1
    elif user == "s":
        if comp == "p":
            return("WIN!")
            wins +=1
        else:
            return("LOSS...")
            losses +=1
    elif user == "p":
        if comp == "r":
            return("WIN!")
            wins +=1
        else:
            return("LOSS...")
            losses +=1
    else:
        return("Please enter r, p or s.")
        sys.exit()
print(compare(player_answer, comp_answer))
