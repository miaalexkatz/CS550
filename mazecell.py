import random 
class Cell:

	def __init__(self):
		self.upwall = True
		self.leftwall = True
		self.downwall = True
		self.rightwall = True
		self.isVisited = False
		self.frontier = False
		self.adjacentchecks = 0
		self.identity = "|_|"

	def selected(self):
		chance = random.randrange(4)
		if chance < 1:
			#go up

	def finish(self):
		if self.upwall == True:
			if self.leftwall == True:
				self.identity = "|  "
			elif self.rightall == True:
				self.identity = "  |"
			elif self.downwall = True:
				self.identity = "___"
		elif self.rightwall == True:
			if self.leftwall == True:
				self.identity = "| |"
			if self.downall == True:
				self.identity = "__|"
		elif self.leftwall == True:
			if self.downwall == True:
				self.identity = "|__"
		else:
			self.identity = "   "

	def __str__(self):
		return self.identity


#to do: set the cell graphics (|_| and so on)

