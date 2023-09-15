import pygame

TYPES = ("clubs",  "diamonds", "hearts", "spades")
VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14}

class Card(object) :
    """
    each card have a value and a sprite
    """
    def __init__ (self, value: int, sprite_pathing: str) :
        """
            create the card
        Args:
            value (int): the value of the card
            sprite_pathing (str): the file path to the cards sprite
        """
        self.value = value
        self.surf = pygame.transform.smoothscale(pygame.image.load(sprite_pathing).convert_alpha(),(100,152)) # load the sprite
        

    def __gt__(other: object)->bool:
        if self.value > card.value:
            return True
        return False
        
    def __lt__(other: object)->bool:
        if self.value < card.value:
            return True
        return False
    
    def __eq__(other: object)->bool:
        if self.value == card.value:
            return True
        return False


    


