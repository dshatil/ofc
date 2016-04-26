from card import Card
import random

class Deck(object):
	
	def __init__(self): # creates a standard 52-card deck
		self._cards = []
		for i in Card.RANKS:
			for j in Card.SUITS:
				self._cards.append(Card(i, j))
				
	def __len__(self):	# returns number of cards in the deck
		return len(self._cards)

	def __iter__(self): # returns an iterator on cards in the deck
		return iter(self._cards)
		
	def shuffle(self): # uses random.shuffle to shuffle the deck
		random.shuffle(self._cards)

	def pop(self): # pops the top card
                return self._cards.pop()
