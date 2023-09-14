import pygame
import math

pygame.init() #initalize pygame 
screen = pygame.display.set_mode((700,700)) # set the size of the window
pygame.display.set_caption("bataille") # set the name 
clock = pygame.time.Clock() 
help = True


two_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/2_of_clubs.png").convert_alpha(),(100,100))
two_of_clubs_rect = two_of_clubs_surf.get_rect(center = (350,350))
two_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/2_of_diamonds.png").convert_alpha(),(100,100))
two_of_diamonds_rect = two_of_diamonds_surf.get_rect(center = (350,350))
two_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/2_of_hearts.png").convert_alpha(),(100,100))
two_of_hearts_rect = two_of_hearts_surf.get_rect(center = (350,350))
two_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/2_of_spades.png").convert_alpha(),(100,100))
two_of_spades_rect = two_of_spades_surf.get_rect(center = (350,350))


three_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/3_of_clubs.png").convert_alpha(),(100,100))
three_of_clubs_rect = three_of_clubs_surf.get_rect(center = (350,350))
three_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/3_of_diamonds.png").convert_alpha(),(100,100))
three_of_diamonds_rect = three_of_diamonds_surf.get_rect(center = (350,350))
three_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/3_of_hearts.png").convert_alpha(),(100,100))
three_of_hearts_rect = three_of_hearts_surf.get_rect(center = (350,350))
three_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/3_of_spades.png").convert_alpha(),(100,100))
three_of_hearts_rect = three_of_spades_surf.get_rect(center = (350,350))

four_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/4_of_clubs.png").convert_alpha(),(100,100))
four_of_clubs_rect = four_of_clubs_surf.get_rect(center = (350,350))
four_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/4_of_diamonds.png").convert_alpha(),(100,100))
four_of_diamonds_rect = four_of_diamonds_surf.get_rect(center = (350,350))
four_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/4_of_hearts.png").convert_alpha(),(100,100))
four_of_hearts_rect = four_of_hearts_surf.get_rect(center = (350,350))
four_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/4_of_spades.png").convert_alpha(),(100,100))
four_of_hearts_rect = four_of_spades_surf.get_rect(center = (350,350))

five_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/5_of_clubs.png").convert_alpha(),(100,100))
five_of_clubs_rect = five_of_clubs_surf.get_rect(center = (350,350))
five_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/5_of_diamonds.png").convert_alpha(),(100,100))
five_of_diamonds_rect = five_of_diamonds_surf.get_rect(center = (350,350))
five_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/5_of_hearts.png").convert_alpha(),(100,100))
five_of_hearts_rect = five_of_hearts_surf.get_rect(center = (350,350))
five_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/5_of_spades.png").convert_alpha(),(100,100))
five_of_hearts_rect = five_of_spades_surf.get_rect(center = (350,350))

six_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/6_of_clubs.png").convert_alpha(),(100,100))
six_of_clubs_rect = six_of_clubs_surf.get_rect(center = (350,350))
six_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/6_of_diamonds.png").convert_alpha(),(100,100))
six_of_diamonds_rect = six_of_diamonds_surf.get_rect(center = (350,350))
six_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/6_of_hearts.png").convert_alpha(),(100,100))
six_of_hearts_rect = six_of_hearts_surf.get_rect(center = (350,350))
six_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/6_of_spades.png").convert_alpha(),(100,100))
six_of_hearts_rect = six_of_spades_surf.get_rect(center = (350,350))

seven_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/7_of_clubs.png").convert_alpha(),(100,100))
seven_of_clubs_rect = seven_of_clubs_surf.get_rect(center = (350,350))
seven_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/7_of_diamonds.png").convert_alpha(),(100,100))
seven_of_diamonds_rect = seven_of_diamonds_surf.get_rect(center = (350,350))
seven_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/7_of_hearts.png").convert_alpha(),(100,100))
seven_of_hearts_rect = seven_of_hearts_surf.get_rect(center = (350,350))
seven_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/7_of_spades.png").convert_alpha(),(100,100))
seven_of_hearts_rect = seven_of_spades_surf.get_rect(center = (350,350))

height_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/8_of_clubs.png").convert_alpha(),(100,100))
height_of_clubs_rect = height_of_clubs_surf.get_rect(center = (350,350))
height_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/8_of_diamonds.png").convert_alpha(),(100,100))
height_of_diamonds_rect = height_of_diamonds_surf.get_rect(center = (350,350))
height_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/8_of_hearts.png").convert_alpha(),(100,100))
height_of_hearts_rect = height_of_hearts_surf.get_rect(center = (350,350))
height_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/8_of_spades.png").convert_alpha(),(100,100))
height_of_hearts_rect = height_of_spades_surf.get_rect(center = (350,350))

