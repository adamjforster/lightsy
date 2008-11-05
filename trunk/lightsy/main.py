from random import randint, choice

import pyglet
from pyglet.window import mouse

from levels import LEVELS

LIGHT_WIDTH = 50
LIGHT_HEIGHT = 45
BOARD_SIZE = 5

def build_board(random=False):
    '''
    Example board:
    board = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]
    '''
    if random:
        board = []
        for y in range(BOARD_SIZE):
            row = []
            for x in range(BOARD_SIZE):
                row.append(randint(0, 1))
            board.append(row)
    else:
        board = choice(LEVELS)
    return board

board = build_board()

window = pyglet.window.Window(BOARD_SIZE * LIGHT_WIDTH, BOARD_SIZE * LIGHT_HEIGHT)
light_off = pyglet.resource.image('light-off.jpg')
light_on = pyglet.resource.image('light-on.jpg')

def draw_board():
    for row in range(BOARD_SIZE):
        for square in range(BOARD_SIZE):
            if board[row][square] == 1:
                light_on.blit(LIGHT_WIDTH * square, window.height - (LIGHT_HEIGHT * row) - LIGHT_HEIGHT)
            else:
                light_off.blit(LIGHT_WIDTH * square, window.height - (LIGHT_HEIGHT * row) - LIGHT_HEIGHT)

def x_index(x):
    return x//LIGHT_WIDTH
  
def y_index(y):
    return (y//LIGHT_HEIGHT - 4) * -1

def change_lights(x, y):
    x = x_index(x)
    y = y_index(y)
    coord_set = (
        (y-1, x),
        (y, x-1),
        (y, x),
        (y, x+1),
        (y+1, x),
    )
    for coords in coord_set:
        try:
            if coords[0] >= 0 and coords[1] >= 0:
                board[coords[0]][coords[1]] = not(board[coords[0]][coords[1]])
        except IndexError:
            pass

@window.event
def on_draw():
    window.clear()
    draw_board()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        change_lights(x, y)

pyglet.app.run()
