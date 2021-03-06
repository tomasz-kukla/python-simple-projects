from os import system
from random import randint
from time import sleep
import keyboard
import cursor


class Game:
    WIDTH = 50
    HEIGHT = 24

    def __init__(self):
        self.snake = Snake()
        self.food_pos = None
        self.alive = True

    def game_loop(self):
        system("cls")
        self.generate_food()
        while self.alive:
            self.draw()
            self.snake.update()

    def draw(self):
        """draws all game objects into the terminal"""
        system("cls")
        for y in range(self.HEIGHT):
            temp = ""
            for x in range(self.WIDTH):
                if y == 0 or y == self.HEIGHT - 1:
                    temp += Snake.WALL
                elif x == 0 or x == Game.WIDTH - 1:
                    temp += Snake.WALL
                elif x == self.snake.x and y == self.snake.y:
                    temp += Snake.SNAKE_HEAD
                elif x == self.food_pos[0] and y == self.food_pos[1]:
                    temp += Snake.FOOD
                else:
                    temp += Snake.EMPTY

            print(temp)

    def generate_food(self):
        """if eaten generate new food"""
        self.food_pos = randint(1, self.WIDTH - 1), randint(1, self.HEIGHT - 1)


class Snake:
    WALL = '#'
    EMPTY = ' '
    SNAKE_HEAD = 'D'
    SNAKE = 'X'
    FOOD = 'F'

    START_POS = 24, 12
    DIRECTIONS = {'w': (0, -1), 'd': (1, 0), 's': (0, 1), 'a': (-1, 0)}
    UP, RIGHT, DOWN, LEFT = 'wdsa'

    def __init__(self):
        self.dir = self.DIRECTIONS['d']
        self.x, self.y = self.START_POS

    def update(self) -> None:
        """updates game state by one tick of logic"""
        self.handle_input()
        self.move()
        #Death by collision with the wall
        if self.x == 49 or self.x == 0:
            Game.alive = False
            print("Dead")
            self.x, self.y = self.START_POS
            sleep(3)

        if self.y == 24 or self.y == 0:
            Game.alive = False
            print("Dead")
            self.x, self.y = self.START_POS
            sleep(3)

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
        self.x += self.dir[0]
        self.y += self.dir[1]

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
