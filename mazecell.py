#Mia Katz
#12 November 2018
#The classes for the bottom cells and cell walls.
import random 
class Cell:
	def __init__(self, aesthetic):
		self.downwall = True
		self.identity = "|_|"
		self.aesthetic = aesthetic
                                            
	def finish(self):
		if self.downwall == False:
			if self.aesthetic == 2:
				self.identity = "△  "
			elif self.aesthetic == 3:
				self.identity = "♬  "
			elif self.aesthetic == 1:
				self.identity = ".  " 
			elif self.aesthetic == 4:
				self.identity = "☆  "    
		else:                      
			if self.aesthetic == 2:
				self.identity = "△●○"  
			elif self.aesthetic == 3:
				self.identity = "♬--"       
			elif self.aesthetic == 1:
				self.identity = ".--"      
			elif self.aesthetic == 4:
				self.identity = "☆**"                              
	def __str__(self):
		return self.identity
# note: left wall takes precedent.
class Walls:
	def __init__(self):
		self.leftwall = True
		self.identity = "|_|"
	
	def walls(self):
		if self.leftwall == True:
			self.identity = "|  "                              
		else:
				self.identity = "   "       

	def __str__(self):
		return self.identity

#You have likely noticed by now that the are only two wall types, the downward wall and the left wall. In essence, each cell is set to have it's downward wall exist or left wall exist. The bottom wall has variations based on the style selected by the user. They are in separated classes as I was unable to return multiple \n from a single class, as it printed each cell in one line as opposed to a desired two.