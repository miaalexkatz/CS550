 #Mia Katz and Steph Hotz
#On my honor, I've neither given nor received anauthorized aid
#For our final project, we made a escape room game. This game consist of many rooms and puzzles to be completed in order to escape.


#WHAT I'VE DONE:
#Mia: You can add to the inventory and select items, but they don't properly remove yet.Also, you can unfog the bathroom now


#Steph: I am currently working on mkaing the item chosen appear next to the inventory to make it more clear what the user  has chosen.
#To do: program box functions for the rest of the boxes
import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.flip()
pygame.display.set_caption('Escape Game') 



#Loading images
itemchosen = "none"
t = pygame.font.SysFont('arial', 56) #renders all text
d = pygame.font.SysFont('arial', 30) #renders the word selected 

#The images for the rooms themselves
entryim = pygame.image.load('entry.png')
fireplaceim = pygame.image.load('fireplace.png')
kitchenim = pygame.image.load('kitchen.png')
bathroomim = pygame.image.load('bathroom.png')
couchim = pygame.image.load('couch.png')
tableim = pygame.image.load('table.png')
washroomim = pygame.image.load('washroom.png')
bedroomim = pygame.image.load('bedroom.png')
fireim = pygame.image.load('fire.png')

#Images for the boxes
bedboxim = pygame.image.load('bedbox.png')
couchboxim = pygame.image.load('couchbox.png')
pinkboxim = pygame.image.load('pinkbox.png')
colorshapeim = pygame.image.load('colorshapebox.png')
finalboardim = pygame.image.load('finalboard.png')
boxdoneim = pygame.image.load('completed.png')

#Arrow images
Rarrowim = pygame.image.load('Rarrow.png')
Larrowim = pygame.image.load('Larrow.png')
Darrowim = pygame.image.load('Darrow.png')
arrowim = pygame.image.load('arrow.png')
dirtim = pygame.image.load('dirt.png')

#Other images and items/ inventory
inventim = pygame.image.load('inventory.png')
laddersmall = pygame.image.load('laddersmall.png')
ladderlarge = pygame.image.load('ladderlarge.png')
screwdriverlarge = pygame.image.load('screwdriverlarge.png')
screwdriversmall = pygame.image.load('screwdriversmall.png')
tapesmall = pygame.image.load('tapesmall.png')
tapelarge = pygame.image.load('tapelarge.png')
bucketlarge = pygame.image.load('bucketlarge.png')
bucketsmall = pygame.image.load('bucketsmall.png')
waterbucketim = pygame.image.load('waterbucket.png')

#key images
closetkeylarge = pygame.image.load('closetkeylarge.png')
closetkeysmall = pygame.image.load('closetkeysmall.png')
key2im = pygame.image.load('key2.png')
key2large = pygame.image.load('key2large.png')
key1large = pygame.image.load('key1large.png')
key1small = pygame.image.load('key1small.png')
key3large = pygame.image.load('key3large.png')
key3small = pygame.image.load('key3small.png')
finalkeylarge = pygame.image.load('finalkeylarge.png')
finalkeysmall = pygame.image.load('finalkeysmall.png')
cleanerim = pygame.image.load('cleaner.png')

#starting and ending screens
startim = pygame.image.load('startscreen.png')
gameoverim = pygame.image.load('gameend.png')
startletter = pygame.image.load('startletter.png')
screen.blit(inventim, (0, 600))


# This is the player class which holds the variables for the different items used throughout the game.
class Player():
	def __init__(self):
		self.fogbathroom = False #if dirt is cleaned
		self.kitchenboxopen = False #if kitchen box is solved
		self.bathroombox = False #if bathroom box us opened
		self.gameend = False #if the game is over
		self.tablebox = False #if the table box is opened
		self.couchbox = False #if the couch box is opened
		self.washbox = False #if the washroom box is opened
		self.panel = True #if the panel is on
		self.bedbox = False #if the bedbox is solved
		self.fire = True #if the fire is on
		self.lockedcloset = True #if the closet is open
		self.cleaner = False #if cleaner is retreived
		self.roomid = "startscreen" #starting room id
		self.itemchosen = "none" #started inventory selection
		self.wirefix = False #if the wire has been taped
		self.key2ladder = False #if the second key has been retrieved
		self.finalboard = False #if you're in the key menu
		self.box = False #if you're looking at a box
		self.answer1, self.answer2, self.answer3, self.answer4 = 0,0,0,0 #box answers
		self.key1done, self.key2done, self.key3done = False, False, False #if you've found a final key

