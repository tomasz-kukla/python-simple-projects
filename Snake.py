from random import randint
from time import sleep

import cursor


class Game:
    WIDTH = 50
    HEIGHT = 24

    def __init__(self):
        pass

    def game_loop(self):
        snake = Snake()
        while True:
            self.draw()
            self.update()

    def draw(self):
        """draws all game objects into the terminal"""
        for h in range(self.HEIGHT):
            for w in range(self.WIDTH):
                if h == 0 or h == self.HEIGHT - 1:
                    cursor.draw(w, h, Snake.WALL)
                elif w == 0 or w == Game.WIDTH - 1:
                    cursor.draw(w, h, Snake.WALL)
                else:
                    cursor.draw(w, h, Snake.EMPTY)
        X, Y = Snake.START_POS
        cursor.draw(X, Y, Snake.SNAKE_HEAD)
        cursor.draw(randint(1, self.WIDTH - 1), randint(1, self.HEIGHT - 1), Snake.FOOD)
        pass

    def generate_food(self):
        '''if eaten generate new food'''
        cursor.draw(randint(1, self.WIDTH - 1), randint(1, self.HEIGHT - 1), Snake.FOOD)
        pass

    def update(self):
        X, Y = Snake.START_POS
        for x in range(25):
            cursor.draw(X, Y, Snake.EMPTY)
            X -= 1
            cursor.draw(X, Y, Snake.SNAKE_HEAD)
            sleep(1)
            if X == 0 or X == 49:
                print("GAME OVER")
                return False

        pass


class Snake:
    WALL = '#'
    EMPTY = ' '
    SNAKE_HEAD = 'D'
    SNAKE = 'X'
    FOOD = 'F'

    START_POS = 25, 12
    DIRECTIONS = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    UP, RIGHT, DOWN, LEFT = 'NESW'

    def __init__(self):
        self.dir = self.UP
        self.x, self.y = self.START_POS

    def update(self) -> None:
        """updates game state by one tick of logic"""
        pass

    def handle_input(self) -> None:
        """Changes direction of snake based on player input"""

        pass

    def move(self) -> None:
        """moves snake by one field in x or y axis"""
        pass

    def get_collision(self) -> str:
        """
        returns object snake head has collided with
        options are: [self.EMPTY, self.HEAD, self.SNAKE, self.FOOD]
        """
        pass

    def consume(self) -> None:
        """handles snake growing logic when it has collided with food"""
        pass

    def die(self) -> None:
        """handles snake death when it has collided with food"""
        pass


if __name__ == '__main__':
    game = Game()
    game.game_loop()
