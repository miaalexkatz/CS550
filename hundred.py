import random
randomNumber = int(random.randrange(1, 10))

def reset():
    randomNumber = int(random.randrange(1, 10))

def main():
    number = int(input("I'm thinking of a number between one and ten... "))
    guess(number)

def guess(number1):
    correct = False
    if number1 == randomNumber:
       print("Yay! let's play again! Cause you got it right ;)")
       reset()
       main()
    else:
    	print("Nope, let's try it again!")
    	main()
main()