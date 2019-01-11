#Mia Katz
#A 22 block walk yielded the most results the at the closest value to 50% transit requirements!

#the Monte Carlo simulation, aka the probability simulation aims to improve on how businesses handle large uncertainty. The simulation removes the need for a single average number when dealing with derivatives. It replaces this average with many carried out "scenarios," thus granting the business a better idea of outcome likelihood. According to Investopedia, the simulation is named for a popular gambling site, and the simulation is employed in gambling rates and slot machines. Additionally, the Monte Carlo simulation is often used in determining costs for projects, as well as detecting potential budget-breaking tendencies. Something important to note is that all outcomes of a Monte Carlo simulation form a bell curve when accounting for all possible outcomes.

import random, math
def darts(trials):
	circle = 0
	for i in range(trials):
		y = float(random.randrange(-1000, 1000))/1000
		x = float(random.randrange(-1000, 1000))/1000
		if math.sqrt(x**2 + y**2) < 1:
			circle += 1
#	final = circle*4/trials
	return (circle*4)/trials
print(darts(100))
print(darts(1000))
print(darts(10000))


#The more trials you do, the closer the return from the function get to Pi!
