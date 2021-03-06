from random import randint
from time import sleep
import keyboard

import cursor


class Game:
    WIDTH = 50
    HEIGHT = 24

    def __init__(self):
        self.snake = Snake()


    def game_loop(self):
        self.generate_food()
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
        self.generate_food()
        A, B = randint(1, self.WIDTH - 1), randint(1, self.HEIGHT - 1)
        cursor.draw(A, B, Snake.FOOD)

    def generate_food(self):
        '''if eaten generate new food'''
        self.food_pos = randint(1, self.WIDTH - 1), randint(1, self.HEIGHT - 1)


    def update(self):
        X, Y = Snake.START_POS
        x = 0
        y = 1
        for x in range(25):
            self.snake.handle_input()
            cursor.draw(X, Y, Snake.EMPTY)
            # movement direction - to be considered later
            X += x
            Y += y
            cursor.draw(X, Y, Snake.SNAKE_HEAD)
            sleep(1)
            if X == 0 or X == 49:
                print("GAME OVER")
                break
            if Y == 0 or Y == 23:
                print("GAME OVER")
                break


class Snake:
    WALL = '#'
    EMPTY = ' '
    SNAKE_HEAD = 'D'
    SNAKE = 'X'
    FOOD = 'F'

    START_POS = 25, 12
    DIRECTIONS = {'w': (0, -1), 'd': (1, 0), 's': (0, 1), 'a': (-1, 0)}
    UP, RIGHT, DOWN, LEFT = 'wdsa'

    def __init__(self):
        self.dir = self.DIRECTIONS['w']
        self.x, self.y = self.START_POS

    def update(self) -> None:
        """updates game state by one tick of logic"""
        pass

    def handle_input(self):
        """Changes direction of snake based on player input"""
        if keyboard.is_pressed('d'):
            self.dir = self.DIRECTIONS['d']
        if keyboard.is_pressed('a'):
            self.dir = self.DIRECTIONS['a']
        if keyboard.is_pressed('w'):
            self.dir = self.DIRECTIONS['w']
        if keyboard.is_pressed('s'):
            self.dir = self.DIRECTIONS['s']


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
