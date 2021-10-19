import random

piles = []
for i in range(0,random.randint(2,5)):
    n = random.randint(1,9)
    piles.append(n)

print(len(piles))



# to_string function

final_board = " "
dash = 20

for i in range(dash):
    final_board += ("_", end = " ") + "\n\n"

# print()
# print()

row_num = range(0,len(piles))

for n in row_num:
    final_board +=(f"{n}: ", end = "")
    stones_in_row = range(2,piles[n])
    for n in stones_in_row:
        final_board += ("O ", end = "" ) + "\n"
    print()


for i in range(dash):
    final_board += ("_", end = " ")

print(final)


