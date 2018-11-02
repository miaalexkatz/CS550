from cards import Card

class Deck:

	def __init__(self):
		fulldeck = []
		for i in range(2, 15):
			for j in range(4):
				newcard = Card(j, i)
				fulldeck.append(newcard)
deck = Deck()
print(deck)