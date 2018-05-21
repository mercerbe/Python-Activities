import random

def getWord():
    words = ['safe', 'courage', 'offer', 'remember', 'consider', 'love', 'speak', 'create', 'open',
             'spend', 'reach', 'remain', 'suggest', 'appear', 'develop', 'python', 'agree', 'prepare',
             'indicate', 'wonder', 'arrive', 'mention', 'figure', 'settle']
    return random.choice(words).upper()

def check(word,guesses,guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '_'
        if letter == guess:
            matches += 1
    if matches > 1:
        print 'Correct! The word contains',matches,'"' + guess + '"' + 's'
    elif matches == 1:
        print('Correct! the word contains the letter "' + guesses + '"')
    else:
        print('Incorrect, the word does not contain the letter: "' + guess + '"')
    return status

def main():
    player = input("Let's start an adventure! What is your name? ")
    print "Hello ", player,"!"
    word = getWord()
    guesses = []
    guessed = False
    print('The word contains',len(word),'letters')
    while not guessed:
        text = 'please enter one letter or a {}-letter word '.format(len(word))
        guess = input(text).lower()
        if guess in guesses:
            print('You already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Incorrect')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print('Invalid Guess')

        print 'Correct! the word is',word + '! You got it in', len(guesses), 'tries!'

main()
