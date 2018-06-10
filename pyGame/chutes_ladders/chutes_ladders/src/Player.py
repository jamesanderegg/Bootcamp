import numpy as np

class Dice():

    def __init__(self, n_sides=6):
        self.n_sides = n_sides

    def roll(self):
        return np.random.randint(1,self.n_sides)


class Player():

    def __init__(self, name, dice=Dice()):
        '''
        Initialize a Game Player
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''

        self.name = name
        # starting at 0
        self.position = 0
        # init dice object
        self.dice=dice
        self.won=False
        self.victories=0

    def take_turn(self):
        raise ImplementationError("It looks like the method take_turn hasn't been Implemented for the Player Type: {}".format(type(self)))

    def win(self, tie=False):
        if not tie:
            print("Congratulations {}, You've won the Game!".format(self.name))
            self.victories+=1
            print('{} win count: {}'.format(self.name, self.victories))
        elif tie:
            print("Congratulations {}, You've tied for the win!".format(self.name))
            self.victories+=1
            print('{} win count: {}'.format(self.name, self.victories))





class Human_Player(Player):

    def __init__(self, name, dice=Dice()):
        '''
        Initialize a Human Player
        Inherits from Player class
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''

        self.name = name
        # starting at 0
        self.position = 0
        # init dice object
        self.dice=dice
        self.won=False
        self.victories=0

    def take_turn(self):
        input("{}'s Turn, Press <ENTER> to Roll".format(self.name))
        roll = self.dice.roll()
        print('You rolled a {}'.format(roll))
        return roll


class Computer_Player(Player):

    def __init__(self, name, dice=Dice()):
        '''
        Initialize a Computer Player
        Inherits from Player class
        Players have a: Dice, name, position
        Players can: take_turn (roll dice, return roll)
        '''

        self.name = 'Computer_'+name
        # starting at 0
        self.position = 0
        # init dice object
        self.dice=dice
        self.won=False
        self.victories=0

    def take_turn(self):
        print("{}'s Turn\n".format(self.name))
        roll = self.dice.roll()
        print("\t{} Rolls a {}".format(self.name,roll))
        return roll
