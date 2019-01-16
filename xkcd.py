#Mia Katz
#16 January 2019
#Sources: The MatPlotLib online Pyplot resources, Joe Spych of the PA fire departments, and the National Body Mass Index website.
#xkcd project, the question being "If you drew all of the water out of a person's body, how many fires could you extinguish?" I have an actual comic format which I intend to email during class or submit on Canvas. I think it'll be canvas.
#some related statistics
#50-65% water
#one campfire takes about 3 gallons to extinguish: this is about .04L per square centimeter. It's generated to be slightly on the higher side, to ensure that your fire is not risky.
#weight of a person in kg will account for L of water, in a thankfully simple conversion.
import random
import matplotlib.pyplot as plt

def personwater():
	firesputout = 0
	weight = random.randrange(57, 90) #Underweight to overweight kg amounts for a person
	waterper = random.randrange(5000, 6500)/10000 #calculates the body water percentage, whicb is
	waterl = weight*waterper
	firesize = random.randrange(280, 470)
	lneeded = .04*firesize #Generates the fires you'll make during your camping trip, in cm
	firesputout = waterl/lneeded
	firesputout = round(firesputout, 2)
	return firesputout

tr = [] #hosts the number of repetitions of each scenario
gr = []#hosts the actual number of fires made and extinguished
for i in range(10000):
	tr.append(0)
	gr.append(i/100)
for i in range(100000):
	enter = int(personwater()*100)
	tr[enter] +=1
#code related to the graph
plt.plot(gr, tr, color=(.18, .4, .92, 1.0))
plt.xlabel('Number of Fires Extinguished')
plt.ylabel('Repitions')
plt.title('Fires Extinguished Using the L of Water in a Human Body')
plt.show()

