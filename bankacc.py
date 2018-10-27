#Opening a bank account 
#
import random as rd
class Bank:

	def __init__(self, name, bal, pin, acc):
		self.name = name
		self.bal = bal
		self.pin = pin
		self.acc = acc

	def stats(self):
		info = "\nName: "+self.name
		info += "\nAccount Number: "+str(self.acc)
		info += "\nBalance: "+str(self.bal)
		return info


def startscreen():
	print("Hello! Welcome to the bank!")
	hi = input("Please enter your PIN: ")
	if hi == youraccount.pin:
		print("Correct! Welcome, "+youraccount.name)
	else:
		hi == input("That was incorrect. Try again: ")
		return hi
	de = input("Will you Deposit or Withdraw?")
	if de == 'Withdraw':
		minus = int(input("How much would you like to withdraw? :"))
		if minus < youraccount.bal:
			youraccount.bal -= minus
			print(youraccount.stats())
		else: 
			print("Sorry. Your withdrawl amount cannot exceed your balance")
	elif de == 'Deposit':
		depo = int(input("How much would you like to deposit?: "))
		youraccount.bal += depo
		print(youraccount.stats())

		
start = input("Would you like to open an account?: ")
if start == 'Y' or start == 'y' or start == 'yes' or start == 'Yes':
	name = input("Welcome. Please enter your name: ")
	bal = int(input("What is your initial deposit?: "))
	while bal < 100:
		bal = int(input("Sorry, that's not enough. Please make a larger initial deposit: "))
	pin = input("Please select an Account Passcode: ")
#	while pin/1000 < 1 or pin/1000 > 9.999:
#		pin = int(input("Sorry, that's an invalid PIN. Please try again: "))
	acc = rd.randrange(999999999)
	youraccount = Bank(name, bal, pin, acc)
	startscreen()

else:
	print("Okay. Goodbye")