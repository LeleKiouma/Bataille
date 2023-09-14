import pygame

class cards () :
    """
    each card have a value and a sprite
    """
    def __init__ (self,value : int,sprite_pathing : str) :
        """
            create the card
        Args:
            value (int): the value of the card
            sprite_pathing (str): the file path to the cards sprite
        """
        self.value = value
        self.surf = pygame.transform.smoothscale(pygame.image.load(sprite_pathing).convert_alpha(),(100,152))