def text(text):
	screen.blit(inventim, (0, 600))
	doortext = t.render(text, True, (52, 37, 16))
	screen.blit(doortext, (10, 615))
	inventblit()


def inventblit():
	pygame.draw.rect(screen, (198, 184, 155), (875, 600, 125, 150))
	pygame.draw.line(screen, (52, 37, 16), (0, 600), (1000, 600), 4)
	pygame.draw.line(screen, (52, 37, 16), (875, 600), (875, 750), 4)
	hey = d.render("selected:", True, (52, 37, 16))
	screen.blit(hey, (895, 620))
	itemcheck()


inventory = []
for i in range(6):
	inventory.append("none")

def remove(itemname):
	for i in range(len(inventory)):
		if inventory[i] == itemname:
			inventory[i] = "none"

#Blits the images for the inventory, and checks their arrangement
def itemcheck():
	for i in range(6):
		if inventory[i] == "screwdriver":
			screen.blit(screwdriversmall, (i*150,675))
		elif inventory[i] == "tape":
			screen.blit(tapesmall, (i*150, 675))
		elif inventory[i] == "emptybucket":
			screen.blit(bucketsmall, (i*150, 675))
		elif inventory[i] == "fullbucket":
			screen.blit(waterbucketim, (i*150, 675))
		elif inventory[i] == "cleaner":
			screen.blit(cleanerim, (i*150, 675))
		elif inventory[i] == "key1":
			screen.blit(key1small, (i*150, 675))
		elif inventory[i] == "key2":
			screen.blit(key2im, (i*150, 675))
		elif inventory[i] == "key3":
			screen.blit(key3small, (i*150, 675))
		elif inventory[i] == "finalkey":
			screen.blit(finalkeysmall, (i*150, 675))
		elif inventory[i] == "closetkey":
			screen.blit(closetkeysmall, (i*150, 675))
		elif inventory[i] == "ladder":
			screen.blit(laddersmall, (i*150, 675))

#Adds items to the inventory
def itemadd(item):
	checks = 0
	incomplete = True
	while incomplete and checks < 6:
		if inventory[checks] == "none":
			inventory[checks] = item
			incomplete = False
		else:
			checks += 1


#This is the basic room function that sets up the pictures of the rooms and the arrows inside of them.
def room():
	if player.roomid == "entry":
		screen.blit(entryim, (0, 0))
		screen.blit(Rarrowim, (900, 400))
		screen.blit(Larrowim, (0, 400))
		screen.blit(arrowim, (450, 500))
