import random

class Board():

    '''
    This class will make to game board and the updates as the game progresses. 

    '''
    def __init__(self):

        self._piles = []
        for i in range(0,random.randint(2,5)):
            n = random.randint(1,9)
            self._piles.append(n)

    def to_string(self):
        '''
        you need 20 dashes at top and bottom

        You need random rows between 2-5 and 1-9 random number of O's in each row.: 
        0: O O O O O
        1: O
        2: O O O O O O
        3: O O O O
        4: O O O O O O O O

        return the board
        '''
        dash = 20
        final_board = " "


        for i in range(dash):
            final_board += ("_ ")

        final_board +="\n\n"


        row_num = range(0, len(piles))

        for n in row_num:
            final_board += (f"{n}: ")
            stones_in_row = range(1,random.randint(2, 9))
            for n in stones_in_row:
                final_board += ("O ")
            final_board += "\n"


        for i in range(dash):
            final_board += ("_")

        return final_board

    def apply(self, move):
        '''
        this def tells what row and how many to remove. move will have two numbers the first is what row and the second is how many "O's" to remove. 
        
        '''
        pass

    def is_empty(self):

        '''
        this determens if the board is empty
        '''
        pass
