import pygame

class cards () :
    def __init__ (self,value,sprite_chemin,) :
        self.value = value
        self.sprite = pygame.transform.smoothscale(pygame.image.load(sprite_chemin).convert_alpha(),(100,152))
