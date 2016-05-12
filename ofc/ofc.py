from card import Card
from hand import Hand
from errors import OFCError
import random

class Player(object):

    def __init__(self):
        self.topHand = Hand()
        self.midHand = Hand()
        self.botHand = Hand()

    def addTop(self, card):
        if len(self.topHand) >=3:
            raise OFCError('This hand is full!')
            return
        self.topHand.add(card)
        

    def addMid(self, card):
        if len(self.midHand) >= 5:
            raise OFCError('This hand is full!')
            return
        self.midHand.add(card)

    def addBot(self, card):
        if len(self.botHand) >= 5:
            raise OFCError('This hand is full!')
            return
        self.botHand.add(card)

    def fullHands(self):
        return len(self.botHand) == 5 and len(self.midHand) == 5 and len(self.topHand) == 3

    def printStatus(self):
        print ("Top Hand: ")
        self.topHand.printHand()
        print ("\n\nMiddle Hand: ")
        self.midHand.printHand()
        print ("\n\nBottom Hand: ")
        self.botHand.printHand()

    def addCard(self, card, hand):
        if hand == 1:
            self.addBot(card)
        elif hand == 2:
            self.addMid(card)
        elif hand == 3:
            self.addTop(card)

    def playManual(self, deck):
        nextCard = deck.pop()
        print "\nthe current card is " + nextCard.value
        choice = raw_input("where would you like this card?\nplease enter bot or 1 for bottom,\nmid or 2 for middle, top or 3 for top\n--> ")
        if choice == "1" or choice == "bot":
            try:
                self.addBot(nextCard)
            except OFCError:
                print("that hand is full! try again")
                deck.heap(nextCard)
                self.playManual(deck)
        elif choice == "2" or choice == "mid":
            try:
                self.addMid(nextCard)
            except OFCError:
                print("that hand is full! try again")
                deck.heap(nextCard)
                self.playManual(deck)
        elif choice == "3" or choice == "top":
            try:
                self.addTop(nextCard)
            except OFCError:
                print("that hand is full! try again")
                deck.heap(nextCard)
                self.playManual(deck)
        else:
            print "that choice was not recognized!"
            deck.heap(nextCard)

    def playRandom(self, card):
        spaces = []
        for i in range(5 - len(self.botHand)):
            spaces.append(1)
        for i in range(5 - len(self.midHand)):
            spaces.append(2)
        for i in range(3 - len(self.topHand)):
            spaces.append(3)
        if len(spaces) == 0:
            raise OFCError("No empty spaces!")
        else:
            choice = random.choice(spaces)
            self.addCard(card, choice)

"""

def Evaluator(Player1, Player2):
    
        
"""
