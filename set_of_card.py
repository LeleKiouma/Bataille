from card import *
from random import randint, getrandbits



import doctest
doctest.testmod()

class Set_of_card(object):
    """
        The set_of_card class allows to easily manipulate the deck of card (shuffling, distributing)
    """
    def __init__(self):
        self.deck_of_cards = []
        for color in TYPES: # the 4 stand for the 4 type of card 
            for str_value, value in VALUES.items():  # str_value is a string of the number and value is the int of this value ex: if str_value = "two", then value = 2
                # create all the cards with their correct path
                self.deck_of_cards.append(Card(value, "assets/deck_of_cards/" + str(str_value) + "_of_"+ str(color) + ".png"))
    
    def shuffle(self) -> None:
        """
            shuffle the deck of card
        """
        self.cards_length = len(self.deck_of_cards)
        for index in range(self.cards_length) :
            self.random = randint(0,self.cards_length-1)
            self.deck_of_cards[index] , self.deck_of_cards[self.random] = self.deck_of_cards[self.random],self.deck_of_cards[index] 
    
    def split_in_two(self, player1: object, player2: object) -> None:
        """
            split in two and randomly all the card to the players 
            
            Args:
                player1: (object) the player 1
                plater2: (object) the player 2
        """
        if (not isinstance(player1, Player)) or (not isinstance(player2, Player)):
            return
        
        player1.list_of_cards.clear() # clear the cards of both players
        player2.list_of_cards.clear()
        
        self.shuffle()                # shuffle the deck
        
        for element in self.deck_of_cards :
            self.random_bool = bool(getrandbits(1)) # create a random bool 
            if self.random_bool == True :
                player1.add_card(element)           # add the card to player 1
            else :
                player2.add_card(element)           # add the card to player 2
                
        player1.update_score()        # calculate their score
        player2.update_score()
