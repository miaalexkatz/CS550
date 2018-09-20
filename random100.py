import random

def reset():
    win =(random.randrange(0, 10, 1))
    guess = input("I'm thinking of a number between one and ten! Guess it, fool! ")
    check()
    guess = str(guess)


def check():
	if guess == win:
	    print("Wow, you did it! Let's play again!")
	    reset()
	else:
		newguess = input("Nope, guess again! ")
		newguess = guess

reset()