from card import *
from random import randint, getrandbits
class Set_of_card(object):

    def __init__(self):
        self.deck_of_cards = []
        for type in range(0, 4): 
            for str_value, value in VALUES.items():
                self.deck_of_cards.append(Card(value, "assets/deck_of_cards/" + str(str_value) + "_of_"+ str(TYPES[type]) + ".png"))
    
    def shuffle(self)->None:
        """
            shuffle the deck of card
        """
        self.cards_length = len(self.deck_of_cards)
        for index in range(self.cards_length) :
            self.random = randint(0,self.cards_length-1)
            self.deck_of_cards[index] , self.deck_of_cards[self.random] = self.deck_of_cards[self.random],self.deck_of_cards[index] 
    
    def split_in_two(self, player1: object, player2: object)->None:
        """
            # vide les cartes dans les mains des joueurs ,melange les cartes de la pile de carte a distribué
            puis ajoute les cartes aléatoirement dans la main d'un des joueurs 
            Parameters:
            ----------
                player1: (object) the player 1
                plater2: (object) the player 2
            Return:
            ---------
                nothing
        """

        self.shuffle()
        for element in self.deck_of_cards :
            self.random_bool = bool(getrandbits(1)) #create a random bool 
            if self.random_bool == True :
                player1.list_of_cards.append(element) 
            else :
                player2.list_of_cards.append(element)
        player1.update_score()
        player2.update_score()
