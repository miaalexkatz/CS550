#Mia Katz
#Minesweeper Board Homework
import random as rd
width = int(input("How many columns should the board have? >>"))
height = int(input("And how many rows? >>"))
bombs = int(input("How many bombs? >>"))

t = [[0]*width for x in range(height)]

for x in range(bombs):
	wi = int(rd.randrange(0, width-1, 1))
	he = int(rd.randrange(0, height-1, 1))
	wim =  int(wi -1) 
	wip = int(wi + 1)
	hem = int(he-1)
	hep = int(he+1)
	t[wip][he] += 1
	t[wim][he] += 1
	t[wi][hep] += 1
	t[wi][hem] += 1
	t[wim][hem] += 1
	t[wim][hep] += 1
	t[wip][hem] += 1
	t[wip][hep] += 1
	t[wi][he]= str('*')
print(t)
