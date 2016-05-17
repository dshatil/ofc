from card import Card
from hand import Hand
from deck import Deck
from ofc import Player
from pokereval.hand_evaluator import HandEvaluator

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

#

"""

while not myPlayer.fullHands():
    myPlayer.printStatus()
    myPlayer.playManual(myDeck)

print "You are done!"

myPlayer.printStatus()

"""

#


for i in range(13):
    myPlayer.playRandom(myDeck.pop())

botscore = HandEvaluator.Five.evaluate_rank(myPlayer.botHand)
midscore = HandEvaluator.Five.evaluate_rank(myPlayer.midHand)

myPlayer.printStatus()

print "Hand evaluations:\n"
print "Bottom Hand: " + str(botscore) + "\nMiddle Hand: " + str(midscore)
