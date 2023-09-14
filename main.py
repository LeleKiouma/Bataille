import pygame
from cards import *

pygame.init() #initalize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("bataille") # set the name 
clock = pygame.time.Clock() 
help = True

list_of_cards = [
    (2,"ressource/cartes/2_of_clubs.png"),
    (2,"ressource/cartes/2_of_diamonds.png"),
    (2,"ressource/cartes/2_of_hearts.png"),
    (2,"ressource/cartes/2_of_spades.png"),
    
    (3,"ressource/cartes/3_of_clubs.png"),
    (3,"ressource/cartes/3_of_diamonds.png"),
    (3,"ressource/cartes/3_of_hearts.png"),
    (3,"ressource/cartes/3_of_spades.png"),
    
    (4,"ressource/cartes/4_of_clubs.png"),
    (4,"ressource/cartes/4_of_diamonds.png"),
    (4,"ressource/cartes/4_of_hearts.png"),
    (4,"ressource/cartes/4_of_spades.png"),
    
    (5,"ressource/cartes/5_of_clubs.png"),
    (5,"ressource/cartes/5_of_diamonds.png"),
    (5,"ressource/cartes/5_of_hearts.png"),
    (5,"ressource/cartes/5_of_spades.png"),
    
    (6,"ressource/cartes/6_of_clubs.png"),
    (6,"ressource/cartes/6_of_diamonds.png"),
    (6,"ressource/cartes/6_of_hearts.png"),
    (6,"ressource/cartes/6_of_spades.png"),
    
    (7,"ressource/cartes/7_of_clubs.png"),
    (7,"ressource/cartes/7_of_diamonds.png"),
    (7,"ressource/cartes/7_of_hearts.png"),
    (7,"ressource/cartes/7_of_spades.png"),
    
    (8,"ressource/cartes/8_of_clubs.png"),
    (8,"ressource/cartes/8_of_diamonds.png"),
    (8,"ressource/cartes/8_of_hearts.png"),
    (8,"ressource/cartes/8_of_spades.png"),
    
    (9,"ressource/cartes/9_of_clubs.png"),
    (9,"ressource/cartes/9_of_diamonds.png"),
    (9,"ressource/cartes/9_of_hearts.png"),
    (9,"ressource/cartes/9_of_spades.png"),
    
    (10,"ressource/cartes/10_of_clubs.png"),
    (10,"ressource/cartes/10_of_diamonds.png"),
    (10,"ressource/cartes/10_of_hearts.png"),
    (10,"ressource/cartes/10_of_spades.png"),
    
    (11,"ressource/cartes/jack_of_clubs.png"),
    (11,"ressource/cartes/jack_of_diamonds.png"),
    (11,"ressource/cartes/jack_of_hearts.png"),
    (11,"ressource/cartes/jack_of_spades.png"),
    
    (12,"ressource/cartes/queen_of_clubs.png"),
    (12,"ressource/cartes/queen_of_diamonds.png"),
    (12,"ressource/cartes/queen_of_hearts.png"),
    (12,"ressource/cartes/queen_of_spades.png"),
    
    (13,"ressource/cartes/king_of_clubs.png"),
    (13,"ressource/cartes/king_of_diamonds.png"),
    (13,"ressource/cartes/king_of_hearts.png"),
    (13,"ressource/cartes/king_of_spades.png"),
    
    (14,"ressource/cartes/ace_of_clubs.png"),
    (14,"ressource/cartes/ace_of_diamonds.png"),
    (14,"ressource/cartes/ace_of_hearts.png"),
    (14,"ressource/cartes/ace_of_spades.png"),
    
]
background_surf = pygame.transform.smoothscale(pygame.image.load("ressource/background/background.png").convert_alpha(),(700,700))
background_rect = background_surf.get_rect(center = (350,350))

card_back_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/card_back.png").convert_alpha(),(100,152))
card_back_rect = card_back_surf.get_rect(center = (350,624))

list_of_object = []

for element in list_of_cards :
    list_of_object.append(cards(element[0],element[1]))





while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_surf,background_rect)
    screen.blit(list_of_object[0].sprite,list_of_object[0].sprite.get_rect(center = (350,350)))
    screen.blit(card_back_surf,card_back_rect)
    pygame.display.flip() #refreshing the window with new element 