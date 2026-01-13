class Card:
    def __init__(self, v, c):
        self.value = v
        self.colour = c
    def __str__(self):
        return self.colour + self.value
    
class DeckCards:
    def __init__(self):
        colours = ["S", "H", "C", "D"]
        values = ["A","2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]

        self.cards = []
        for c in colours:
            for v in values:
                self.cards.append(Card(v,c))
        # Mtn le talon est rempli avec 4*13=52 cartes différentes
    
    def __str__(self):
        pass
    def shuffle_cards(self):
        pass
    def draw_card(self):
        pass

# essai class Card avec Roie Coeurs
mycard1 = Card("K", "H")
print(mycard1)

# tester le talon
mydeck = DeckCards()
print(mydeck.cards) #str() de DeckCards n'existe pas encore