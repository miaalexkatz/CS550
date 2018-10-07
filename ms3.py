import random as rd
global width 
global bombcount
global otherbomb
width = int(input("How many columns should the board have? >>")) 
wid = width +2
height = int(input("And how many rows? >>")) 
hei = height +2
bombs = int(input("How many bombs? >>")) 
bombcount = bombs
otherbomb = ((height*width) - bombs)
global t
t = [[0]*wid for x in range(hei)]

for x in range(bombs):
	wi = int(rd.randrange(0, width, 1))
	he = int(rd.randrange(0, height, 1))
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
global ex, xa, yb, xc, yc
ex = [['X'] * width for x in range(height)]
for x in range(len(ex)):
	print(*ex[x])
for x in range(len(t)):
	print(*t[x])


def coord():
	global ex, xa, yb, xc, yc, otherbomb, bombcount
	xc = int(input("Enter ROW NUMBER >> "))
	yc = int(input("Enter COLUMN NUMBER >> "))
	if type(t[xc][yc]) == str:
		r = [['*']*width for x in range(height)]
		print("Game Over! Sorry, you lost...")
		for x in range(len(r)):
			print(*r[x])
	else: 
		print(otherbomb)
		ex[xc][yc] = t[xc-1][yc-1]
		if ex[xc][yc] == 0:
			expand()
		else:
			otherbomb -= 1
		if otherbomb >= 0 or bombcount >= 0:
			for x in range(len(ex)):
				print(*ex[x])
			rep()
		else:
			print("Yay! You won!")
			for x in range(len(t)):
				print(*t[x])

def rep():
	res = input("""
Nice! Would you like to plant a flag? 
Type 1 for Yes, anything else for No!
>> """)
	if res == '1':
		flag()
	else:
		coord()

def flag():
	global bombcount
	ro = int(input("Which ROW? >>"))-1
	co = int(input("Which COLUMN? >>"))-1
	ex[ro][co] = str('!')
	if type(t[ro][co]) == str:
		bombcount -= 1
	for x in range(len(ex)):
		print(*ex[x])
	coord()

def expand(xc, yc):
	global otherbomb
	print("in expand")
	for x in range(-1, 2):
		for y in range(-1, 2):
			ex[xc+x][yc+y] = t[xc+x][yc+y]
			if x != 0 and y != 0:
				otherbomb -= 1
			print(otherbomb)
			if ex[xc+x][yc+y] == 0:
				xc +=x
				yc +=y
				for x in range(-1, 2):
					for y in range(-1, 2):
						ex[xc+x][yc+y] = t[xc+x][yc+y]
						if x != 0 and y != 0:
							otherbomb -= 1
						if t[xc+x][yc+y] == 0:
							expand(xc+x, yc+y)

coord()