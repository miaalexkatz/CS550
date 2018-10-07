import random as rd
width = int(input("How many columns should the board have? >>")) 
wid = width +2
height = int(input("And how many rows? >>")) 
hei = height +2
bombs = int(input("How many bombs? >>")) 
bombcount = bombs
global otherbomb
othercount = (height*width) - bombs
global t
t = [[0]*wid for x in range(hei)]

for x in range(bombs):
	wi = int(rd.randrange(1, width+1))
	he = int(rd.randrange(1, height+1,))
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
global ex
ex = [['X'] * width for x in range(height)]
for x in range(len(ex)):
	print(*ex[x])
for x in range(len(t)):
	print(*t[x])

def coord():
	global xa, yb, xc, yc, otherbomb
	xa = int(input("Enter ROW NUMBER >> "))
	xc = xa-1
	yb = int(input("Enter COLUMN NUMBER >> "))
	yc = yb-1
	if type(t[xa][yb]) == str:
		r = [['*']*width for x in range(height)]
		print("Game Over! Sorry, you lost...")
		for x in range(len(r)):
			print(*r[x])
	else: 
		ex[xc][yc] = t[xa][yb]
		if ex[xc][yc] == 0:
			expand(xc, yc, xa, yb)
		for x in range(len(ex)):
			print(*ex[x]) 
		flag()

def flag():
	res = input("""
Nice! Would you like to plant a flag? 
Type 1 for Yes, anything else for No!
>> """)
	if res == '1':
		ro = int(input("Which ROW? >>"))-1
		co = int(input("Which COLUMN? >>"))-1
		ex[ro][co] = str('!')
		if t[ro-1][co-1] == '*':
			bombcount -= 1
		if bombcount == 0:
			print("Yay! You won! :)")
		else:
			for x in range(len(ex)):
				print(*ex[x])
	else:
		print("Alright, let's keep going!")
		coord()

def expand(xi, yi, xh, yh):
	global otherbomb, xc, yc, xa, yb
	print("in expand")
	for x in range(-1, 2):
		for y in range(-1, 2):
			ex[xi+x][yi+y] = t[xh+x][yh+y]
	for x in range(-1, 2):
		for y in range(-1, 2):
			if ex[xi+x][yi+y] == 0:
				if xi+x < (len(t[x])) and xi+x > 0:
					if yi+y < (len(t)) and yi+y > 0:
						expand(xi+x, yi+y, xh+x, yh+y)

coord()