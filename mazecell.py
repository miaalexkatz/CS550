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
	#	if self.upwall == True:
		if self.leftwall == True:
			if self.downwall == False:
				if self.rightwall == True:
					self.identity = "+  +"                                    #UT LT DF RT
				else:
					self.identity = "+  +"                                    #UT LT DF RF
			else:
				if self.rightwall == True:
					self.identity = "+--+"                                    #UT LT DT RT
				else:
					self.identity = "+--+"                                   #UT LT DT RF
		else:
			if self.downwall == False:
				if self.rightwall == True:
					self.identity = "+  +"                                    #UT LF DF RT 
				else:
					self.identity = "+  +"                                    #UT LF DF RF
			else:
				if self.rightwall == True:
					self.identity = "+--+"                                    #UT LF DT RT
				else:
					self.identity = "+--+"                                    #UT LF DT RF

	def walls(self):
		if self.leftwall == True:
			if self.downwall == False:
				if self.rightwall == True:
					self.identity = "|  |"                                    #UT LT DF RT
				else:
					self.identity = "|   "                                    #UT LT DF RF
			else:
				if self.rightwall == True:
					self.identity = "|  |"                                    #UT LT DT RT
				else:
					self.identity = "|   "                                   #UT LT DT RF
		else:
			if self.downwall == False:
				if self.rightwall == True:
					self.identity = "   |"                                    #UT LF DF RT 
				else:
					self.identity = "    "                                    #UT LF DF RF
			else:
				if self.rightwall == True:
					self.identity = "   |"                                    #UT LF DT RT
				else:
					self.identity = "    "                                    #UT LF DT RF


	def __str__(self):
		return self.identity


#to do: set the cell graphics (|_| and so on)
#ask about making a list of all of the individual cell values for graphical reasons tomorrow, mia!!!! good job talking to people
