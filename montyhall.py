#Mia Katz monty hall sim

import random

switch = False
carcount = 0
for i in range(5000):
	car = random.randint(0,2)
	if car == 1:
		door1, door2, door3 = True, False, False
	elif car == 0:
		door2, door3, door1 = True, False, False
	else:
		door3, door2, door1 = True, False, False

	choice = random.randint(1, 3)
	#choice 1 is door 1, 2 is door 2, etc

	if choice == 1:
		if door2 == False and door3 == False:
			op = random.randint(0,1)
			if op == 0 and switch == True:
				choice = 3
			elif op == 1 and switch == True:
				choice = 2
		elif door2 == False and switch == True:
			choice = 3
		elif door3 == False and switch == True:
			choice = 2
	elif choice == 2:
		if door1 == False and door3 == False:
			op = random.randint(0,1)
			if op == 0 and switch == True:
				choice = 3
			elif op == 1 and switch == True:
				choice = 1
		elif door1 == False and switch == True:
			choice = 3
		elif door3 == False and switch == True:
			choice = 1
	elif choice == 3:
		if door2 == False and door1 == False:
			op = random.randint(0,1)
			if op == 0 and switch == True:
				choice = 1
			elif op == 1 and switch == True:
				choice = 2
		elif door2 == False and switch == True:
			choice = 1
		elif door3 == False and switch == True:
			choice = 2

	if choice == 1:
		if door1 == True:
			carcount += 1
	elif choice == 2:
		if door2 == True:
			carcount += 1
	else:
		if door3 == True:
			carcount+= 1

print(carcount)


#In this situation, by switching your choice, your chance of winning the car doubles from 33% to 66%. When I ran 5000 trials, switching restuled in a car about 3200, but keeping my choice halved the won cars. It's a wiser idea to switch because surely, if the available door was not removed, you know that it will serve some value. The chances of each door holding a prize are 33%, so when you first choose you are completely blind. However, there's also only a 33% chance that both of the remaining doors have cars behind them, and a 66% chance that one holds the car. Therefore, it's more likely for you to find the car behind the non-selected door because it's twice as likely that the host had only one penny door to open than two.