#		screen.fill((0, 255, 0)
	elif player.roomid == "gameover": #placeholder for now, i'll draw something during my free tomorrow!
		screen.blit(gameoverim, (0,0))

	elif player.roomid == "startletter":
		screen.blit(entryim, (0, 0))
		screen.blit(startletter, (0,0))
		abc = d.render("click to start!", True, (57, 16, 37))
		screen.blit(abc, (600, 450))

	elif player.roomid == "fireplace":
		screen.blit(fireplaceim, (0, 0))
		screen.blit(Darrowim, (450, 500))
		screen.blit(arrowim, (750, 400))
		if player.fire  == True:
			screen.blit(fireim, (0, 0))
		if player.finalboard == True:
			screen.blit(finalboardim, (0,0))
			if player.key1done == True:
				screen.blit(key1large, (150, 150))
			if player.key2done == True:
				screen.blit(key2large, (350, 150))
			if player.key3done == True:
				screen.blit(key3large, (600, 150))
			keyz = d.render("3 keys to succeed", True, (52, 16, 37))
			screen.blit(keyz, (200, 450))
			screen.blit(arrowim, (450, 0))

	elif player.roomid == "kitchen":
		screen.blit(kitchenim, (0,0))
		screen.blit(Rarrowim, (900, 400))
		screen.blit(Larrowim, (0, 400))
		screen.blit(Darrowim, (450, 500))
		if player.box == True:
			screen.blit(colorshapeim, (0, 0))
			screen.blit(arrowim, (450, 0))
			if player.kitchenboxopen == True:
				screen.blit(boxdoneim, (0,0))
			else:
				numbers()

	elif player.roomid == "bathroom":
		screen.blit(bathroomim, (0,0))
		screen.blit(Larrowim, (0, 400))
		if player.fogbathroom == False:
			screen.blit(dirtim, (0, 0))
		if player.box == True:
			screen.blit(pinkboxim, (0, 0))
			screen.blit(arrowim, (450, 0))
			t = pygame.font.SysFont('arial', 100)
			texto = t.render(":", True, (52, 37, 16))
			t = pygame.font.SysFont('arial', 56)
			screen.blit(texto, (490, 200))
			if player.bathroombox == True:
				screen.blit(boxdoneim, (0,0))
			else:
				numbers()
	elif player.roomid == "couch":
		screen.blit(couchim, (0,0))
		screen.blit(Larrowim, (0, 400))
		if player.key2ladder == False:
			screen.blit(key2im, (100, 100))
		if player.box == True:
			screen.blit(bedboxim, (0,0))
			screen.blit(arrowim, (450, 0))
			if player.couchbox == True:
				screen.blit(boxdoneim, (0,0))
			else:
				numbers()
	elif player.roomid == "table":
		screen.blit(tableim, (0,0))
		screen.blit(Rarrowim, (900, 400))
		screen.blit(arrowim, (300, 500))
		if player.panel == True:
			pygame.draw.rect(screen, (202, 202, 202), (75, 360, 100, 125))
			pygame.draw.rect(screen, (52, 37, 16), (75, 360, 100, 125), 2)
		if player.box == True:
			screen.blit(pinkboxim, (0,0))
			screen.blit(arrowim, (450, 0))
			if player.tablebox == True:
				screen.blit(boxdoneim, (0,0))
			else:
				arrow(player.answer1, 138)
				arrow(player.answer2, 338)
				arrow(player.answer3, 580)
				arrow(player.answer4, 780)

	elif player.roomid == "washroom":
		screen.blit(washroomim, (0,0))
		screen.blit(Rarrowim, (900, 400))
		if player.cleaner == False:
			screen.blit(cleanerim, (300, 25))
	elif player.roomid == "bedroom":
		screen.blit(bedroomim, (0,0))
		screen.blit(Darrowim, (500, 500))
		if player.box == True:
			screen.blit(couchboxim, (0,0))
			screen.blit(arrowim, (450, 0))
			if player.bedbox == True:
				screen.blit(boxdoneim, (0,0))
			else:
				numbers()
	elif player.roomid == "startscreen":
		screen.blit(startim, (0, 0))

#Controls the blitting of the text with the boxes

def numbers():
	t = pygame.font.SysFont('arial', 178)
	doortext = t.render(str(player.answer1), True, (52, 37, 16))
	screen.blit(doortext, (138, 225))
	doortext = t.render(str(player.answer2), True, (52, 37, 16))
	screen.blit(doortext, (338, 225))
	doortext = t.render(str(player.answer3), True, (52, 37, 16))
	screen.blit(doortext, (580, 225))
	doortext = t.render(str(player.answer4), True, (52, 37, 16))
	screen.blit(doortext, (780, 225))
	t = pygame.font.SysFont('arial', 56)
	
#The box in the table required a different input, so this controls the appearance of the arrow input box.
def arrow(answer, xco):
	if answer == 0:
		screen.blit(Larrowim, (xco, 225))
	elif answer == 1:
		screen.blit(Darrowim, (xco, 225))
	elif answer == 2:
		screen.blit(Rarrowim, (xco, 225))
	else:
		screen.blit(arrowim, (xco, 225))


#Setting up which room starts

#Controls clicking for the entry/start room
def entry():
	if mousey < 500 and mousey > 400 and  mousex < 100:
		player.roomid = "table"
	if mousex > 900 and mousey < 500 and mousey > 400:
		player.roomid = "couch"
	if mousex < 550 and mousey < 600 and mousex > 450 and mousey > 500:
		player.roomid = "fireplace"
	elif mousey > 150 and mousey < 500 and mousex <575 and mousex > 425:
		if player.itemchosen == "finalkey":
			gameend = True
			player.roomid = "gameover"
			remove("finalkey")
		else:
			text("The door is locked, find the final key!")
	elif mousex > 200 and mousey < 500 and mousey > 270 and mousex < 350:
		text("What an odd shelf...")

