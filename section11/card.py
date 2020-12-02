import random
suits = ('Hearts' , 'Diamonds' , 'Spades' , 'Clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten',
'jack','queen','king','ace')
values=  {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
'jack':11,'queen':12,'king':13,'ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank +" of "+self.suit

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)
                # print(created_card)
                self.all_cards.append(created_card)

    def shuffle(self):
            random.shuffle(self.all_cards)

    def deal_one(self):
            return self.all_cards.pop()

class Player:
    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'



if __name__ == '__main__':
    new_deck = Deck()
    new_deck.shuffle()
    my_card = new_deck.deal_one()

    new_player = Player('Jak')
    new_player.add_cards(my_card)
    print(new_player)
    '''
    new_player.add_cards([my_card,my_card,my_card,my_card])
    print(new_player)
    print(new_player.all_cards[0])
    '''
