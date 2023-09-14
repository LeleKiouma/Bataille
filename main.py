import pygame
from cards import *
from player import *
import random 

def create_game(list_of_cards:list,player1:object,player2:object) :
    """
    recreate the game variable to a correct state
    Args:
        list_of_cards (list): list of all the cards path and value
        player1 (object): player1 object
        player2 (object): player2 object
    """
    player1.list_of_cards.clear()
    player2.list_of_cards.clear()
    random_bool = bool(random.getrandbits(1)) #create a random bool 
    for element in list_of_cards :
        if random_bool == True :
            player1.ajouter_carte(cards(element[0],element[1]))
            random_bool = not random_bool 
        else :
            player2.ajouter_carte(cards(element[0],element[1]))
            random_bool = not random_bool
    player1.melanger_cartes() 
    player2.melanger_cartes()

def afficher_carte(show_cards_bool:bool):
    """
    test which card we need to print
    Args:
        show_cards_bool (bool): the bool of if we need to show all the card of not
    """
    if show_cards_bool:
        screen.blit(player1.list_of_cards[0].surf , player1.list_of_cards[0].surf.get_rect(center = (350,player1.y_pos_of_cards)))
        screen.blit(player2.list_of_cards[0].surf , player2.list_of_cards[0].surf.get_rect(center = (350,player2.y_pos_of_cards)))
    
    screen.blit(card_back_surf,card_back_surf.get_rect(center = (350,player1.y_pos_of_reversed_card)))
    screen.blit(card_back_surf,card_back_surf.get_rect(center = (350,player2.y_pos_of_reversed_card)))

def comparer_cartes(player1:bool,player2:bool):
    """
    look for who win the 1v1
    Args:
        player1 (bool): the player 1 object
        player2 (bool): the player 1 object
    """
    if player1.list_of_cards[0].value > player2.list_of_cards[0].value :
        player1.ajouter_carte(player2.list_of_cards[0])
        player2.supprimer_cartes
    elif player1.list_of_cards[0].value < player2.list_of_cards[0].value :
        player2.ajouter_carte(player1.list_of_cards[0])
        player1.supprimer_cartes
    else :
        return False
    return True

pygame.init() #initalize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("bataille") # set the name 

show_cards_bool = False

font = pygame.font.Font("ressource/police/FiraCode.ttf", 20) # load the font of the game


list_of_cards = [ #the whole list of card file path
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
background_surf = pygame.transform.smoothscale(pygame.image.load("ressource/background/background.png").convert_alpha(),(700,700)) #import and resizing the background image
background_rect = background_surf.get_rect(center = (350,350)) #set the location of the  background image

card_back_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/card_back.png").convert_alpha(),(100,152))#import and resizing the backof the card image


sentence_surf = font.render("tirer la carte :",False,(0,0,0))
sentence_rect = sentence_surf.get_rect(center = (550,550 ))



player1 = Player(454,614) #create the player
player2 = Player(246,86) #create the player

create_game(list_of_cards,player1,player2)


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked
            if (450 <= event.pos[0] and event.pos[0] <= 650) and (525 <= event.pos[1] and event.pos[1] <= 575) : # we look the mouse is in the rect                #if show_cards_bool == True :
                    #if comparer_cartes(player1,player2) == false:
                        #a completer
                show_cards_bool = not show_cards_bool
                
                
    screen.blit(background_surf,background_rect) #put the background image  
    pygame.draw.rect(screen,(0,255,0),(450,525,200,50)) #put the green rect
    screen.blit(sentence_surf,sentence_rect) #put the sentence in the green rect
    
    afficher_carte(show_cards_bool)
    
    pygame.display.flip() #refreshing the window with new element 