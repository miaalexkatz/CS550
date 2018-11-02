
class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		if self.rank == 1:
			suitprint = " of Clubs"
		if self.rank == 2:
			suitprint = " of Diamonds"
		if self.rank == 3:
			suitprint = " of Hearts"
		if self.rank == 4:
			suitprint = " of Spades"
		if self.rank <= 10:
			rankprint = str(self.rank)
		elif self.rank == 11:
			rankprint = "Jack"
		elif self.rank == 12:
			rankprint = "Queen"
		elif self.rank == 13:
			rankprint = "King"
		elif self.rank == 14:
			rankprint = "Ace"

	def __str__(self):
		return str(self.rankprint + self.suitprint)

