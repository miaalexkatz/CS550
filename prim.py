#Mia Katz
#Prim Algorithm Maze Generation
#Sources: Idea for Maze Layout (plus/dash) http://www.delorie.com/game-room/mazes/genmaze.cgi, aka the first result for copy paste maze. Note: the layout has since changed, but still, this website was a major influence


import sys
import random
from mazecell import Cell, Walls

width = int(sys.argv[1])
height = int(sys.argv[2])

global ex
ex = [[".X."] * (width) for x in range(height*2+1)] #this sets up the board in general
#test = [["hi"] * (width) for x in range(height)]
cells = [[Cell() for i in range(width)]for j in range(height)] #the previous line may be unnecessary
walls = [[Walls() for i in range(width)] for j in range(height)]
visitedcells = [] #the list of cells that have been selected already
frontiercells = [] #the list of cells on the frontier which can be selected next
selectedx = 0 #sets the start point in the corner
selectedy = 0
print(selectedx,selectedy)

while len(visitedcells) <= ((height+1)*(width+1)):
	chance0, chance1, chance2, chance3 = False, False, False, False
	itWorked = False
	visitedcells.append(complex(selectedx, selectedy))	
	if selectedx+1 < height and complex(selectedx+1, selectedy) not in frontiercells and complex(selectedx+1, selectedy) not in visitedcells: #the if statements check that the value added to frontier is actually in the usable board
		frontiercells.append(complex(selectedx+1, selectedy)) #this adds to the frontier list

	if selectedy != 0 and complex(selectedx, selectedy-1) not in frontiercells and complex(selectedx, selectedy-1) not in visitedcells:
		frontiercells.append(complex(selectedx,selectedy-1))
	elif selectedy == 0:
		frontiercells.append(complex(selectedx, selectedy+1))

	if selectedx != 0 and complex(selectedx-1, selectedy) not in frontiercells and complex(selectedx-1, selectedy) not in visitedcells:
		frontiercells.append(complex(selectedx-1,selectedy))
	elif selectedx == 0:
		frontiercells.append(complex(selectedx+1, selectedy))

	if selectedy+1 < width and complex(selectedx, selectedy+1) not in frontiercells and complex(selectedx, selectedy+1) not in visitedcells:
		frontiercells.append(complex(selectedx,selectedy+1))
	while itWorked != True:
		if len(visitedcells) != (height+1)*(width+1):
			#if selectedx != 0 and selectedy != 0:
			#if selectedx != 0 and selectedy != 0 and selectedy != height-1 and selectedx != width-1:
			chance = random.randint(0,3) #whether it will go up, down, left, right
		if (chance0 == True and chance1 == True and chance2 == True and chance3 == True):
			itWorked = True
		elif chance == 0:
			if complex(selectedx,selectedy+1) in visitedcells: #go down
				cells[selectedx][selectedy+1].upwall = False
				cells[selectedx][selectedy].downwall = False
				itWorked = True
			chance0 = True
		elif chance == 2:
			if complex(selectedx-1,selectedy) in visitedcells: #right
				walls[selectedx-1][selectedy].rightwall = False
				walls[selectedx][selectedy].leftwall = False
				itWorked = True
			chance2 = True
		elif chance == 1:
			if complex(selectedx,selectedy-1) in visitedcells: #go down
				cells[selectedx][selectedy-1].downwall = False
				cells[selectedx][selectedy].upwall = False
				itWorked = True
			chance1 = True
         #go down
		elif chance == 3: 
			if complex(selectedx+1,selectedy) in visitedcells: #go left
				walls[selectedx+1][selectedy].leftwall = False
				walls[selectedx][selectedy].rightwall = False
				itWorked = True
			chance3 = True
#		print(chance0, chance1, chance2, chance3)
#	for g in range(height):
#		if selectedx == 0:
#			walls[0][g].leftwall = True
	if len(frontiercells) > 0:
		number = random.randint(0, (len(frontiercells)-1)) #this picks the next values from the complex number stored in the frontier 
		print(selectedx,selectedy, frontiercells)
		selectedx = int(frontiercells[number].real) #these two functions convert the stored complex into values
		selectedy = int(frontiercells[number].imag)
		frontiercells.remove(complex(selectedx, selectedy))
	else: 
		break
for c in range(int(height/2)):
	walls[c][0].leftwall = True
for d in range(width):
	cells[height-1][d].downwall = True
#for c in range((height*2)-2):
#	walls[c][width].rightwall = True
#for be in range(width):
#	walls[be][height].downwall = True
for x in range(height):
	for y in range(width):
		cells[x][y].finish()
		walls[x][y].walls()

for x in range(width):
	ex[0][x] = ".--"
	for y in range(height):
		ex[(y*2)+1][x] = walls[y][x]
		ex[(y*2)+2][x] = cells[y][x]
for y in range(height):
	ex[(y*2)+1].insert(width, "|")
	ex[(y*2)+1][0] = "|  "
for i in range(height+1):
	ex[(i*2)].insert(width, ".")
#for a in range(width):
ex[0][0]="   "
ex[1][0]="   "
ex[height*2][width]=".  "
ex[height*2-1][width]="   "
walls[0][0].leftwall = False
for a in range(len(ex)):
	print(*ex[a])

print(len(visitedcells))
print(visitedcells)



#ideas for before I forget:
#the maze board is a list of Cells arranged in an array like Minesweeper
#Each is composed of 4 walls
#A wall value is set to False when the cell next to it randomly selects it. Then the cell will lose the wall adjacent to the cell that selected it
#A cell can only lose two walls, and cannot visit a visited cell. The only exception is cells on the border!
#Cells will apply a wall to the bottom, not the top. If a cell has downwall = True, then the above cell should have upwall == False. The top row of the list will be a border, which is why height has one added. This is because I can't find an up thing

#randomly select a cell
#append cell to list of cells
#when the len of the used cells list is equivalent to the total area it all prints.

#okay so here's the idea: when a cell is selected, it becomes selectedcell values. From there, it moves to oldcell values, and once oldcell, it receives an identity to be replaced into a maze board. 