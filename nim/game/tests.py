import random

class Board():

    def __init__(self, pile, stones):

        self._piles = pile
        self._stones = stones

    def to_string(self):

        _dash = 20
        _game_board = " "


        for i in range(_dash):
            _game_board += ("_ ")
        _game_board += "\n\n"

        x = 0
        for range in self._piles:
            _game_board  += (f"{x}: ")
            for range in self._stones:
                _game_board += "0 "

        _game_board += "\n"
        for i in range(_dash):
            _game_board += ("_ ")

        return _game_board

















# import random

# piles = { }
# for i in range(random.randint(2,5)):
#     piles[i] = random.randrange(2, 9)
    
# keys = list(piles.keys())
# test = keys[0]
# print(piles)
# print(test, end = ": ")
# print(piles[0])

# print()

# star = " "
# x = 0 
# def stones(number):
#     for range in number:
#         return "0 "

# for n in len(piles):
#     star += (f"{keys[x]}: {stones(str(x))} " )
#     x += 1
# print(star)


# # to_string function

# final_board = " "
# dash = 20

# for i in range(dash):
#     final_board += ("_ ")

# final_board += "\n\n"
# # print()

# row_num = range(0,len(piles))

# for n in row_num:
#     final_board +=(f"{n}: ")
#     stones_in_row = range(1, random.randint(2, 9))
#     for n in stones_in_row:
#         final_board += ("O " )
#     final_board += "\n"


# for i in range(dash):
#     final_board += ("_ ")

# print(final_board)




