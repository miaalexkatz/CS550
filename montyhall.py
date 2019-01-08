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