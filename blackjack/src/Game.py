'''
The Game class contains all of the game's main logic and methods
This is the super class that gets imported into all others.
'''
class Game:

    def __init__(self):
        print('Game initialized')

    def game_win_logic(self, dealer_list, player_list):
        if self.return_total(dealer_list) > self.return_total(player_list):
            print('House wins')
            return True
        else:
            return False

    def return_total(self, lst):
        total = 0
        ace_count = 0
        for x in lst:
            if x == 'ace':
                ace_count += 1
            else:
                total += x
        for x in range(0, ace_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        return total

    def check_hand_total(self, lst):
        total = 0
        ace_count = 0
        for x in lst:
            if x == 'ace':
                ace_count += 1
            else:
                total += x
        for x in range(0, ace_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        if total <= 21:
            return True
        else:
            print('You\'re bust')
            return False
