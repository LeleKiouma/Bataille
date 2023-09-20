import pygame
from card import *
from player import *
from set_of_card import *
from time import sleep


def reveal_card(show_cards_int: int, cards_on_table: list) -> None:
    """
    test which card we need to print and print the card when there is a tie at the right to the current
    Args:
        show_cards_int (int): the int of if we need to show all the card or not
        cards_on_table (list): the list of all the card

    """
    for card_pos in range(len(cards_on_table[0])):  # all the card in the first player side
        if card_pos % 2 != 0:                       # if this card is an equality flipped card
            if show_cards_int ==  1:                # if the game is on the state we don't flip equality cards, we show their back
                screen.blit(card_back_surf, card_back_surf.get_rect(center=((225-25*card_pos), player1.y_pos_of_cards)))
            else:                                   # else, we show them
                screen.blit(cards_on_table[0][card_pos].surf, cards_on_table[0][card_pos].surf.get_rect(center=((225-25*card_pos), player1.y_pos_of_cards)))
        else:                                       # if this card is not an equality card we show it correctly
            screen.blit(cards_on_table[0][card_pos].surf, cards_on_table[0][card_pos].surf.get_rect(center=(350 + 15*card_pos, player1.y_pos_of_cards)))
    
    for card_pos in range(len(cards_on_table[1])):  # do the same thing for player 2
        if (card_pos % 2) != 0 :
            if show_cards_int ==  1 :
                screen.blit(card_back_surf, card_back_surf.get_rect(center=((225-25*card_pos), player2.y_pos_of_cards)))
            else :
                screen.blit(cards_on_table[1][card_pos].surf, cards_on_table[1][card_pos].surf.get_rect(center=((225-25*card_pos), player2.y_pos_of_cards)))
        else :
            screen.blit(cards_on_table[1][card_pos].surf, cards_on_table[1][card_pos].surf.get_rect(center=(350 + 15*card_pos, player2.y_pos_of_cards)))

    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player1.y_pos_of_reversed_card)))    # show the card reversed
    screen.blit(card_back_surf,card_back_surf.get_rect(center=(350,player2.y_pos_of_reversed_card)))    # for both players
    return 

def new_turn(player1: object, player2: object, cards_on_table: list) -> int:
    """
    add the next card to the correct list and return if someone have no card in his hand
    Args:
        player1 (object): the player 1
        player2 (object): the player 2
        cards_on_table (list): the list of cards on the card mat
    Return:
        (int) the winner of the round: 1 if player one wins, 2 if it's player two, 0 otherwise
    """
    card1 = player1.delete_card()       # remove the card from the deck of the players
    card2 = player2.delete_card()
    if card1 is not None:
        cards_on_table[0].append(card1) # add the card to the card that are on the card mat
        player1.update_score()          # and update the score
    else:
        return 2                        # player 1 has no card left: player 2 won
    
    if card2 is not None:
        cards_on_table[1].append(card2)
        player2.update_score()
    else :
        return 1                        # player 2 has no card left: player 1 won
    return 0                            # nobody won


pygame.init()                               # initialize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("Jeu de Bataille")   # set the title of the window

show_cards_int = 1              # 0 if we show all the card and see if someone wins,
                                # 1 if we show no card
                                # 2 if we show all the card but it's tie so we don't show the side-left one
who_win = 0                     # 1 if player 1 win the round,
                                # 2 if player 2 win the round,
                                # 0 if there no one winning yet
game_state = 0                  # 0 if no one already wins, 1 if player 1 wins, 2 if player 2 wins

font = pygame.font.Font("assets/police/FiraCode.ttf", 20)       # load a font of the game
big_font = pygame.font.Font("assets/police/FiraCode.ttf", 50)   # load another font of the game

background_surf = pygame.transform.smoothscale(pygame.image.load("assets/background/background.png").convert_alpha(), (700, 700)) # import and resize the background image
background_rect = background_surf.get_rect(center=(350, 350)) # set the location of the  background image

card_back_surf = pygame.transform.smoothscale(pygame.image.load("assets/deck_of_cards/card_back.png").convert_alpha(), (100, 152)) # import and resize the back of the card image

sentence_surf = font.render("Tirer une carte", False, (0, 0, 0))    # create the surf for the text in the button
sentence_rect = sentence_surf.get_rect(center=(550, 550))           # create the rect of the text in the button

player1 = Player(454, 614) # create the player 1
player2 = Player(246, 86)  # create the player 2

deck = Set_of_card()                # create all the card
deck.split_in_two(player1, player2) # split all the card in two, and distribute them

