
class Player() :
    """
    the class player with all the info we need about the player
    """

    def __init__(self, y_pos_of_cards: int, y_pos_of_reversed_card: int) :
        """
            initalize the constructor 
        Args:
            y_pos_of_cards (int): the y pos of the card when flipped
            y_pos_of_reversed_card (int): the y pos of the card when they are on the back
        """
        self.list_of_cards = []
        self.score = 0
        self.y_pos_of_cards = y_pos_of_cards
        self.y_pos_of_reversed_card = y_pos_of_reversed_card
    
    def add_card(self, card: object) :
        """
            add a card to the deck of the player
        Args:
            card (object): the card to add
        """
        self.list_of_cards.append(card)
        

    def update_score(self):
        """
            Update the score of a player by adding
            the value of all cards in his deck
        """
        self.score = 0
        for card in self.list_of_cards:
            self.score += card.value

    def delete_card(self,) :
        """
            delete the first card of the deck
        """
        print(self.list_of_cards[0])
        self.score -= self.list_of_cards[0].value
        return self.list_of_cards.pop(0)
    

    