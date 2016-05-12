from card import Card
from hand import Hand
from deck import Deck
from ofc import Player

myPlayer = Player()
myDeck = Deck()
myDeck.shuffle()

"""
for i in range(2):
    myPlayer.addTop(myDeck.pop())

for i in range(3):
    myPlayer.addMid(myDeck.pop())

for i in range(3):
    myPlayer.addBot(myDeck.pop())

myPlayer.printStatus()

myPlayer.playCard(myDeck)
"""

while not myPlayer.fullHands():
    myPlayer.printStatus()
    myPlayer.playManual(myDeck)

print "You are done!"

myPlayer.printStatus()
