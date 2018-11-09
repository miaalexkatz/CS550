#Mia Katz
#Prim Algorithm Maze Generation
#Sources: Idea for Maze Layout (plus/dash) http://www.delorie.com/game-room/mazes/genmaze.cgi, aka the first result for copy paste maze.


import sys
import random
from mazecell import Cell

width = int(sys.argv[1])
height = int(sys.argv[2])

global ex
ex = [[".X."] * (width) for x in range(height*2)] #this sets up the board in general
cells = [[Cell() for i in range(width)]for j in range(height)] #the previous line may be unnecessary
visitedcells = [] #the list of cells that have been selected already
frontiercells = [] #the list of cells on the frontier which can be selected next
for x in range(height):
	ex[x][0] = "|" #left border
for x in range(width): #top border
	ex[0][x] = '____'
#ex[0][width+1] = '_'
for a in range(len(ex)):
	print(*ex[a])
selectedy = random.randrange(0, width+1, 1) #the values of the first selected cells
selectedx = random.randrange(1, height+1, 1)
print(selectedx,selectedy)
while len(visitedcells) <= height+1*width+1:
	if (complex(selectedx, selectedy)) not in visitedcells:
		visitedcells.append(complex(selectedx, selectedy))	

	if selectedx+1 < height and complex(selectedx+1, selectedy) not in frontiercells and complex(selectedx+1, selectedy) not in visitedcells: #the if statements check that the value added to frontier is actually in the usable board
		frontiercells.append(complex(selectedx+1, selectedy)) #this adds to the frontier list

	if selectedy-1 > 0 and complex(selectedx, selectedy-1) not in frontiercells and complex(selectedx, selectedy-1) not in visitedcells:
		frontiercells.append(complex(selectedx,selectedy-1))

	if selectedx-1 >= 0 and complex(selectedx-1, selectedy) not in frontiercells and complex(selectedx-1, selectedy) not in visitedcells:
		frontiercells.append(complex(selectedx-1,selectedy))

	if selectedy+1 < width and complex(selectedx, selectedy+1) not in frontiercells and complex(selectedx, selectedy+1) not in visitedcells:
		frontiercells.append(complex(selectedx,selectedy+1))

	chance = random.randint(0,3) #whether it will go up, down, left, right
	if chance == 0:
		if complex(selectedx,selectedy+1) in frontiercells: #go up
			cells[selectedx][selectedy+1].downwall = False
			cells[selectedx][selectedy].upwall = False
	elif chance == 1:
		if complex(selectedx+1,selectedy) in frontiercells: #right
			cells[selectedx+1][selectedy].leftwall = False
			cells[selectedx][selectedy].rightwall = False
	elif chance == 2:
		if complex(selectedx,selectedy-1) in frontiercells: #go down
			cells[selectedx][selectedy-1].upwall = False
			cells[selectedx][selectedy].downwall = False
         #go down
	elif chance == 3:
		if complex(selectedx-1,selectedy) in frontiercells: #go left
			cells[selectedx-1][selectedy].rightwall = False
			cells[selectedx][selectedy].leftwall = False
	if len(frontiercells) > 0:
		number = random.randint(0, (len(frontiercells)-1)) #this picks the next values from the complex number stored in the frontier 
		print(selectedx,selectedy, frontiercells)
		selectedx = int(frontiercells[number].real) #these two functions convert the stored complex into values
		selectedy = int(frontiercells[number].imag)
		frontiercells.remove(complex(selectedx, selectedy))
	else: 
		break

for a in range(height):
	cells[a][0].leftwall = True
	for be in range(width):
		cells[a][be].finish() 
		ex[a+2][be] = cells[a][be]
		cells[a][be].walls()
		ex[a*2][be] = cells[a][be]
for a in range(len(ex)):
	print(*ex[a])
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