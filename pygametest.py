#PyGame Code Examples!
#Mia Katz, E Block, On my honor, I have neither given nor received unauthorized aid
#Sources: www.pygame.org/docs and pygametutorials.wikidot.com/tutorials

#Welcome to the interactive introduction to PyGame! Today, you'll see some examples on setting up PyGame, drawing some shapes and/or text, playing some music, importing images, and processing events! First, import the module.


import pygame
rectx = 10 #<- ignore until later; this is for the events setup


#Initializes the PyGame functions and the display. It is mandatory.
pygame.init() 

#Sets the dimensions of the display window. 400 and 300 may be replaced with whatever you'd like. 
#Note that this must be stored in a variable so it may be reused in almost every other function. It will replace "Surface" in surface functions.
screen = pygame.display.set_mode((400, 300)) 

#Changes the name of the game window. 
pygame.display.set_caption('Examples') 

#STORING COLOR---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Though not a PyGame function itself, storing RGB values in tuples is a great way to reuse colors
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

#This is actually the Surface.fill() function. However, you must replace "Surface" with the name of the display. screen is my display name
screen.fill(white)

#DRAWING-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The following is a rectangle drawn on the display. The top left corner is specified by the first two numbers, 100 and 100. 50 is the width, and 70 is the height. Replace them with whatever. NOTE THAT ANYTHING DRAWN HERE WILL NOT BE REPEATED
pygame.draw.rect(screen, red, (100, 100, 50, 70)) 
#pygame.draw.rect(Surface, color, (x_topleft, y_topleft, width, height) optional_line_width)
#If line_width is not provided, the shape will fill.

#Draws a blue not-filled circle. The provided point is the center, and 10 is the radius.
pygame.draw.circle(screen, blue, (200, 200), 80, 5)
#pygamne.draw.circle(Surface, color, (center_x, center_y), radius, optional_line_width)

#The ellipse function is not a circle, but a rounded rectangle. However, the coordinates are the center, not the corner.
pygame.draw.ellipse(screen, green, (350, 175, 30, 120))
#pygame.draw.ellipse(Surface, color, (x_topleft, y_topleft, width, height) optional_line_width)

#Arc is based on the ellipse function, but onlt draws a portion of the curve. The degrees of the arc must be provided in radians. Line_weight will default to 1.
pygame.draw.arc(screen, red, (300, 100, 30, 40), 2, 6.28, 6)
#pygame.draw.arc(Surface, color, (center_x, center_y, width, height), start_radian, end_radian, optional_line_width)

#Draws a line between two specified points
pygame.draw.line(screen, green, (50, 50), (350, 50), 8)
#pygame.draw.line(Surface, color, (x1, y1), (x2, y2))

#The polygon function can take any number of points. Here, it draws a triangle. All points must reside within a massive parentheses to pass as one argument.
pygame.draw.polygon(screen, red, ((50, 280), (200, 280), (125, 240)))
#pygame.draw.polygon(Surface, color, ((x1, y1), (x2, y2), (x3, y3), ... ))

#IMAGES -------------------------------------------------------------------------------------------------------------------------------------------------------------------

#First, you must load the image and store it in a variable

testimage = pygame.image.load('cavs.png') #from there, Surface.blit() will place it for you. Remember to put the destination in parentheses
screen.blit(testimage, (0, 0))

#TEXT--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#First, you must initialize the module. However, this is included in PyGame's init(), so it's not needed.
t = pygame.font.SysFont('arial', 56).               #variable = pygame.font.SysFont('font_name', size)
exam = t.render("hello", True, (0, 255, 0))         #other = variable.render("text", True, (color))
screen.blit(exam, (200, 100))

#MUSIC--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Initialize first
pygame.mixer.init() 
#Arguments are optional, but can include frequency, channel amount and buffer.

#Note: This section is commented to avoid having to distribute sound files I don't own.

#mixer.sound(file_name) -> loads the music track 
#mixer.start(repetitions)->Plays the sound for a selected duration.


#HOW TO CLOSE THE SURFACE WINDOW --------------------- MANDATORY ----------------------------------------------------------------------------------------------------------

 #Controls the closure of the game window, inside of an INFINITE loop. This section is MANDATORY.

done = False
while not done:
	for event in pygame.event.get(): #this for loop tracks the PyGame events.
		if event.type == pygame.QUIT: #pygame.QUIT is the action of pressing the x button on the window. If the x has been pressed, the window closes.
			done = True

#TESTING TYPES OF EVENTS __________________________________________________________________________________________________________________________________________________

#The first type of event is a mouse clicking event. You check it the same way you'd check for surface exits. Note that this is checked every time an event occurs. 
		if event.type == pygame.MOUSEBUTTONDOWN: #It checks for the press of a click. MOUSEBUTTONUP will check for the release. MOUSEMOTION checks for cursor motion.
			rectx += 10
			pygame.draw.rect(screen, green, (rectx, 100, 50, 70)) 
#consider that the rest of the images drawn earlier are not redrawn because they are not "redrawn" in this infinite loop. if they were to be redrawn, you would place them here.

#This second event is a key press event. PyGame can differentiate between keys, but you must nest the checks inside of a main key check.
		if event.type == pygame.KEYDOWN:                 #checks for the press of a key. KEYUP will check for the release
			if event.key == pygame.K_SPACE:              #This checks for the individual key. Note that it begins with K_. The a key would be K_a, for example
				screen.fill(red)

			elif event.key == pygame.K_RETURN:           #The main keycheck is capable of processing all of the keys. 
				screen.fill(blue)

#ONE FINAL PART TO THIS LOOP-----------------------------------------------------------------------------------------------------------------------------------------------

	pygame.display.flip() #flip() updates the game window! update() will also work in its place. it must remain in the infinite while loop
#drawing a rectangle

#Thank you for reading this interactive tutorial!Have fun repeatedly clicking to expand the green rectangle!