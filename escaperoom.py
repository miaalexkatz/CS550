#Mia Katz and Steph Hotz idk the last name sorry

import pygame
screen = pygame.display.set_mode((1000, 750)) 


done = False
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True


