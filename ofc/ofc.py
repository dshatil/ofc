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
