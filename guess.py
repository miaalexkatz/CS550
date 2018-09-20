import random
randomNumber = random.randrange(0,10)
guess = False

def start():
    user = int(input("I'm thinking of a number between one and ten...: "))
def check():
    if user==randomNumber:
        guess = True
        print("Yay! You've won! That's pretty cool")
    elif user>10 or user<1:
        print("I literally just told you it's between one and ten...")
    else:
    	print("Eh, try again")

while guess ==False:
    start()
    check()