from card import Card

class Hand(object):
	
	def __init__(self): # creates an empty hand
		self._cards = []
		
	def __len__(self): # return number of cards
		return len(self._cards)
	
	def __iter__(self):
		return iter(self._cards)
		
	def add(self, card): # adds a card to the hand
		self._cards.append(card)

	def printHand(self):
		for i in self._cards:
			print i.value
"""			
	# Evaluation Methods
	
	def getRanks(self):
		ranks = []
		for i in self._cards:
			ranks.append(i.rank)
		return ranks

	def checkFlush(self):
		suits = []
		for i in self._cards:
			suits.append(i.suit)
		return len(set(suits)) == 1
		
        def checkStraight(self):
"""