def fireplace():
	if mousex <800 and mousex > 700 and mousey <650 and mousey > 350:
		player.roomid = "kitchen"
	elif mousex < 550 and mousey > 450 and mousex < 550 and mousey > 450:
		player.roomid = "entry"
	elif mousex < 575 and mousex > 200 and mousey > 225 and mousey < 500:
		if player.itemchosen == "fullbucket":
			text("You've extinguished the flame!")
			remove("fullbucket")
			player.fire = False
			inventblit()
		elif player.itemchosen == "emptybucket":
			text("You might need some water")
	elif mousex <650 and mousex > 520 and mousey <200 and mousey > 50:
		text("Seems suspicious...")
	elif mousex < 200 and mousey < 200:
		text("Lovely artwork!")
	elif 300 < mousex < 465 and mousey < 150:
		player.finalboard = True



def bathroom():
	if mousex < 100 and mousey < 500 and mousey > 400:
		player.roomid = "kitchen"
	elif  640< mousex <875 and 50< mousey <250:
		if player.itemchosen == "cleaner":
			print("good2")
			remove("cleaner")
			text("Could this text be... a clue?")
			player.fogbathroom = True
			room()
		else:
			text("The mirror needs to be cleaned")
	elif 700<mousex<930 and 40<mousey<200 :
		if itemchosen == 'bucket':
			bucketfull = True
			text("You've filled the bucket with water!")
	elif mousex < 850 and mousex > 650 and mousey < 375 and mousey > 260:
		if player.itemchosen == "emptybucket":
			text("You filled the bucket!")
			remove("emptybucket")
			itemadd("fullbucket")
			inventblit()
			print(inventory)
		else:
			text("A sink with running water.")
	elif mousex < 400 and mousey < 400:
		text("Hmmm, just an old shower")
	elif mousey < 500 and mousey > 450 and mousex < 700 and mousex > 600:
		player.box = True 


def couch():
	if mousex < 100 and mousey < 500 and mousey > 400:
		player.roomid = "entry"
	elif mousex < 675 and mousex > 325 and mousey < 150:
		text("Just a plain old painting")
	elif mousex > 150 and mousex < 750 and mousey < 550 and mousey > 200:
		text("You don't have time to relax!")
	elif mousex < 100 and mousey < 500 and mousey > 200:
		text("A well-watered plant")
	elif mousex > 800 and mousex < 925 and mousey < 550 and mousey > 500:
		player.box = True
	elif mousex < 200 and mousey < 200:
		if player.itemchosen == "ladder":
			if player.key2ladder == False:
				itemadd("key2")
				player.key2ladder == True
				remove("ladder")
				text("You got the second key!")
		else:
			text("You might need a ladder...")	
def table():
	if mousex > 900 and mousey < 500 and mousey > 400:
		player.roomid = "entry"
	elif mousex > 300 and mousey < 600 and mousex < 400 and mousey > 500:
		player.roomid = "bedroom"
	elif mousex < 600 and mousex > 400 and mousey < 350 and mousey > 150:
		text("Just some carnations")
	elif mousex > 75 and mousex < 175 and mousey < 450 and mousey > 330:
		if player.panel == True and player.wirefix == False:
			if player.itemchosen == "screwdriver":
				player.panel = False
				text("You're going to need some tape for that now!")
				remove("screwdriver")
				inventblit()
			else:
				text("Try unscrewing this panel")
		elif player.panel == False and player.wirefix == False:
			if player.itemchosen == "tape":
				player.wirefix = True
				text("You fixed the wire, and it dropped Key 3!")
				remove("tape")
				inventblit()
				itemadd("key3")
				inventblit()
			else:
				text("Ouch! Put some tape on that wire!")
		else: 
			text("You've already solved this")
	elif 450<mousex<550 and mousey>400:
		player.answer1, player.answer2, player.answer3, player.answer4 == 0,0,0,0
		player.box = True

			
def kitchen():
	if mousey < 500 and mousey > 400:
		if mousex < 100:
			player.roomid = "washroom"
		elif mousex > 900:
			player.roomid = "bathroom"
	if 400< mousex < 600 and 400 < mousey <500:
		player.box = True
	elif mousex < 550 and mousey > 450 and mousex < 550 and mousey > 450:
		player.roomid = "fireplace"
	elif mousex < 150 and mousey < 275 and mousey > 115:
		text("The time is 10:00")
	elif mousex < 400 and mousex > 150 and mousey < 500 and mousey > 140:
		text("The fridge is empty")
	elif mousex < 720 and mousex > 500 and mousey < 300 and mousey > 50:
		text("It's a lovely day outside!")
	elif mousex > 800 and mousex < 500 and mousex > 250:
		text("An ancient oven")

