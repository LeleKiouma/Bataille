from random import randint
class Player() :
    """
    the class player with all the info we need about the player
    """

    def __init__(self,y_pos_of_cards:int,y_pos_of_reversed_card:int) :
        """
            initalize the constructor 
        Args:
            y_pos_of_cards (int): the y pos of the card when flipped
            y_pos_of_reversed_card (int): the y pos of the card when they are on the back
        """
        self.list_of_cards = []
        self.score = 0
        self.y_pos_of_cards = y_pos_of_cards
        self.y_pos_of_reversed_card = y_pos_of_reversed_card
    
    def ajouter_carte(self,carte_ajouter:object) :
        """
            add the card to the deck of the player
        Args:
            carte_ajouter (object): the card object
        """
        self.list_of_cards.append(carte_ajouter)
        self.score += carte_ajouter.value
        
    def supprimer_cartes(self) :
        """
            delete the first card of the deck
        """
        self.score -= self.list_of_cards[0].value
        self.list_of_cards.pop(0)
    
    def melanger_cartes (self) :
        """
        randomly change the deck
        """
        self.cards_length = len(self.list_of_cards)
        self.random = 0
        for index in range(self.cards_length) :
            self.random = randint(0,self.cards_length-1)
            self.list_of_cards[index] , self.list_of_cards[self.random] = self.list_of_cards[self.random],self.list_of_cards[index] 