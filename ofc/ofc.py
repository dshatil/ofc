from card import Card
from hand import Hand

class Player(object):

    def __init__(self):
        self.topHand = Hand()
        self.midHand = Hand()
        self.botHand = Hand()

    def addTop(self, card):
        self.topHand.add(card)

    def addMid(self, card):
        self.midHand.add(card)

    def addBot(self, card):
        self.botHand.add(card)

    def printStatus(self):
        print ("Top Hand: ")
        self.topHand.printHand()
        print ("\n\nMiddle Hand: ")
        self.midHand.printHand()
        print ("\n\nBottom Hand: ")
        self.botHand.printHand()

    def oneCard(self, deck):
        nextCard = deck.pop()
        print "the current card is " + nextCard.value
        choice = raw_input("where would you like this card?\nplease enter bot or 1 for bottom,\nmid or 2 for middle, top or 3 for top\n--> ")
        if choice == "1" or choice == "bot":
            self.addBot(nextCard)
        elif choice == "2" or choice == "mid":
            self.addMid(nextCard)
        elif choice == "3" or choice == "top":
            self.addTop(nextCard)
        else:
            print "that choice was not recognized!"
            deck.heap(nextCard)
