class Dog:
	#constructor (you need those little underscores when you write the initial statement)
	def __init__(self, name):
		self.fullness = 5
		self.energy = 5
		self.happiness = 5
		self.name = name
		self.turns = 0

	def play(self):
		if self.energy > 0 and self.fullness > 0:
			self.happiness +=1
			self.fullness -=1
			self.energy -=1
			self.turns += 1
			status = self.name+" played and had a great time!"
			if self.energy == 0:
				status += "\nNow they're very tired..."
			if self.energy == 0:
				status += "\n Now they're very hungry..."
		elif self.energy == 0:
			status = "Oh no... "+self.name+" has starved to death"
		elif self.fullness == 0:
			status = "Oh gosh! "+self.name+

	def stats(self):
		info = "Name: " + self.name
		if turns < 100:
			info += """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░████████░░░░░░░░░░░░
░░░░░░░░░░██        ██░░░░░░░░░░
░░░░░░░░██            ██░░░░░░░░
░░░░░░██        ████    ██░░░░░░
░░░░░░██            ██  ██░░░░░░
░░░░░░██            ██  ██░░░░░░
░░░░██              ██    ██░░░░
░░░░██                    ██░░░░
░░░░██                    ██░░░░
░░░░██                    ██░░░░
░░░░██                    ██░░░░
░░░░██                    ██░░░░
░░░░░░██                ██░░░░░░
░░░░░░░░████████████████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

		"""
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nFullness: " + str(self.fullness)
		return info
start = input("You've received a wonderful egg! You should name it: ")
dog1 = dog(start)

while True:
	print(dog1.stats())
	choice == input("What would you like to do with "+self.name+"?")
	if choice == 'play':
		dog1.play()