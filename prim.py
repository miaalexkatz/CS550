#Mia Katz
#12 November 2018
#Prim Algorithm Maze Generation
#Algorthim Explanations in Comments
#Sources: Idea for Maze Layout (plus/dash) http://www.delorie.com/game-room/mazes/genmaze.cgi, aka the first result for copy paste maze. Note: the layout has since changed, but still, this website was a major influence. https://cutekaomoji.com/misc/sparkles/ for the maze styles. Credits to http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm. IMPORTANT NOTE: Said source does contain implemented code, which I avoided (and also isn't Python anyways). I used the step-by-step algorithm gifs in the middle of the page, and the G/V explanation at the top.

import sys
import random
from mazecell import Cell, Walls

columns = int(sys.argv[1])              #The user enters the width and height in the command line
rows = int(sys.argv[2])

aesthetic = input("""
Please select a Maze Style by typing the corresponding number:

1) Standard
2) Geometric
3) Musical
4) Starry
>>	""")
while aesthetic != "1" and aesthetic != "2" and aesthetic != "3" and aesthetic != "4":          #error checking for aesthetic selection
	aesthetic = input("Please enter a valid number >> ")
aesthetic = int(aesthetic)


global ex
ex = [[".X."] * (columns) for x in range(rows*2+1)] #game board
cells = [[Cell(aesthetic) for i in range(columns)]for j in range(rows)] #stores the values for the bottom cell walls
walls = [[Walls() for i in range(columns)] for j in range(rows)] #stores the vertical cell walls
visitedcells = [] #the list of cells that have been selected and used already
frontiercells = [] #the list of cells on the frontier which can be selected next
realnumber = 1 #sets the start point in the corner. The values will be subtracted from eventually to be 0,0. The complex negates 0 as a real number during wall selections, so 1,1 is the top corner in the complex() sense.
imagnumber = 1 #also sets the point in the corner


visitedcells.append(complex(realnumber, imagnumber))       #The while loop begins by choosing a frontiercell, so this provides the function with a starting set as the starting point isn't random.
frontiercells.append(complex(realnumber+1, imagnumber))
frontiercells.append(complex(realnumber, imagnumber+1))

while len(visitedcells) <= ((rows+1)*(columns+1)):
	if len(frontiercells) > 0:       #if there are still cells in the frontier which haven't been selected
		number = random.randint(0, (len(frontiercells)-1)) #this picks the next values from the complex number stored in the frontier 
		realnumber = int(frontiercells[number].real) #these two functions convert the stored complex into values
		imagnumber = int(frontiercells[number].imag)
		frontiercells.remove(complex(realnumber, imagnumber)) #removes the frontier cell and adds it to the visited list 
		visitedcells.append(complex(realnumber, imagnumber))	
	else: 
		break
	chance0, chance1, chance2, chance3 = False, False, False, False
	itWorked = False #it worked is set to true when a frontiercell latches onto the visited list, or in emergency cases if it is unable to do so.
	if realnumber < rows and realnumber != 0 and complex(realnumber+1, imagnumber) not in frontiercells and complex(realnumber+1, imagnumber) not in visitedcells:  #For each of the checks here, the first numerical comparison checks that a frontiercell outside of the board will not be added. The next two checks make sure a frontier isn't duplicated, and ensures that a used cell is not re-added to the frontier list.
		frontiercells.append(complex(realnumber+1, imagnumber)) #If all three are true, the cell is added to the frontier list.

	if imagnumber != 1 and complex(realnumber, imagnumber-1) not in frontiercells and complex(realnumber, imagnumber-1) not in visitedcells:
		frontiercells.append(complex(realnumber,imagnumber-1))

	if realnumber != 1 and complex(realnumber-1, imagnumber) not in frontiercells and complex(realnumber-1, imagnumber) not in visitedcells:
		frontiercells.append(complex(realnumber-1,imagnumber))

	if imagnumber<columns and imagnumber!=0 and complex(realnumber,imagnumber+1) not in frontiercells and complex(realnumber,imagnumber+1) not in visitedcells:
		frontiercells.append(complex(realnumber,imagnumber+1))
	
	while itWorked != True: #itWorked becomes true when a frontier cell finds a visited cell to connect with
		if len(visitedcells) != (rows+1)*(columns+1):
			chance = random.randint(0,3) #whether it will go up, down, left, right
		if (chance0 == True and chance1 == True and chance2 == True and chance3 == True): #emergency case to ensure the code doen't stop working if a frontier is somehow chosen that can't latch on for unknown reasons.
			itWorked = True
		elif chance == 0:
			if complex(realnumber+1,imagnumber) in visitedcells: #go down, but checks that the direction desired is in the visited list already
				cells[realnumber-1][imagnumber-1].downwall = False #the second line in each if statement removes the necessary wall
				itWorked = True #Then it stops the loop
			chance0 = True #The chance_ values are an "emergency stop" but otherwise are useless
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

for c in range(int(rows/2)): #These sections here entail the formatting of the maze, giving it a border!
	walls[c][0].leftwall = True
for d in range(columns):
	cells[rows-1][d].downwall = True
for x in range(rows):
	for y in range(columns):
		cells[x][y].finish() #These two functions return the __str__ of Walls() and Cell()
		walls[x][y].walls()

for x in range(columns):   #This entire section has to do with maze customization as opposed to Prim's algorithm itself. 
	if aesthetic == 2:
		ex[0][x] = "△●○"
	elif aesthetic == 3:
		ex[0][x] = "♬--"
	elif aesthetic == 4:
		ex[0][x] = "☆**"
	else:
		ex[0][x] = ".--"
	for y in range(rows):
		ex[(y*2)+1][x] = walls[y][x]     #This adds appropriate walls and cells to the maze
		ex[(y*2)+2][x] = cells[y][x]
for y in range(rows):
	ex[(y*2)+1].insert(columns, "|")
	ex[(y*2)+1][0] = "|  "
	if aesthetic == 2:
		ex[(y*2)].insert(columns,"△")
	elif aesthetic == 3:
		ex[(y*2)].insert(columns,"♬")
	elif aesthetic == 4:
		ex[(y*2)].insert(columns,"☆")
	else:
		ex[(y*2)].insert(columns,".")
ex[0][0]="   "                                 #opens the starting and stopping point
ex[rows*2-1][columns]="   "
for a in range(len(ex)):
	print(*ex[a])

