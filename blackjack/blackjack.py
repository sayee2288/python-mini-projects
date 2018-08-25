from src.Player import *
from src.Deck import Deck
from src.Game import Game

print('\n' * 10)
print('Welcome to the Casino Royale\'s high roller blackjack table, '
      'please enter your starting chip amount!')

try:
    chips = int(input('Chips: '))
except ValueError:
    print('You have crashed the game bad boy')
    exit(1)

my_player = Player(chips, [], 0)
my_deck = Deck()
my_dealer = Dealer([])
game = Game()
who = 0
play_again = True
game_options = {
    1: 'Raise Bet',
    2: 'Hit me',
    3: 'Stop',
    4: 'Check_hand',
    5: 'Check total chips',
    6: 'Cash out'
}

while play_again:

    while who < 1:
        option = int(input('Player - Choose your action {}: \n' .format(game_options)))
        if option == 1:
            my_player.raise_bet(int(input(
                'Enter bet amount please'
            )))
        elif option == 2:
            print('Player is picking a card from the deck')
            a, b = my_deck.pick_card()
            my_player.hand.append(a)
            if game.check_hand_total(my_player.hand):
                continue
            else:
                my_player.bust = 1
                break
        elif option == 3:
            break
        elif option == 4:
            my_player.check_hand()
        elif option == 5:
            my_player.check_total()
        elif option == 6:
            play_again = False
            print('Thank you for playing, you have {} chips left' .format(my_player.chips))
            exit(0)

    if my_player.bust == 0:
        while game.check_hand_total(my_dealer.hand):
            print('Dealer is picking a card from the deck')
            a, b = my_deck.pick_card()
            my_dealer.hand.append(a)
            if game.check_hand_total(my_dealer.hand):
                if game.game_win_logic(my_dealer.hand, my_player.hand):
                    break
                else:
                    continue
            else:
                print('player wins!')
                my_player.win_bet()
                break
        else:
            my_player.lose_bet()

    my_deck.shuffle()
    my_player.hand = []
    my_dealer.hand = []
    my_player.bet = 0