from collections import defaultdict
import numpy as np

class Square():

    def __init__(self, position, last_square):
        '''
        Initialize Individual Board Game Squares
        '''
        pass

    def land_on(self, player):
        pass

    def board_end(self):
        pass

class Chute(Square):

    def __init__(self, position, end, last_square):
        pass

    def land_on(self,player):
        pass

    def board_end(self):
        pass

class Ladder(Square):

    def __init__(self, position, end, last_square):
        pass

    def land_on(self,player):
        pass

    def board_end(self):
        pass
class Board():

    def __init__(self, chutes='default', ladders='default', n_squares=100):
        '''
        Initialize Board Game
        Chutes: 'default' or Dictionary object of {position: slide end} for each chute
        Ladder: 'default' or Dictionary object of {position: climb end} for each Ladder
        Initializes Dictionary object of all squares belonging to the board
        '''
        # keeping this here so that you won't need to hard code slides
        if chutes == 'default':
            chutes = {16:6, 49:11, 47:26, 56:53, 64:60, 87:24, 93:73, 95:75, 98:78}
        if ladders == 'default':
            ladders = {1:38, 5:14, 9:31, 28:84, 40:42, 51:67, 71:91, 80:100}
        pass


    def reference_square(self, player, position):
        pass


    def wipe_board(self):
        pass

    def __str__(self):
        '''
        Implements print magic method for color formatting
        '''
        board_carry = list()
        # move through rows
        for row in range(1,11):
            row_top=list()
            row_middle=list()
            row_bottom=list()

            if row%2==1:
                row_start=((row-1)*10)+1
                for column in range(10):
                    position = row_start+column
                    # get inhabitants (if any)
                    inhabitants=list()
                    # first index
                    if len(self.square_inhabitants[position])>0:
                        inhabitants.append(self.square_inhabitants[position][0])
                    else:
                        inhabitants.append('')
                    # next index
                    if len(self.square_inhabitants[position])>1:
                        inhabitants.append(self.square_inhabitants[position][1])
                    else:
                        inhabitants.append('')


                    s_top = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(str(position)+' '*10)[:10])
                    row_top.append(s_top)
                    s_middle = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(inhabitants[0]+' '*10)[:10])
                    row_middle.append(s_middle)
                    s_bottom = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(inhabitants[1]+' '*10)[:10])
                    row_bottom.append(s_bottom)

            elif row%2==0:
                row_end=(row*10)
                for column in range(10):
                    position = row_end-column
                    # get inhabitants (if any)
                    inhabitants=list()
                    # first index
                    if len(self.square_inhabitants[position])>0:
                        inhabitants.append(self.square_inhabitants[position][0])
                    else:
                        inhabitants.append('')
                    # next index
                    if len(self.square_inhabitants[position])>1:
                        inhabitants.append(self.square_inhabitants[position][1])
                    else:
                        inhabitants.append('')


                    s_top = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(str(position)+' '*10)[:10])
                    row_top.append(s_top)
                    s_middle = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(inhabitants[0]+' '*10)[:10])
                    row_middle.append(s_middle)
                    s_bottom = self.base_str_format.format(style=self.cell_colors[self.squares[position].type], text=(inhabitants[1]+' '*10)[:10])
                    row_bottom.append(s_bottom)


            # push row to board
            full_row = '\n'.join([''.join([cell for cell in row_part]) for row_part in [row_top, row_middle, row_bottom]])
            board_carry.append(full_row)

        return '\n'.join([row for row in reversed(board_carry)])
        


if __name__ == '__main__':
    b=Board()
    print(b)