cards_on_table = [[],[]]    # cards_on_table[0] --> card of player 1 on the table,
                            # cards_on_table[1] --> card of player 2 on the table
                            
""" ####################### """
""" ###### MAIN LOOP ###### """
""" ####################### """
while game_state == 0:               # while nobody win the game
    for event in pygame.event.get(): # if we see any event
        if event.type == pygame.QUIT:# if the event is quitting pygame
            pygame.quit() # close pygame
            exit()        # stop the program
        elif event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked
            if (450 <= event.pos[0] and event.pos[0] <= 650) and (525 <= event.pos[1] and event.pos[1] <= 575): # the mouse is in the "flip card" button when clicked
                if show_cards_int == 1:     # if we were in the statement that we don't show any card
                    game_state = new_turn(player1,player2,cards_on_table) # we play a new round
                    if game_state != 0:     # if someone loose we restart the while true loop
                        continue            # the loop end
                    if cards_on_table[0][-1] > cards_on_table[1][-1]: # if the player 1 win
                        for i in range (2):
                            for card in cards_on_table[i]:
                                player1.add_card(card)  # add all the cards on te table to player 1's deck
                        show_cards_int = 0              # set to a statement we show all the card
                        who_win = 1                     # player 1 win the current round
                    elif cards_on_table[0][-1] < cards_on_table[1][-1]: # do the same but for the player 2
                        for i in range (2):
                            for card in cards_on_table[i] :
                                player2.add_card(card)
                        show_cards_int = 0
                        who_win = 2
                    else:                   # if it's a tie 
                        who_win = 0         # nobody wins
                        show_cards_int = 2  # set game state to tie
                elif show_cards_int == 0:   # if we were on the state who show card
                    for i in range(2) :
                        cards_on_table[i].clear() # clear all the card
                    show_cards_int = 1      # prepare the second round: - hide cards
                    who_win = 0             #                           - nobody won the next round
                else:
                    game_state = new_turn(player1, player2, cards_on_table) # new round (this card will be add at an even place on the deck list)
                    show_cards_int = 1
    
    screen.blit(background_surf, background_rect)               # draw the background image  
    pygame.draw.rect(screen, (0, 255, 0), (450, 525, 200, 50))  # draw the green rect
    screen.blit(sentence_surf, sentence_rect)                   # write the sentence in the green rect
    reveal_card(show_cards_int, cards_on_table) 
    
    """ this whole part is only about showing the score with the good color """
    if who_win == 1: # if the player 1 win we show his score in green and the player 2 in red
        player1_score_surf = font.render("Score: " + str(player1.score), False, (0, 255, 0))
        player1_score_rect = player1_score_surf.get_rect(center=(175, 614))
        player2_score_surf = font.render("Score: " + str(player2.score), False, (255, 0, 0))
        player2_score_rect = player2_score_surf.get_rect(center = (175,86))
    elif who_win == 2: # if the player 2  win we show his score in green and the player 1 in red
        player1_score_surf = font.render("Score: " + str(player1.score), False, (255, 0, 0))
        player1_score_rect = player1_score_surf.get_rect(center=(175, 614))
        player2_score_surf = font.render("Score : " + str(player2.score), False, (0, 255, 0))
        player2_score_rect = player2_score_surf.get_rect(center=(175, 86))
    else: # tie: show all the score in white
        player1_score_surf = font.render("Score : " + str(player1.score), False, (255, 255, 255))
        player1_score_rect = player1_score_surf.get_rect(center=(175, 614))
        player2_score_surf = font.render("Score: " + str(player2.score), False, (255, 255, 255))
        player2_score_rect = player2_score_surf.get_rect(center=(175, 86))
    
    screen.blit(player1_score_surf, player1_score_rect) # print the score on the screen
    screen.blit(player2_score_surf, player2_score_rect) # print the score on the screen

    pygame.display.flip() # refresh


""" ### SOMEONE WON ### """
screen.blit(background_surf, background_rect) # draw the background image
if game_state == 1: # if the player one win 
    win_sentences_surf = big_font.render("Le joueur 1 gagne !!!", False, (255, 255, 255))
    win_sentences_rect = win_sentences_surf.get_rect(center=(350, 150))
else:               # if the player two win
    win_sentences_surf = big_font.render("Le joueur 2 gagne !!!", False, (255, 255, 255))
    win_sentences_rect = win_sentences_surf.get_rect(center=(350, 150))
    
screen.blit(win_sentences_surf, win_sentences_rect)
pygame.display.flip() # refreshing the window with new element 
sleep(10)             # we wait ten seconds before the game ends
pygame.quit()         # stop pygame