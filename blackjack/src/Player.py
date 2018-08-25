'''
The player class defines the player object and all methods associated with the player.
It can perform actions such as holding a deck of cards and return its value on demand.
The other method here is to check the total number of chips remaining in hand.
'''


class Player():
    def __init__(self, chips, hand, bet):
        self.chips = chips
        self.hand = hand
        self.bet = bet
        self.bust = 0

    def win_bet(self):
        print('Congrats you won amount: {}' .format(self.bet * 2))
        self.chips += self.bet * 2

    def raise_bet(self, amount):
        if self.chips >= amount:
            print('Increasing bet amount by {}' .format(amount))
            self.chips -= amount
            self.bet += amount
        else:
            print('Insufficient balance to raise bet, only bet what you have')

    def lose_bet(self):
        if self.bet >= self.chips:
            print('Whoops you\'re out of chips')
            print ('Game over')
            exit(0)
        else:
            print('You lost your bet money: {}' .format(self.bet))
            self.chips -= self.bet
            self.bet = 0

    def check_total(self):
        print(self.chips)
        return

    def check_hand(self):
        print(self.hand)

'''
Dealer class for the blackjack game, has similar functions to
the player
'''

class Dealer():

    def __init__(self, hand):
        self.hand = hand
        print ('Dealer initialized with empty hand')

    def check_hand(self):
        print(self.hand)