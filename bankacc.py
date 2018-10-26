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
		info += "\nAccount Number: "+self.acc
		info += "\nBalance: "+self.bal
		return info


start = input("Would you like to open an account? (Y/N)")
if start == 'Y' or start == 'y':
	name = input("Alright. Please enter your name: ")
	bal = int(input("What is your initial deposit?: "))
	if bal < 100:
		bal = int(input("Sorry, that's not enough. Please make a larger initial deposit: "))
	pin = int(input("Please enter a four digit PIN: "))
	if pin/1000 < 1 or pin/1000 > 9.999:
		pin = int(input("Sorry, that's an invalid PIN. Please try again: "))
	acc = rd.randrange(999999999)
	youraccount = Bank(name, bal, pin, acc)

else:
	print("Okay. Goodbye")


def startscreen():
	print("Hello! Welcome to the bank!")
	de = input("Will you Deposit or Withdraw?")
	if de == 'Withdraw':
		pin()
		minus == int(input("How much would you like to withdraw? :"))
		if minus < self.bal:
			self.bal -= minus
			print(youraccount.stats())





def pin():
	hi = int(input("Please enter your PIN: "))
	if hi == pin:
		print("Correct!")
	else:
		hi == int(input("That was incorrect. Try again: "))
		
