class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        available = True

    def getNum(self):
        return self.num

    def getSuit(self):
        return self.suit

class DeckOfCards:
    def __init__(self):
        self.min = 2
        self.max = 14
        self.deck = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.dealtIndex = 0

    def populateDeck(self):
        deck = []
        for x in self.suits:
            for i in range(self.min, self.max+1):
                newCard = Card(i, x)
                deck = deck + [newCard]

        self.deck = deck

    def printDeck(self):
        for x in self.deck:
            print(x.getNum(), x.getSuit())

    def shuffle(self)

    def remainingCards(self):
        return len(self.deck) - dealtIndex

def main():
    deck = DeckOfCards()
    deck.populateDeck()

    deck.printDeck()

main()
        
