import random

def blockwalk(dist):
	xval = 0
	yval = 0
	for i in range(dist):
		dire = random.randint(0,3)
		if dire == 0: #left
			xval += 1
		elif dire == 1:
			yval -= 1
		elif dire ==2:
			xval -= 1
		else:
			yval += 1
	journey = abs(xval) + abs(yval)
	return journey









transit = 0

for i in range(1000):
	if blockwalk(22) > 4:
		transit +=1
print(transit/1000)