def washroom():
	if mousex > 900 and mousey < 500 and mousey > 400:
		player.roomid = "kitchen"
	elif mousex > 175 and mousex < 275 and mousey < 150 and mousey > 100:
		player.box == True
	elif mousex < 400 and mousey < 125 and mousex > 300:
		thing = False
		for i in range(6):
			if inventory[i] == "cleaner":
				thing = True
		if thing == False:
			itemadd("cleaner")
			text("You found some glass cleaner!")
			player.cleaner = True
	elif mousex < 225 and mousey < 500 and mousey > 250:
		text("An old washing machine")
	elif mousey < 500 and mousey > 250 and mousex < 450 and mousex > 225:
		text("And that's the dryer")
	elif mousex < 925 and mousex >700 and mousey < 500 and mousey > 125:
		if player.itemchosen == "closetkey" and player.lockedcloset == True:
			player.lockedcloset = False
			itemadd("ladder")
			remove("closetkey")
			text("There was a ladder in the closet!")  
		else:
			text("You're going to need a key for the closet")
	elif mousex < 275 and mousex > 175 and mousey < 150 and mousey > 100:
			text("...somebody put a fake box here. So mean.")


def bedroom():
	if mousex < 550 and mousey > 450 and mousex < 550 and mousey > 45:
		player.roomid = "table"
	elif mousex < 650 and mousex > 450 and mousey < 200:
		text("pentagon, circle, triangle, hexagon?")
	elif mousex < 820 and mousex > 300 and mousey > 250:
		text("What a comfy bed")
	elif mousex < 960 and mousey < 335 and mousey > 285 and mousex > 860:
		player.box = True




def mousepos():
	mouseloc = pygame.mouse.get_pos()
	mousex, mousey = mouseloc
	mouseclick()


def inventclicks():
	if mousex < 105:
		if player.itemchosen != inventory[0]:
			player.itemchosen = inventory[0]
		else:
			player.itemchosen = "none"
	elif mousex < 240 and mousex > 150:
		if player.itemchosen != inventory[1]:
			player.itemchosen = inventory[1]
		else:
			player.itemchosen = "none"
	elif mousex < 400 and mousex > 300:
		if player.itemchosen != inventory[2]:
			player.itemchosen = inventory[2]
		else:
			player.itemchosen = "none"
	elif mousex < 550 and mousex > 450:
		if player.itemchosen != inventory[3]:
			player.itemchosen = inventory[3]
		else:
			player.itemchosen = "none"
	elif mousex < 700 and mousex > 600:
		if player.itemchosen != inventory[4]:
			player.itemchosen = inventory[4]
		else:
			player.itemchosen = "none"
	elif mousex < 850 and mousey > 750:
		if player.itemchosen != inventory[5]:
			player.itemchosen = inventory[5]
		else:
			player.itemchosen = "none"
	if player.itemchosen != "none":
		if player.itemchosen == "screwdriver":
			screen.blit(screwdriversmall, ((900,650)))
		elif player.itemchosen == "tape":
			screen.blit(tapesmall, (900, 650))
		elif player.itemchosen == "emptybucket":
			screen.blit(bucketsmall, (900, 650))
		elif player.itemchosen == "fullbucket":
			screen.blit(waterbucketim, (900, 650))
		elif player.itemchosen == "cleaner":
			screen.blit(cleanerim, (900, 650))
		elif player.itemchosen == "key1":
			screen.blit(key1small, (900, 650))
		elif player.itemchosen == "key2":
			screen.blit(key2im, (900, 650))
		elif player.itemchosen == "key3":
			screen.blit(key3small, (900, 650))
		elif player.itemchosen == "finalkey":
			screen.blit(finalkeysmall, (900, 650))
		elif player.itemchosen == "closetkey":
			screen.blit(closetkeysmall, (900, 650))
		elif player.itemchosen == "ladder":
			screen.blit(laddersmall, (900, 650))
	if player.itemchosen == "none":
		inventblit()


