import numpy as np

class Dice():

    def __init__(self, n_sides=6):
        pass

    def roll(self):
        pass

class Player():

    def __init__(self, name, dice=Dice()):
        '''
        ***Base Class For Human_Player and Computer_Player***
        Initialize a Game Player
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''
        pass

    def take_turn(self):
        raise ImplementationError("It looks like the method take_turn hasn't been Implemented for the Player Type: {}".format(type(self)))

    def win(self, tie=False):
        pass





class Human_Player(Player):

    def __init__(self, name, dice=Dice()):
        '''
        ***Inherits from Player class***
        Initialize a Human Player
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''
        pass

    def take_turn(self):
        pass

class Computer_Player(Player):

    def __init__(self, name, dice=Dice()):
        '''
        ***Inherits from Player class***
        Initialize a Computer Player
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''
        pass

    def take_turn(self):
        pass
