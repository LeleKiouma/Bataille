class player() :
    def __init__(self) :
        self.list_of_cards = []
        self.score = 0
    
    def ajouter_carte(self,cartes) :
        self.list_of_cards.append(cartes)
        self.score += cartes.value