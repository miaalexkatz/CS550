import sys
from mazecell import Cell

width = int(sys.argv[1])
height = int(sys.argv[2])

global t
ex = [['X'] * width for x in range(height)+1]
for x in range(width):

for a in range(len(ex)):
	print(*ex[a])
#ideas for before I forget:
#the maze board is a list of Cells arranged in an array like Minesweeper
#Each is composed of 4 walls
#A wall value is set to False when the cell next to it randomly selects it. Then the cell will lose the wall adjacent to the cell that selected it
#A cell can only lose two walls, and cannot visit a visited cell. The only exception is cells on the border!
#Cells will apply a wall to the top, not the bottom. If a cell has upwall = True, then the above cell should have downwall == False. The bottom row of the list will be a border, which is why height has one added