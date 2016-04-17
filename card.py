class Card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = str(suit).lower()
		self.value = str(self.rank) + self.suit
		
	def display(self):
		print self.value

	def higher(self, other):
            return(self.rank > other.rank)

		def lower(self, other):
			return(self.rank < other.rank)

		def suited(self, other):
			return (self.suit == other.suit)

	RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	
	SUITS = ["s", "h", "c", "d"]