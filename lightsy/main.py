import copy

import pyglet
from pyglet.window import mouse

from levels import ANIMATION, EMPTY, LEVELS

class Board():
    SIZE = 5
    LIGHT_WIDTH = 50
    LIGHT_HEIGHT = 45

    LIGHT_ON = pyglet.resource.image('light-on.jpg')
    LIGHT_OFF = pyglet.resource.image('light-off.jpg')
    
    def __init__(self):
        self.ani_step = 0
        self.load_level(0)
        
    def load_level(self, level_number):
        try:
            self.load_board(LEVELS[level_number])
        except IndexError:
            level_number = 0
            self.load_board(LEVELS[level_number])
        self.current_level = level_number

    def load_board(self, board):
        # Ensure that self.lights is a clone of the level and not an alias.
        self.lights = copy.deepcopy(board)
    
    def is_complete(self):
        if self.lights == EMPTY:
            return True
        else:
            return False
    
    def __get_x_index(self, x):
        return x//Board.LIGHT_WIDTH
      
    def __get_y_index(self, y):
        return (y//Board.LIGHT_HEIGHT - 4) * -1
    
    def draw(self, max_height):
        for row in range(Board.SIZE):
            for square in range(Board.SIZE):
                if self.lights[row][square] == 1:
                    Board.LIGHT_ON.blit(
                        Board.LIGHT_WIDTH * square,
                        max_height - (Board.LIGHT_HEIGHT * row) - Board.LIGHT_HEIGHT
                    )
                else:
                    Board.LIGHT_OFF.blit(
                        Board.LIGHT_WIDTH * square,
                        max_height - (Board.LIGHT_HEIGHT * row) - Board.LIGHT_HEIGHT
                    )
    
    def press(self, x, y):
        x = self.__get_x_index(x)
        y = self.__get_y_index(y)
        coordinate_set = (
            (y-1, x),
            (y, x-1),
            (y, x),
            (y, x+1),
            (y+1, x),
        )
        for coords in coordinate_set:
            try:
                if coords[0] >= 0 and coords[1] >= 0:
                    self.lights[coords[0]][coords[1]] = not(self.lights[coords[0]][coords[1]])
            except IndexError:
                pass
        if self.is_complete():
            pyglet.clock.schedule_interval(self.animate, 10/60.0)

    def animate(self, dt):
        try:
            self.load_board(ANIMATION[self.ani_step])
            self.ani_step += 1
        except IndexError:
            pyglet.clock.unschedule(self.animate)
            self.ani_step = 0
            self.load_level(self.current_level + 1)
    
class LightsyWindow(pyglet.window.Window):
    def __init__(self):
        super(LightsyWindow, self).__init__()
        self.board = Board()
        self.set_caption('Lightsy')
        self.set_size(
            Board.SIZE * Board.LIGHT_WIDTH,
            Board.SIZE * Board.LIGHT_HEIGHT
        )
    
    def on_draw(self):
        self.clear()
        self.board.draw(self.height)
        
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.board.press(x, y)

if __name__ == '__main__':
    LightsyWindow()
    pyglet.app.run()
