import random 
class Cell:
	def __init__(self, ):
		self.upwall = True
		self.leftwall = True
		self.downwall = True
		self.rightwall = True
		#self.isVisited = False
		#self.frontier = False
		self.adjacentchecks = 0
		self.identity = "|_|"
	def finish(self):
		if self.upwall == True:
			if self.leftwall == True:
				if self.downwall == True:
					self.identity = "|__"
				else:
					self.identity = "|  "
			elif self.rightwall == True:
				if self.downwall == True:
					self.identity = "__|"
				else:
					self.identity = "  |"
			elif self.downwall == True:
				self.identity = "___"
		elif self.rightwall == True:
			if self.leftwall == True:
				self.identity = "| |"
			if self.downwall == True:
				self.identity = "__|"
		elif self.leftwall == True:
			if self.downwall == True:
				self.identity = "|__"
		else:
			self.identity = "   "

	def __str__(self):
		return self.identity


#to do: set the cell graphics (|_| and so on)
#ask about making a list of all of the individual cell values for graphical reasons tomorrow, mia!!!! good job talking to people
