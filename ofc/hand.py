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
                        print i.value,
                        
