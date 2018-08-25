'''
The deck class simulates a deck of cards and
returns one card back to the player or the dealer randomly.
'''
import random

class Deck:
    '''
    The deck class creates the cards
    and has functions to return a card or shuffle all cards
    '''

    def __init__(self):
        print('Deck is ready for the game')
        self.card = ''
        self.shape = ''
        self.deck = {
            0: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace'],
            1: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace'],
            2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace'],
            3: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'ace']
            }
        self.suit = {
            0: 'Spades',
            1: 'Hearts',
            2: 'clubs',
            3: 'diamonds'
        }

    def pick_card(self):
        while True:
            a = random.randint(0, 3)
            b = random.randint(0, len(self.deck[a])-1)
            self.card = self.deck[a][b]
            if self.card in self.deck[a]:
                del self.deck[a][b]
                break
            else:
                continue

        print('You retrieved this card: {} of {}' .format(self.card, self.suit[a]))
        return self.card, self.suit[a]

    def shuffle(self):
        print('Deck has been shuffled')
        self.__init__()


if __name__ == "__main__":
    my_deck = Deck()
    my_deck.pick_card()


