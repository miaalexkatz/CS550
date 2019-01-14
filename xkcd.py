#Ideas for ridiculous question thing
#if you took the L of water in an adult human body, how many camp fires could one person put out?

#50-65% water
#one campfire takes about 3 gallons to extinguish
#weight of a person in kg will account of L of water
import random


def personwater():
	firesputout = 0
	weight = random.randrange(57, 90)
	waterper = random.randrange(5000, 6500)/10000
	waterl = weight*waterper
	firesize = random.randrange(330, 470)
	lneeded = .04*firesize
	while waterl - lneeded >=0:
		waterl -= lneeded
		firesputout += 1
		firesize = random.randrange(330, 470)
		lneeded = .04*firesize
	firesputout += lneeded/waterl
	extra = firesputout%.001
	firesputout = firesputout-extra
	return firesputout


