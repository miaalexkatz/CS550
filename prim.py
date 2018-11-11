#Mia Katz
#Prim Algorithm Maze Generation
#Sources: Idea for Maze Layout (plus/dash) http://www.delorie.com/game-room/mazes/genmaze.cgi, aka the first result for copy paste maze. Note: the layout has since changed, but still, this website was a major influence


import sys
import random
from mazecell import Cell, Walls

columns = int(sys.argv[1])
rows = int(sys.argv[2])

global ex
ex = [[".X."] * (columns) for x in range(rows*2+1)] #this sets up the board in general
cells = [[Cell() for i in range(columns)]for j in range(rows)] #stores the values for the bottom cell walls
walls = [[Walls() for i in range(columns)] for j in range(rows)] #stores the vertical cell walls
visitedcells = [] #the list of cells that have been selected already
frontiercells = [] #the list of cells on the frontier which can be selected next
realnumber = 1 #sets the start point in the corner. The values will be subtracted from eventually to be 0,0. The complex negates 0 as a real number during wall selections.
imagnumber = 1


visitedcells.append(complex(realnumber, imagnumber))
print(realnumber,imagnumber)
frontiercells.append(complex(realnumber+1, imagnumber))
frontiercells.append(complex(realnumber, imagnumber+1))

while len(visitedcells) <= ((rows+1)*(columns+1)):
	if len(frontiercells) > 0:
		number = random.randint(0, (len(frontiercells)-1)) #this picks the next values from the complex number stored in the frontier 
		print(realnumber,imagnumber, frontiercells)
		realnumber = int(frontiercells[number].real) #these two functions convert the stored complex into values
		imagnumber = int(frontiercells[number].imag)
		frontiercells.remove(complex(realnumber, imagnumber))
		visitedcells.append(complex(realnumber, imagnumber))	
	else: 
		break
	chance0, chance1, chance2, chance3 = False, False, False, False
	itWorked = False
	if realnumber < rows and realnumber != 0 and complex(realnumber+1, imagnumber) not in frontiercells and complex(realnumber+1, imagnumber) not in visitedcells: #the if statements check that the value added to frontier is actually in the usable board
		frontiercells.append(complex(realnumber+1, imagnumber)) #this adds to the frontier list

	if imagnumber != 1 and complex(realnumber, imagnumber-1) not in frontiercells and complex(realnumber, imagnumber-1) not in visitedcells:
		frontiercells.append(complex(realnumber,imagnumber-1))
#	elif imagnumber == 1:
#		frontiercells.append(complex(realnumber, imagnumber+1))

	if realnumber != 1 and complex(realnumber-1, imagnumber) not in frontiercells and complex(realnumber-1, imagnumber) not in visitedcells:
		frontiercells.append(complex(realnumber-1,imagnumber))
#	elif realnumber == 1:
#		frontiercells.append(complex(realnumber+1, imagnumber))

	if imagnumber<columns and imagnumber!=0 and complex(realnumber,imagnumber+1) not in frontiercells and complex(realnumber,imagnumber+1) not in visitedcells:
		frontiercells.append(complex(realnumber,imagnumber+1))
	while itWorked != True:
		if len(visitedcells) != (rows+1)*(columns+1):
			#if realnumber != 0 and imagnumber != 0:
			#if realnumber != 0 and imagnumber != 0 and imagnumber != rows-1 and realnumber != columns-1:
			chance = random.randint(0,3) #whether it will go up, down, left, right
		if (chance0 == True and chance1 == True and chance2 == True and chance3 == True):
			itWorked = True
		elif chance == 0:
			if complex(realnumber+1,imagnumber) in visitedcells: #go down
				cells[realnumber-1][imagnumber-1].downwall = False
				itWorked = True
			chance0 = True
		elif chance == 2:
			if complex(realnumber,imagnumber-1) in visitedcells: #right
				walls[realnumber-1][imagnumber-1].leftwall = False
				itWorked = True
			chance2 = True
		elif chance == 1:
			if complex(realnumber-1,imagnumber) in visitedcells: #go up
				cells[realnumber-2][imagnumber-1].downwall = False
				itWorked = True
			chance1 = True
         #go down
		elif chance == 3: 
			if complex(realnumber,imagnumber+1) in visitedcells: #go left
				walls[realnumber-1][imagnumber].leftwall = False
				itWorked = True
			chance3 = True
for c in range(int(rows/2)):
	walls[c][0].leftwall = True
for d in range(columns):
	cells[rows-1][d].downwall = True
for x in range(rows):
	for y in range(columns):
		cells[x][y].finish()
		walls[x][y].walls()

for x in range(columns):
	ex[0][x] = ".--"
	for y in range(rows):
		ex[(y*2)+1][x] = walls[y][x]
		ex[(y*2)+2][x] = cells[y][x]
for y in range(rows):
	ex[(y*2)+1].insert(columns, "|")
	ex[(y*2)+1][0] = "|  "
for i in range(rows+1):
	ex[(i*2)].insert(columns, ".")
#for a in range(columns):
ex[0][0]="   "
ex[1][0]="   "
ex[rows*2][columns]=".  "
ex[rows*2-1][columns]="   "
for a in range(len(ex)):
	print(*ex[a])

print(len(visitedcells))
print(visitedcells)



#ideas for before I forget:
#the maze board is a list of Cells arranged in an array like Minesweeper
#Each is composed of 4 walls
#A wall value is set to False when the cell next to it randomly selects it. Then the cell will lose the wall adjacent to the cell that selected it
#A cell can only lose two walls, and cannot visit a visited cell. The only exception is cells on the border!
#Cells will apply a wall to the bottom, not the top. If a cell has downwall = True, then the above cell should have upwall == False. The top row of the list will be a border, which is why rows has one added. This is because I can't find an up thing

#randomly select a cell
#append cell to list of cells
#when the len of the used cells list is equivalent to the total area it all prints.

#okay so here's the idea: when a cell is selected, it becomes selectedcell values. From there, it moves to oldcell values, and once oldcell, it receives an identity to be replaced into a maze board. 