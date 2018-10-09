#Mia Katz
#10.9.18
#Minesweeper Game
#To play the game, enter the desired row length, column length, and bombs. You can win by eliminating everything that isn't a bomb, or by planting enough flags. However, for each flag you place, you MUST clear a square!
#Sources: https://bytes.com/topic/python/, used for help with making a list global
#https://stackoverflow.com/questions/37904343/how-to-delete-a-row-in-2d-list-for-some-specific-column-values, I didn't end up referencing the information I received from this source, but I still used it. Therefore, I will cite it. This was replaced with the gameboard ex from very early on.
#Also, thanks to Mrs. Healey for helping with my recursion problems
#On my honor, I've neither given nor received unauthorized aid __Mia_Katz___

import random as rd
def restart(): #recalling this function lets you start over
	global width, wid, height, hei, bombs, bombcount
	width = int(input("How many columns should the board have? >>")) 
	wid = width +2
	height = int(input("And how many rows? >>")) 
	hei = height +2
	bombs = int(input("How many bombs? >>")) 
	bombcount = bombs #number of unflagged bombs
	global otherbomb #covered squares which ARE NOT bombs
	otherbomb = (height*width) - bombs #the number of squares which don't have a bomb on them
	global t
	t = [[0]*wid for x in range(hei)]
#This is all of the board setup, including calculations for the board. It's stored in another 2d array
	for x in range(bombs):
		he = int(rd.randrange(1, width+1))
		wi = int(rd.randrange(1, height+1,))
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
	global ex #This is the display board
	ex = [['X'] * width for x in range(height)]
	printex()
#	for x in range(len(t)):    this printed the solution during debugging
#		print(*t[x])
	coord()
# This collects the desired input from the user to eliminate an X and replace it with a value from the t board
def coord(): #this is where the game actually starts and lets you pick values
	global xa, yb, xc, yc, otherbomb, width, height
	xcount = height*width
	xa = int(input("Enter ROW NUMBER >> "))
	xc = xa-1
	yb = int(input("Enter COLUMN NUMBER >> "))
	yc = yb-1
	if type(t[xa][yb]) == str and ex[xc][yc] != '!': #If you land on a mine, the game is over. If that mine is covered by a flag, 
		r = [['*']*width for x in range(height)] #prints field of mines
		print("Game Over! Sorry, you lost...")
		for x in range(len(r)):
			print(*r[x])
		end = input("If you want to play again, press 1!")
		if end == '1':
			restart()
	elif otherbomb <= 0:
		print("Yay! You won! :)")
		for x in range(width):
			for y in range(height):
				ex[x][y] = t[x+1][y+1]
		printex()
		end = input("If you want to play again, press 1!")
		if end == '1':
			restart()
	else: 
		#if t[xa][yb] == 0: #if you land on a zero, the board expands
			#expand(xc, yc)
		if ex[xc][yc] == "X":
			ex[xc][yc] = t[xa][yb]
			otherbomb -= 1
		if ex[xc][yc] == 0:
			expand(xc, yc)
		printex()
#		print(otherbomb)
		flag()

def flag():  #fuction to place flags
	global bombcount, otherbomb
	if otherbomb == 0:
		print("Congratulations! You've won the game!")
		for x in range(width):
			for y in range(height):
				ex[x][y] = t[x+1][y+1] #makes the playboard the solution
		printex()
		end = input("If you want to play again, press 1!")
		if end == '1':
			restart()
	else:
		res = input(""". 
Nice! Would you like to plant a flag? 
Type 1 for Yes, anything else for No!
>> """)
		if res == '1': #if you want to plant a flag, you will enter the coordinates 
			ro = int(input("Which ROW? >>"))-1
			co = int(input("Which COLUMN? >>"))-1
			ex[ro][co] = str('!')
			if t[ro+1][co+1] == '*': 
				if t[ro+1][co+1] != '!':#if y
					bombcount -= 1 #this prevents you from cheating by reselecting the square
			if bombcount == 0:
				print("Yay! You won! :)")
				for x in range(width):
					for y in range(height):
						ex[x][y] = t[x+1][y+1]
				printex()
				end = input("If you want to play again, press 1!")
				if end == '1':
					restart()
			else:
				print("Bombs left:",bombs)
				printex()
				print("Nice work, let's keep going!")
				coord()
		else:
			print("Bombs Left:",bombs)
			printex()
			print("Alright, let's keep going!")
			coord()

def expand(xi, yi): #The dreaded expansion recursion function
	global otherbomb
	for x in range(-1, 2):
		for y in range(-1, 2):
			if xi+x >= 0 and yi+y >= 0:
				if xi+x <= height-1 and yi+y <= width-1:
					if ex[xi+x][yi+y] != 0:
						if ex[xi+x][yi+y] == "X":
							otherbomb -= 1
							ex[xi+x][yi+y] = t[(xi+x)+1][(yi+y)+1]
							if ex[xi+x][yi+y] == 0:
								expand((xi+x),(yi+y))

def printex(): #this just prints ex so I don't have to worry about the for loop
		for a in range(len(ex)):
			print(*ex[a])
restart()