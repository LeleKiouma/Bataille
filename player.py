from card import *

class Player() :
    """
        The player has: - a list of cards (his deck)
                        - a score (the value of his deck)
                        - a position to draw the card on the screen
                        - a position to draw the reversed card on the screen
    """

    def __init__(self, y_pos_of_cards: int, y_pos_of_reversed_card: int):
        """
            initialize the constructor 
        Args:
            y_pos_of_cards (int): the y pos of the card when they're flipped
            y_pos_of_reversed_card (int): the y pos of the card when they are on the back
        """
        self.list_of_cards = []
        self.score = 0
        self.y_pos_of_cards = y_pos_of_cards
        self.y_pos_of_reversed_card = y_pos_of_reversed_card
    
    def add_card(self, card: object) -> None:
        """
            add a card to the deck of the player
        Args:
            card (object): the card to add
        """
        if isinstance(card, Card):
            self.list_of_cards.append(card)
        

    def update_score(self) -> None:
        """
            Update the score of a player by adding
            the value all cards in his deck
        """
        self.score = 0
        for card in self.list_of_cards:
            self.score += card.value

    def delete_card(self) -> object:
        """
            delete the first card of the deck and return this card
            Return:
                (object) the card that has been delete or None
        """
        if len(self.list_of_cards) != 0 :
            self.score -= self.list_of_cards[0].value
            return self.list_of_cards.pop(0)
        return None