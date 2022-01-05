### This file will be used to set up the individual game ##
from game import *

cardTest = CardSuit(2, "trumps")
cardTest2 = CardSuit(5, "spades")
cardTest3 = CardSuit(10, "diamond")


list = []
list.append(cardTest)
list.append(cardTest2)
list.append(cardTest3)

practiceDeck = CardDeck(list)
#print(practiceDeck.cardList)
#print(practiceDeck.deckTotal)

i = 0
#print(practiceDeck.cardList)

while i < 10:
    i = i + 1

    print("STATUS")

    for each in practiceDeck.cardList:
        print(each +" : " + str(practiceDeck.cardList[each].availableCards))

    print("selection number: " + str(i))

    practiceDeck.selectCard()
    print("deck is of length : " + str(practiceDeck.availableCards))
    #print(practiceDeck.deckTotal)
