import pygame
from card import *
from player import *
from set_of_card import *

def reveal_card(show_cards_int: int,cards_on_table:list):
    """
    test which card we need to print and print the card when there is a tie at the right to the current
    Args:
        show_cards_int (int): the int of if we need to show all the card or not
        cards_on_table (list): the list of all the card

    """
    for card_pos in range(len(cards_on_table[0])): #all the card in the player1 side
        if (card_pos % 2) != 0 : # if this card is an equality flipped card
            if show_cards_int ==  1 : #if the game is on the state we don't flip equality cards
                screen.blit(card_back_surf, card_back_surf.get_rect(center=((225-25*card_pos), player1.y_pos_of_cards)))
            else :
                screen.blit(cards_on_table[0][card_pos].surf, cards_on_table[0][card_pos].surf.get_rect(center=((225-25*card_pos), player1.y_pos_of_cards)))
        else :#if this card is not an equality card we show it correctly
            screen.blit(cards_on_table[0][card_pos].surf, cards_on_table[0][card_pos].surf.get_rect(center=(350 + 15*card_pos, player1.y_pos_of_cards)))
    
    for card_pos in range(len(cards_on_table[1])): #do the exact same thing but for player 2
        if (card_pos % 2) != 0 :
            if show_cards_int ==  1 :
                screen.blit(card_back_surf, card_back_surf.get_rect(center=((225-25*card_pos), player2.y_pos_of_cards)))
            else :
                screen.blit(cards_on_table[1][card_pos].surf, cards_on_table[1][card_pos].surf.get_rect(center=((225-25*card_pos), player2.y_pos_of_cards)))
        else :
            screen.blit(cards_on_table[1][card_pos].surf, cards_on_table[1][card_pos].surf.get_rect(center=(350 + 15*card_pos, player2.y_pos_of_cards)))

    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player1.y_pos_of_reversed_card))) 
    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player2.y_pos_of_reversed_card)))

    return 

def new_turn(player1: object, player2: object, cards_on_table: list) :
    """
    add the next card to the correct list and return if someone have no card in his hand
        player1 (object): player 1
        player2 (object): player 2
        cards_on_table (list): list de carte sur le tapis
    """
    carte1 = player1.delete_card()
    carte2 = player2.delete_card()
    if carte1 is not None :
        cards_on_table[0].append(carte1)
        player1.update_score()
    else :
        return 2
    
    if carte2 is not None :
        cards_on_table[1].append(carte2)
        player2.update_score()
    else :
        return 1
        
    return 0


pygame.init() #initalize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("bataille") # set the name 

show_cards_int = 1 #0 if we show all the card and see if seomeone win,1 if we show no card, 2 if we show all the card but it's tie so we don't show the side-left one
who_win = 0 #1 if player 1 win the round, 2 if player 2 win the round,0 if there no one winning yet. used to color correctly the score
game_state = 0 #0 if no win already , 1 if player 1 win , 2 if player 2 win

font = pygame.font.Font("assets/police/FiraCode.ttf", 20) # load the font of the game
big_font = pygame.font.Font("assets/police/FiraCode.ttf", 50) # load the font of the game but with a bigger police

background_surf = pygame.transform.smoothscale(pygame.image.load("assets/background/background.png").convert_alpha(),(700,700)) #import and resizing the background image
background_rect = background_surf.get_rect(center = (350,350)) #set the location of the  background image

card_back_surf = pygame.transform.smoothscale(pygame.image.load("assets/deck_of_cards/card_back.png").convert_alpha(),(100,152)) #import and resizing the back of the card image

sentence_surf = font.render("tirer la carte :",False,(0,0,0)) #create the surf for the text in the button
sentence_rect = sentence_surf.get_rect(center = (550,550 )) #create the rect of the text in the button

play_again_sentence_surf = font.render("to play again press any key",False,(255,255,255))
play_again_sentence_rect = play_again_sentence_surf.get_rect(center = (350,400))



player1 = Player(454,614) #create the player
player2 = Player(246,86) #create the player

jeux_de_carte = Set_of_card() #create all the card
#jeux_de_carte.split_in_two(player1,player2) 
player1.add_card(Card(2,"assets/deck_of_cards/5_of_spades.png"))
player2.add_card(Card(1,"assets/deck_of_cards/5_of_spades.png"))

# cards_on_table[0] --> card of player 1 on the table, cards_on_table[1] --> card of player 2 on the table
cards_on_table = [[],[]]

while True :
    if game_state == 0 : # if no player win yet
        for event in pygame.event.get(): # if we see any event
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked
                if (450 <= event.pos[0] and event.pos[0] <= 650) and (525 <= event.pos[1] and event.pos[1] <= 575) : #  the mouse is in the "flip card" button when clicked
                    if show_cards_int == 1 : 
                        game_state = new_turn(player1,player2,cards_on_table)
                        if game_state != 0 : #if someone loose we restart the while true loop
                            continue
                        if cards_on_table[0][-1] > cards_on_table[1][-1] : #if the player win
                            for i in range (2):
                                for card in cards_on_table[i] :
                                    player1.add_card(card) #add all the card on te table to the player1's deck
                            show_cards_int = 0 
                            who_win = 1
                        elif cards_on_table[0][-1] < cards_on_table[1][-1] : #do the same but for the player 2
                            for i in range (2):
                                for card in cards_on_table[i] :
                                    player2.add_card(card)
                            show_cards_int = 0
                            who_win = 2
                        else : #it's a tie 
                            who_win = 0
                            show_cards_int = 2
                    elif show_cards_int == 0 : 
                        for i in range(2) :
                            cards_on_table[i].clear()
                        show_cards_int = 1
                        who_win = 0
                    else :
                        game_state = new_turn(player1,player2,cards_on_table) #flip on card (this one will at an even place on the deck list)
                        show_cards_int = 1
        
        screen.blit(background_surf,background_rect) #put the background image  
        pygame.draw.rect(screen,(0,255,0),(450,525,200,50)) #put the green rect
        screen.blit(sentence_surf,sentence_rect) #put the sentence in the green rect
        reveal_card(show_cards_int,cards_on_table) 
        
        #this whole part is only about showing the score with the good color
        if who_win == 1 : 
            player1_score_surf = font.render("score : "+str(player1.score),False,(0,255,0))
            player1_score_rect = player1_score_surf.get_rect(center = (175,614))
            
            player2_score_surf = font.render("score : "+str(player2.score),False,(255,0,0))
            player2_score_rect = player2_score_surf.get_rect(center = (175,86))
        elif who_win== 2 :
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
        

    else :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN :
                #reset all the variable 
                jeux_de_carte.split_in_two(player1,player2) 
                show_cards_int = 0
                who_win = 0
                game_state = 0
                cards_on_table[0],cards_on_table[1] = [],[] #clear the list of the cards on table
        screen.blit(background_surf,background_rect) #put the background image
        if game_state == 1 :
            win_sentences_surf = big_font.render("player 1 win !!!",False,(255,255,255))
            win_sentences_rect = win_sentences_surf.get_rect(center = (350,150))
        else :
            win_sentences_surf = big_font.render("player 2 win !!!",False,(255,255,255))
            win_sentences_rect = win_sentences_surf.get_rect(center = (350,150))
            
        screen.blit(win_sentences_surf,win_sentences_rect)
        screen.blit(play_again_sentence_surf,play_again_sentence_rect)

    pygame.display.flip() #refreshing the window with new element 