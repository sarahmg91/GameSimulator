### This file will be used to set up the individual game ##
from random import *
## Inputs

## Class set up

class CardSuit:
    """"A class to store required odds and information about the cards"""
    def __init__(self, numCards=0, name="practice"):
        self.totalCards = numCards
        self.availableCards = numCards
        self.name = name
        self.playedCards = 0
        self.winner = False

    def playCard(self):
        self.playedCards = self.playedCards + 1
        self.availableCards = self.availableCards - 1

class CardDeck:
    """A class to store all the cards within the deck"""
    def __init__(self, cardList):
        self.deckTotal = 0
        self.availableCards = 0
        self.playedCards = 0
        self.cardList = dict()

        for card in cardList:
            # cards must be of a class CardSuit, they also need to be unique. Force this somehow.
            self.addDeck(card)

    def addDeck(self, card):
            self.cardList[card.name] = card
            self.deckTotal = self.deckTotal + card.totalCards
            self.availableCards = self.availableCards + card.availableCards

    def playCard(self, card):
        self.playedCards = self.playedCards + 1
        self.availableCards = self.availableCards - 1
        self.cardList[card].playCard()

    def selectCard(self):
        randSelection = randint(0,self.availableCards-1)
        iteration = 0
        #print("rand # selected : " + str(randSelection))

        for cardKey in self.cardList:
            availableCards = self.cardList[cardKey].availableCards
            if availableCards > 0 and randSelection <= availableCards + iteration - 1:
                self.playCard(cardKey)
                #print("selected card type : "+ cardKey)
                return cardKey

            else:
                iteration = iteration + self.cardList[cardKey].availableCards
            #    print("I am at : " + str(iteration) + " iteration after suit " + cardKey)

        ## TODO: Issue number #2
        ## sets up the play suits

## Practice Area ##






#def game(suits, ):
