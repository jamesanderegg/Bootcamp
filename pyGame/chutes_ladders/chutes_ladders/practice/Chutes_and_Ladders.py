# external imports
import numpy as np

# local imports
from Player import Player, Human_Player, Computer_Player, Dice
from Board import Square, Chute, Ladder, Board

class Chutes_and_Ladders_Game():

    def __init__(self):
        '''
        Initialize Game:
        Collect human, computer player names
        Initialize Board
        Print board starting positions to console
        ***I decided to keep the __init__ and play_game methods intact to serve as a starting point***
        From here try to figure out how everything is called/ incorporated, then fill in the pieces
        '''
        print('Initializing Chutes and Ladders Game...')
        self.board = Board()

        self.players = list()
        self.n_humans = eval(input("How many (Human) Players Are Playing Today?"))

        for i in range(1,self.n_humans+1):
            player_name = input('Input Player {} Name: '.format(str(i)))
            self.players.append(Human_Player(name=player_name))


        self.n_computers = eval(input('How many Computer Players would you like?'))

        for i in range(1,self.n_computers+1):
            self.players.append(Computer_Player(name=str(i)))


        print('Successfully added: {} Human and {} Computer Players'.format(self.n_humans, self.n_computers))

        # start game
        self.play_game()

    def play_round(self):
        '''
        Runs through a single round:
        Within Each Round:
            Each player takes a turn
            Board position is referenced:
                if chute or ladder, adjusted
            Someone either wins or not
        '''
        pass

    def announce_winners(self):
        pass

    def play_game(self):
        '''
        Figured that I could keep this here as a starting place
        '''
        # track if game has been won yet, current turn
        self.won = False
        self.turn = 0

        while self.won==False:
            self.turn+=1
            print('Starting turn {} '.format(self.turn))
            print('Player positions:\n\t', '\n\t'.join(['{}: {}'.format(player.name, player.position) for player in self.players]))
            self.play_round()

        self.announce_winners()
        again = input('Press <ENTER> to play again?.. Or press anything else (then <ENTER>) to quit')
        if again == '':
            print('Starting New Game')
            self.reset_game()
            self.play_game()

    def reset_game(self):
        print('Reseting Pieces')
        pass
