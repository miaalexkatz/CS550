import random 
class Cell:
	def __init__(self):
		self.downwall = True
		self.identity = "|_|"

	def finish(self):
	#	if self.upwall == True:
		if self.downwall == False:
			self.identity = ".  "     
		else:                               
			self.identity = ".--"                                    
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


#to do: set the cell graphics (|_| and so on)
#ask about making a list of all of the individual cell values for graphical reasons tomorrow, mia!!!! good job talking to people
