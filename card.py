import pygame


TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
JACK = 11
QUEEN = 12
KING = 13
ACE = 14

TYPES = ("clubs",  "diamonds", "hearts", "spades")
VALUES = {"2": TWO, "3": THREE, "4": FOUR, "5": FIVE, "6": SIX, "7": SEVEN, "8": EIGHT, "9": NINE, "10": TEN, "jack": JACK, "queen": QUEEN, "king": king, "ace": ACE}

class card(object) :
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
        self.surf = pygame.transform.smoothscale(pygame.image.load(sprite_pathing).convert_alpha(),(100,152))


    def __str__(self)->str:
        return self.value