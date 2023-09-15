import cards.py

class set_of_card(object):

    def __init__(self):
        self.set_of_cards = [for type in cards.TYPE for value in cards.VALUES Card(value, "assets/set_of_cards/" + str(list(cards.VALUES.keys()) [list(cards.VALUES.values()).index(value)]))]
        for i in self.set_of_cards:
            print(i)