nine_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/9_of_clubs.png").convert_alpha(),(100,100))
nine_of_clubs_rect = nine_of_clubs_surf.get_rect(center = (350,350))
nine_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/9_of_diamonds.png").convert_alpha(),(100,100))
nine_of_diamonds_rect = nine_of_diamonds_surf.get_rect(center = (350,350))
nine_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/9_of_hearts.png").convert_alpha(),(100,100))
nine_of_hearts_rect = nine_of_hearts_surf.get_rect(center = (350,350))
nine_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/9_of_spades.png").convert_alpha(),(100,100))
nine_of_hearts_rect = nine_of_spades_surf.get_rect(center = (350,350))

ten_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/10_of_clubs.png").convert_alpha(),(100,100))
ten_of_clubs_rect = ten_of_clubs_surf.get_rect(center = (350,350))
ten_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/10_of_diamonds.png").convert_alpha(),(100,100))
ten_of_diamonds_rect = ten_of_diamonds_surf.get_rect(center = (350,350))
ten_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/10_of_hearts.png").convert_alpha(),(100,100))
ten_of_hearts_rect = ten_of_hearts_surf.get_rect(center = (350,350))
ten_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/10_of_spades.png").convert_alpha(),(100,100))
ten_of_hearts_rect = ten_of_spades_surf.get_rect(center = (350,350))

ace_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/ace_of_clubs.png").convert_alpha(),(100,100))
ace_of_clubs_rect = ace_of_clubs_surf.get_rect(center = (350,350))
ace_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/ace_of_diamonds.png").convert_alpha(),(100,100))
ace_of_diamonds_rect = ace_of_diamonds_surf.get_rect(center = (350,350))
ace_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/ace_of_hearts.png").convert_alpha(),(100,100))
ace_of_hearts_rect = ace_of_hearts_surf.get_rect(center = (350,350))
ace_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/ace_of_spades.png").convert_alpha(),(100,100))
ace_of_hearts_rect = ace_of_spades_surf.get_rect(center = (350,350))

jack_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/jack_of_clubs.png").convert_alpha(),(100,100))
jack_of_clubs_rect = jack_of_clubs_surf.get_rect(center = (350,350))
jack_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/jack_of_diamonds.png").convert_alpha(),(100,100))
jack_of_diamonds_rect = jack_of_diamonds_surf.get_rect(center = (350,350))
jack_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/jack_of_hearts.png").convert_alpha(),(100,100))
jack_of_hearts_rect = jack_of_hearts_surf.get_rect(center = (350,350))
jack_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/jack_of_spades.png").convert_alpha(),(100,100))
jack_of_hearts_rect = jack_of_spades_surf.get_rect(center = (350,350))


queen_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/queen_of_clubs.png").convert_alpha(),(100,100))
queen_of_clubs_rect = queen_of_clubs_surf.get_rect(center = (350,350))
queen_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/queen_of_diamonds.png").convert_alpha(),(100,100))
queen_of_diamonds_rect = queen_of_diamonds_surf.get_rect(center = (350,350))
queen_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/queen_of_hearts.png").convert_alpha(),(100,100))
queen_of_hearts_rect = queen_of_hearts_surf.get_rect(center = (350,350))
queen_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/queen_of_spades.png").convert_alpha(),(100,100))
queen_of_hearts_rect = queen_of_spades_surf.get_rect(center = (350,350))

king_of_clubs_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/king_of_clubs.png").convert_alpha(),(100,100))
king_of_clubs_rect = king_of_clubs_surf.get_rect(center = (350,350))
king_of_diamonds_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/king_of_diamonds.png").convert_alpha(),(100,100))
king_of_diamonds_rect = king_of_diamonds_surf.get_rect(center = (350,350))
king_of_hearts_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/king_of_hearts.png").convert_alpha(),(100,100))
king_of_hearts_rect = king_of_hearts_surf.get_rect(center = (350,350))
king_of_spades_surf = pygame.transform.smoothscale(pygame.image.load("ressource/cartes/king_of_spades.png").convert_alpha(),(100,100))
king_of_hearts_rect = king_of_spades_surf.get_rect(center = (350,350))



while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(two_of_clubs_surf,two_of_clubs_rect)
    pygame.display.flip() #refreshing the window with new element 