import pygame


TYPES = ("clubs",  "diamonds", "hearts", "spades") # usefull to create all the cards
VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14}

class Card(object):
    """
        Each card has:  - a value  (the type of card played: ace, king, queen, jack, 10, ...)
                        - a path   (the path to find the card's picture)
    """
    def __init__ (self, value: int, sprite_path: str):
        """
            create the card
        Args:
            value (int): the value of the card
            sprite_path (str): the file path to the cards sprite
        """
        self.value = value  
        if sprite_path is not None : # a card path can't be None except for the doctest because doctest doesn't support pygame
            self.surf = pygame.transform.smoothscale(pygame.image.load(sprite_path).convert_alpha(),(100,152)) # load the sprite and scale it down
        

    def __gt__(self, card: object) -> bool:
        """
            check if the current card is greater than the other card
        Args:
            card: (object) the other card
        Return:
            (bool) True if the value of the current card is greater than the other, 
                    False otherwise or if the object is not a Card
        
        >>> Card(7, None) > Card(6, None)
        True
        >>> Card(5, None) > Card(6, None)
        False
        >>> Card(12, None) > 4
        False
        >>> Card(12, None) > "Hi !"
        False
        """
        if not isinstance(card, Card):
            return False
        return self.value > card.value
        
    def __lt__(self, card: object) -> bool:
        """
            check if the current card is lower than the other card
        Args:
            card: (object) the other card
        Return:
            (bool) True if the value of the current card is lower than the other, 
                    False otherwise or if the object is not a Card
        
        >>> Card(7, None) < Card(6, None)
        False
        >>> Card(5, None) < Card(6, None)
        True
        >>> Card(12, None) > 4
        False
        >>> Card(12, None) > "Hi !"
        False
        """
        if not isinstance(card, Card):
            return False
        return self.value < card.value
    
    def __eq__(self, card: object) -> bool:
        """
            check if the current Card is equal than the other card
        Args:
            card: (object) the other card
        Return:
            (bool) True if the value of the current card is equal than the other, 
                    False otherwise or if the object is not a Card
        
        >>> Card(7, None) == Card(6,None)
        False
        >>> Card(5, None) == Card(5,None)
        True
        >>> Card(12, None) == 4
        False
        >>> Card(12, None) == "Hi !"
        False
        """
        if not isinstance(card, Card):
            return False
        return self.value == card.value

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
