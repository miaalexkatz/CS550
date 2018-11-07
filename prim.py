import sys
import random
from mazecell import Cell

width = int(sys.argv[1])
height = int(sys.argv[2])

global ex
ex = [['__|'] * (width+1) for x in range(height+1)]
visitedcells = []
frontiercells = []
for x in range(height+1):
	ex[x][0] = "|"
for x in range(width):
	ex[0][x] = '____'
#ex[0][width+1] = '_'
for a in range(len(ex)):
	print(*ex[a])
selectedy = random.randrange(1, width)
selectedx = random.randrange(1, height)
print(selectedx)
print(selectedy)
oldx = selectedx
oldy = selectedy
oldcell = Cell()
for x in range(width*height):
	visitedcells.append(complex(oldx, oldy))
	#if selectedx+1 != height+1 and selectedy+1 != height+1:
	frontiercells.append(complex(selectedx+1, selectedy+1))
	#if selectedx+1 != height+1 and selectedy-1 != 0:
	frontiercells.append(complex(selectedx+1,selectedy-1))
	#if selectedx-1 != 0 and selectedy +1 != height+1:
	frontiercells.append(complex(selectedx-1,selectedy+1))
	#if selectedx-1 != 0 and selectedy-1 != 0:
	frontiercells.append(complex(selectedx-1,selectedy-1))
	oldy = selectedx
	oldy = selectedy
	numero = random.randint(0, int(len(frontiercells)))
	chance = random.randint(0,3)
	newcell = Cell()
	if chance == 0:
		if complex(selectedx,selectedy+1) in frontiercells: #go up
			newcell.downwall = False
			oldcell.upwall = False
			selectedy = selectedy+1
	elif chance == 1:
		if complex(selectedx+1,selectedy) in frontiercells: #right
			#selectedx += 1
			newcell.leftwall = False
			oldcell.rightwall = False
			selectedx = selectedx+1
			#go right
	elif chance == 2:
		if complex(selectedx,selectedy-1) in frontiercells: #go down
			newcell.upwall = False
			oldcell.downwall = False
			selectedy = selectedy-1
         #go down
	elif chance == 3:
		if complex(selectedx-1,selectedy) in frontiercells: #go left
			newcell.rightwall = False
			oldcell.leftwall = False
			selected = selectedx-1
	print(selectedx,selectedy)

	aaa = oldcell.finish()
	ex[oldx][oldy] = aaa
for a in range(len(ex)):
	print(*ex[a])
	print(aaa)




#ideas for before I forget:
#the maze board is a list of Cells arranged in an array like Minesweeper
#Each is composed of 4 walls
#A wall value is set to False when the cell next to it randomly selects it. Then the cell will lose the wall adjacent to the cell that selected it
#A cell can only lose two walls, and cannot visit a visited cell. The only exception is cells on the border!
#Cells will apply a wall to the bottom, not the top. If a cell has downwall = True, then the above cell should have upwall == False. The top row of the list will be a border, which is why height has one added. This is because I can't find an up thing

#randomly select a cell
#append cell to list of cells
#when the len of the used cells list is equivalent to the total area it all prints.


#chance = random.randint(3)
#if chance < 1:
#	print("hi")
		#go up
		#ex[xsel][ysel] 
	#elif 1< chance





#okay so here's the idea: when a cell is selected, it becomes selectedcell values. From there, it moves to oldcell values, and once oldcell, it receives an identity to be replaced into a maze board. 