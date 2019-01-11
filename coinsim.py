import random, sys
import  matplotlib.pyplot as plt
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
plt.bar([0,1,2,3,4,5,6,7,8,9,10], l, color=(.98, .8, .02, 1.0))
plt.show()
