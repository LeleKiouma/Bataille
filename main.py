import pygame
from card import *
from player import *
from set_of_card import *
from random import randint

def afficher_carte(show_cards_bool: bool,carte_sur_tapis:list):
    """
    test which card we need to print and print the card when there is a tie at the right to the current card
    Args:
        show_cards_bool (bool): the bool of if we need to show all the card of not
    """
    if show_cards_bool:
        screen.blit(carte_sur_tapis[0][-1].surf, carte_sur_tapis[0][-1].surf.get_rect(center=(350, player1.y_pos_of_cards)))
        screen.blit(carte_sur_tapis[1][-1].surf, carte_sur_tapis[1][-1].surf.get_rect(center=(350, player2.y_pos_of_cards)))
        if len(carte_sur_tapis[0]) > 1 :
            for card_pos in range(len(carte_sur_tapis[0])):
                if (card_pos % 2) != 0 :
                    screen.blit(carte_sur_tapis[0][card_pos].surf, carte_sur_tapis[0][card_pos].surf.get_rect(center=((225-25*card_pos), player1.y_pos_of_cards)))
            for card_pos in range(len(carte_sur_tapis[1])):
                    if (card_pos % 2) != 0 :
                        screen.blit(carte_sur_tapis[1][card_pos].surf, carte_sur_tapis[1][card_pos].surf.get_rect(center=((225-25*card_pos), player2.y_pos_of_cards)))
    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player1.y_pos_of_reversed_card)))
    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player2.y_pos_of_reversed_card)))

    return 

def nouveau_tour(player1: object, player2: object, carte_sur_tapis: list) :
    """
    ajoute les cartes dans la liste de carte face retournée et les enlèves de la liste apparetant au joueur puis actualise les score
    Args:
        player1 (object): player 1
        player2 (object): player 2
        carte_sur_tapis (list): list de carte sur le tapis
    """
    carte_sur_tapis[0].append(player1.delete_card())
    carte_sur_tapis[1].append(player2.delete_card())
    
    player1.update_score()
    player2.update_score()


pygame.init() #initalize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("bataille") # set the name 

show_cards_bool = False
player1_win = 0

font = pygame.font.Font("assets/police/FiraCode.ttf", 20) # load the font of the game

background_surf = pygame.transform.smoothscale(pygame.image.load("assets/background/background.png").convert_alpha(),(700,700)) #import and resizing the background image
background_rect = background_surf.get_rect(center = (350,350)) #set the location of the  background image

card_back_surf = pygame.transform.smoothscale(pygame.image.load("assets/deck_of_cards/card_back.png").convert_alpha(),(100,152))#import and resizing the backof the card image


sentence_surf = font.render("tirer la carte :",False,(0,0,0))
sentence_rect = sentence_surf.get_rect(center = (550,550 ))



player1 = Player(454,614) #create the player
player2 = Player(246,86) #create the player


jeux_de_carte = Set_of_card()
jeux_de_carte.split_in_two(player1,player2)

# carte_sur_tapis[0] --> carte du joueur 1, carte_sur_tapis[1] --> carte du joueur 2
carte_sur_tapis = [[],[]]

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked
            if (450 <= event.pos[0] and event.pos[0] <= 650) and (525 <= event.pos[1] and event.pos[1] <= 575) : # we look the mouse is in the rect
                if show_cards_bool == False :
                    nouveau_tour(player1,player2,carte_sur_tapis)
                    if carte_sur_tapis[0][-1] > carte_sur_tapis[1][-1] :
                        for i in range (2):
                            for card in carte_sur_tapis[i] :
                                player1.add_card(card)
                            
                        show_cards_bool = not show_cards_bool
                        player1_win = 1
                    elif carte_sur_tapis[0][-1] < carte_sur_tapis[1][-1] :
                        for i in range (2):
                            for card in carte_sur_tapis[i] :
                                player1.add_card(card)
                        show_cards_bool = not show_cards_bool
                        player1_win = 2
                    else :
                        for i in range (2):
                            nouveau_tour(player1,player2,carte_sur_tapis)
                        player1_win = 0
                else :
                    for i in range(2) :
                        carte_sur_tapis[i].clear()
                    show_cards_bool = not show_cards_bool
                    player1_win = 0
    screen.blit(background_surf,background_rect) #put the background image  
    pygame.draw.rect(screen,(0,255,0),(450,525,200,50)) #put the green rect
    screen.blit(sentence_surf,sentence_rect) #put the sentence in the green rect
    
    afficher_carte(show_cards_bool,carte_sur_tapis)
    
    if player1_win == 1 :
        player1_score_surf = font.render("score : "+str(player1.score),False,(0,255,0))
        player1_score_rect = player1_score_surf.get_rect(center = (175,614))
        
        player2_score_surf = font.render("score : "+str(player2.score),False,(255,0,0))
        player2_score_rect = player2_score_surf.get_rect(center = (175,86))
    elif player1_win== 2 :
        player1_score_surf = font.render("score : "+str(player1.score),False,(255,0,0))
        player1_score_rect = player1_score_surf.get_rect(center = (175,614))
        
        player2_score_surf = font.render("score : "+str(player2.score),False,(0,255,0))
        player2_score_rect = player2_score_surf.get_rect(center = (175,86))
    else :
        player1_score_surf = font.render("score : "+str(player1.score),False,(255,255,255))
        player1_score_rect = player1_score_surf.get_rect(center = (175,614))
        
        player2_score_surf = font.render("score : "+str(player2.score),False,(255,255,255))
        player2_score_rect = player2_score_surf.get_rect(center = (175,86))

    screen.blit(player1_score_surf,player1_score_rect)
    screen.blit(player2_score_surf,player2_score_rect)
    

    pygame.display.flip() #refreshing the window with new element 