#Mia Katz
#Minesweeper Board Homework
import random as rd
global width 
width = int(input("How many columns should the board have? >>")) 
wid = width +2
height = int(input("And how many rows? >>")) 
hei = height +2
bombs = int(input("How many bombs? >>")) 

t = [[0]*wid for x in range(hei)]

for x in range(bombs):
	wi = int(rd.randrange(1, width-1, 1))
	he = int(rd.randrange(1, height-1, 1))
	wim =  int(wi -1) 
	wip = int(wi + 1)
	hem = int(he-1)
	hep = int(he+1)
	if type(t[wip][he]) != str:
		t[wip][he] += 1
	if type(t[wim][he]) != str:
		t[wim][he] += 1
	if type(t[wi][hep]) != str:
		t[wi][hep] += 1
	if type(t[wi][hem]) != str:
		t[wi][hem] += 1
	if type(t[wim][hem]) != str:
		t[wim][hem] += 1
	if type(t[wim][hep]) != str:
		t[wim][hep] += 1
	if type(t[wip][hem]) != str:
		t[wip][hem] += 1
	if type(t[wip][hep]) != str:
		t[wip][hep] += 1
	t[wi][he]= str('*')
#for x in range(0, height):
#	t[x].pop(0)
#	print(*t[x])

ex = ['X' * width for x in range(height)]
print(ex)

def coord():
	xc = int(input("Enter x coordinate>> "))
	yc = int(input("Enter y coordinate>> "))
	if type(t[xc][yc]) == str:
		r = ['*'*width for x in range(height)]
		print("Game Over! Sorry, you lost...")
		print(r)
	else:
		ex[xc][yc] = t[xc][yc]
		print(ex) 
		repeat()

def repeat():
	print("Alright, let's try again!")
	coord()

coord()