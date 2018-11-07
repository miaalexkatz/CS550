import sys
import random
from mazecell import Cell

width = int(sys.argv[1])
height = int(sys.argv[2])

global ex
ex = [['.X.'] * (width+1) for x in range(height+1)] #this sets up the board in general, the .X. is a placeholder
cells = [[Cell() for i in range(width)]for j in range(height)] #the previous line may be unnecessary
visitedcells = [] #the list of cells that have been selected already
frontiercells = [] #the list of cells on the frontier which can be selected next
for x in range(height+1):
	ex[x][0] = "|" #left border
for x in range(width): #top border
	ex[0][x] = '____'
#ex[0][width+1] = '_'
for a in range(len(ex)):
	print(*ex[a])
selectedy = random.randrange(1, width, 1) #the values of the first selected cells
selectedx = random.randrange(1, height, 1)
selectedy = random.randrange(1, width, 1) #the values of the first selected cells
selectedx = random.randrange(1, height, 1)
while len(visitedcells) <= height*width:
#	if complex(selectedx, selectedy) in visitedcells or complex(selectedx, selectedy) not in frontiercells:
#		selectedy = random.randrange(1, width, 1) #the values of the first selected cells
#		selectedx = random.randrange(1, height, 1)
#	else: 
	visitedcells.append(complex(selectedx, selectedy))	
	if selectedx+1 != height+1 and selectedy+1 != height+1: #the if statements check that the value added to frontier is actually in the usable board
		frontiercells.append(complex(selectedx+1, selectedy+1)) #this adds to the frontier list
	if selectedx+1 != height+1 and selectedy-1 != 0:
		frontiercells.append(complex(selectedx+1,selectedy-1))
	if selectedx-1 != 0 and selectedy +1 != height+1:
		frontiercells.append(complex(selectedx-1,selectedy+1))
	if selectedx-1 != 0 and selectedy-1 != 0:
		frontiercells.append(complex(selectedx-1,selectedy-1))
	chance = random.randint(0,3) #whether it will go up, down, left, right
	if chance == 0:
		if complex(selectedx,selectedy+1) in frontiercells: #go up
			if selectedy+1 <height:
				cells[selectedx][selectedy+1].downwall = False
				cells[selectedx][selectedy].upwall = False
	elif chance == 1:
		if complex(selectedx+1,selectedy) in frontiercells: #right
			if selectedx+1 <height:
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
	number = random.randint(0, len(frontiercells)-1) #this picks the next values from the complex number stored in the frontier 
	selectedx = frontiercells[number].real
	selectedy = frontiercells[number].imag
	frontiercells.pop(number)

	print(selectedx,selectedy)
for a in range(height):
	for be in range(width):
		cells[a][be].finish() 
		ex[a][be] = str(cells[a][be].identity())
for a in range(len(ex)):
	print(*ex[a])
#The problem right now: it checks everything randomly before it can continue and mia no



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