#This is a directory for the various rooms. It sorts the clicking locations.
def mouseclick():
	if mousey > 600:
		inventclicks()
	if player.box == True:
		boxscreen()
	elif player.finalboard == True:
		finalpic()
	elif player.roomid == "startscreen":
		player.roomid = "startletter"
	elif player.roomid == "startletter":
		player.roomid = "entry"
	elif player.roomid =="entry":
		entry()
	elif player.roomid == "fireplace":
		fireplace()
	elif player.roomid == "bedroom":
		bedroom()
	elif player.roomid == "bathroom":
		bathroom()
	elif player.roomid == "table":
		table()
	elif player.roomid == "kitchen":
		kitchen()
	elif player.roomid == "washroom":
		washroom()
	elif player.roomid == "couch":
		couch()


#Controls the appearance of the text in the boxes to solve. This is printed in room()
def boxscreen():
	if mousex < 550 and mousex > 450 and mousey < 100:
		player.box = False
	elif mousex > 305 and mousex < 705 and mousey > 420 and mousey < 500:
		boxanswer()
	elif mousey > 180 and mousey <360:
		if mousex >138 and mousex < 240:
			if player.roomid != "table":
				if player.answer1+1 == 10:
					player.answer1 = 0
				else:
					player.answer1 +=1
					print("add1")
			elif player.roomid == "table":
				if player.answer1 +1 == 4:
					player.answer1 = 0
				else:
					player.answer1 +=1
					print("add2")
		elif mousex < 440 and mousex > 300:
			if player.roomid != "table":
				if player.answer2+1 == 10:
					player.answer2 = 0
				else:
					player.answer2 +=1
			else:
				if player.answer2 +1 >= 4:
					player.answer2 = 0
				else:
					player.answer2 +=1
		elif mousex < 665 and mousex > 562:
			if player.roomid != "table":
				if player.answer3+1 == 10:
					player.answer3 = 0
				else:
					player.answer3 +=1
			else:
				if player.answer3 +1 >= 4:
					player.answer3 = 0
				else:
					player.answer3 +=1

		elif mousex > 757 and mousex < 852:
			if player.roomid != "table":
				if player.answer4+1 == 10:
					player.answer4 = 0
				else:
					player.answer4 +=1
			else:
				if player.answer4 +1 >= 4:
					player.answer4 = 0
				else:
					player.answer4 +=1

#Checks the input answers for the boxes, and gives items if solved.
def boxanswer():
	print("answered")
	answer = (player.answer1*1000)+player.answer2*100+player.answer3*10+player.answer4
	print(answer)
	if player.roomid == "table":
		if player.tablebox == False:
			if answer == 213:
				text("You found the closet key!")
				itemadd("closetkey")
				inventblit()
				player.tablebox = True
			else: 
				text("Sorry, that's not right")
		else:
			screen.blit(boxdoneim, (0,0))
	if player.roomid == "bedroom":
			if answer == 4125:
				if player.bedbox == False:
					itemadd("emptybucket")
					text("You found a bucket!")
					player.bedbox = True
			else:
				text("Sorry, that's not it!")
	elif player.roomid == "bathroom":
			if answer == 1000:
				if player.bathroombox == False:
					itemadd("tape")
					text("You found some electrical tape!")
					player.bathroombox = True
			else: text("Hmm, that's not right")

	elif player.roomid == "kitchen":
		if answer == 5136:
			if player.kitchenboxopen == False:
				itemadd("screwdriver")
				text("You found a screwdriver!")
				player.kitchenboxopen = True
		else:
			text("Sorry, try again!")

	elif player.roomid == "couch":
		if answer == 1181: 
			if player.couchbox == False:
				itemadd("key1")
				text("You found the first final key!")
				player.couchbox = True
		else:
			text("Sorry, but don't give up!")

def finalpic():
	if 450<mousex<550 and mousey < 100:
		player.finalboard = False
	if player.itemchosen == "key1":
		player.key1done = True
		remove("key1")
		text("You've inserted key 1")
	elif player.itemchosen == "key2":
		player.key2done = True
		remove("key2")
		text("You've inserted key 2")
	elif player.itemchosen == "key3":
		remove("key3")
		text("You've inserted key 3")
		player.key3done = True
	if player.key1done == True and player.key2done == True and player.key3done == True:
		text("You found the final door key!")
		itemadd("finalkey")

player = Player()
notdone = True
inventblit()
while notdone:
	room()
	pygame.display.flip()
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			notdone = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseloc = pygame.mouse.get_pos()
			mousex, mousey = mouseloc
			mouseclick()
	pygame.display.update()

			
