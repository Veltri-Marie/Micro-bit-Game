import math
import random

import radio
import microbit

# definition of functions
def get_message():
    """Wait and return a message from another micro:bit.

    Returns
    -------
    message: message sent by another micro:bit (str)

    """

    message = None
    while message == None:
        microbit.sleep(250)
        message = radio.receive()

    return message


def board_microbit(board, player_x, player_y, cat_x, cat_y):
    """
    Parameters
    ----------
    Board: The board of the game with the player, the cat and the rocks(list)
    player_x : the x position of the player (int)
    player_y : the y position of the player (int)
    cat_x : the x position of the cat (int)
    cat_y : the y position of the cat (int)

    Returns
    -------
    box_player: The coordinates of the player (int)
    """

    box_player = ""
    for y in range(player_y - 2, player_y + 3):
        for x in range(player_x - 2, player_x + 3):
            if player_x == x and player_y == y:
                box_player += "P"
            elif cat_x == x and cat_y == y:
                box_player += "C"
            else:
                box_player += board[y][x]

    return box_player


# settings
group_id = 29
size = 100

# setup radio to receive/send messages
radio.on()
radio.config(group=group_id)

# create board and place cat + player

board = []

x = 10
y = 10

for i in range(y):
    board.append(["O"] * x)

for i in range(0, x):
    wall_x = random.randint(3, x - 3)
    wall_y = random.randint(3, y - 3)
    board[wall_y][wall_x] = "W"


for i in range(1, x - 1):
    # x axis upper wall
    board[1][i] = "W"
    # right wall of y axis
    board[i][x - 2] = "W"
for i in range(1, y - 1):
    # left wall of y axis
    board[i][1] = "W"
    # x axis lower wall
    board[y - 2][i] = "W"


player_x = random.randint(3, x - 3)
player_y = random.randint(3, y - 3)

while board[player_y][player_x] == "W":
    player_x = random.randint(3, x - 3)
    player_y = random.randint(3, y - 3)


cat_x = random.randint(3, x - 3)
cat_y = random.randint(3, y - 3)

while board[cat_y][cat_x] == "W":
    cat_x = random.randint(3, x - 3)
    cat_y = random.randint(3, y - 3)

# send local view of the board to gamepad
radio.send(board_microbit(board, player_x, player_y, cat_x, cat_y))

# loop until game is over
game_is_over = False
while not game_is_over:
    # show hint

    # right
    if cat_x > player_x:
        microbit.display.show(microbit.Image.ARROW_E, delay=100)
    # left
    elif cat_x < player_x:
        microbit.display.show(microbit.Image.ARROW_W, delay=100)
    # down
    elif cat_y > player_y:
        microbit.display.show(microbit.Image.ARROW_S, delay=100)
    # up
    else:
        microbit.display.show(microbit.Image.ARROW_N, delay=100)

    # wait until gamepad sends an order
    order = get_message()

    # execute order (move player)

    # right
    if order == "R" and board[player_y][player_x + 1] != "W":
        player_x += 1
    # left
    elif order == "L" and board[player_y][player_x - 1] != "W":
        player_x -= 1
    # down
    elif order == "U" and board[player_y + 1][player_x] != "W":
        player_y += 1
    # up
    elif order == "D" and board[player_y - 1][player_x] != "W":
        player_y -= 1

    # send local view of the board to gamepad
    radio.send(board_microbit(board, player_x, player_y, cat_x, cat_y))

    # check if game is not over
    game_is_over = cat_x == player_x and cat_y == player_y

    if not game_is_over:
        # wait a few seconds and clear screen
        microbit.sleep(2000)
        microbit.display.clear()

        # update position of the cat
        direction = random.randint(0, 4)

        if order == "R" or order == "L" or order == "U" or order == "D":
            # right
            if direction == 0 and board[cat_y][cat_x + 1] != "W":
                cat_x += 1
            # left
            elif direction == 1 and board[cat_y][cat_x - 1] != "W":
                cat_x -= 1
            # down
            elif direction == 2 and board[cat_y + 1][cat_x] != "W":
                cat_y += 1
            # up
            elif direction == 3 and board[cat_y - 1][cat_x] != "W":
                cat_y -= 1

# tell that the game is over
microbit.display.scroll("You won", delay=100)
