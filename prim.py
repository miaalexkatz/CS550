import sys
import random
from mazecell import Cell

width = int(sys.argv[1])
height = int(sys.argv[2])

global ex
ex = [['__|'] * (width+1) for x in range(height+1)]
usedcells = []
frontier = []
for x in range(height+1):
	ex[x][0] = "|"
for x in range(width):
	ex[0][x] = '____'
#ex[0][width+1] = '_'
for a in range(len(ex)):
	print(*ex[a])
selectedx = random.randrange(1, width)
selectedy = random.randrange(1, height)
while len(usedcells)<=width*height:
	usedcells.append(ex[selectedx][selectedy])
	if selectedx+1 != height+1 and selectedy+1 != height+1:
		frontiercells.append(ex[selectedx+1][selectedy+1])
	if selectedx+1 != height+1 and selectedy-1 != 0:
		frontiercells.append(ex[selectedx+1][selectedy-1])
	if selectedx-1 != 0 and selectedy +1 != height+1:
		frontiercells.append(ex[selectedx-1][selectedy+1])
	if selectedx-1 != 0 and selectedy != 0:
		frontiercells.append(ex[selectedx-1][selectedy-1])
	numero = random.randint(len(frontiercells))




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