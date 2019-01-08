import random, sys
trials = 10000
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
headcount = 0
for i in range(trials):
	for j in range(10):
		test = random.randint(0,1)
		if test == 0:
			headcount += 1
	l[headcount] += 1
	headcount = 0

print(l)