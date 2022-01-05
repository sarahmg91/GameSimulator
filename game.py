### This file will be used to set up the individual game ##

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
        self.playedCards = self.PlayedCards + 1
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

    def addDeck(card):
            self.cardList[card.name] = card
            self.deckTotal = self.deckTotal + card.totalCards
            self.availableCards = self.availableCards + card.availableCards

    def playCard(self):
        pass
        ## TODO: Issue number #2
        ## sets up the play suits



## Practice Area ##

cardTest = CardSuit(10, "trumps")

list = []
list.append(cardTest)

practiceDeck = CardDeck(list)
print(practiceDeck.cardList)





#def game(suits, ):
