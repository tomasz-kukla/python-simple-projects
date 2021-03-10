from os import system
from random import randint
from time import sleep
import keyboard


class Game:
    WIDTH = 50
    HEIGHT = 24

    def __init__(self):
        self.snake = Snake()
        self.food_pos = None
        self.alive = True
        self.score = 0
        self.dire = self.snake.dir

    def game_loop(self):
        system("cls")
        self.generate_food()
        while self.alive:
            self.draw()
            self.snake.update()
            if not self.alive:
                return 0

    def draw(self):
        """draws all game objects into the terminal"""
        system("cls")
        print(f"Snake: {self.snake.x, self.snake.y}"
              f"\nSnake-1: {self.snake.headPos[0], self.snake.headPos[1]} "
              f"\nFood: {self.food_pos[0], self.food_pos[1]}")
        for y in range(self.HEIGHT):
            temp = ""
            for x in range(self.WIDTH):
                if y == 0 or y == self.HEIGHT - 1:
                    temp += Snake.WALL
                elif x == 0 or x == Game.WIDTH - 1:
                    temp += Snake.WALL
                elif x == self.snake.x and y == self.snake.y:
                    temp += Snake.SNAKE_HEAD

                elif x == self.snake.headPos[0] and y == self.snake.headPos[1] and self.score > 0:
                    temp += Snake.SNAKE


                elif x == self.food_pos[0] and y == self.food_pos[1]:
                    temp += Snake.FOOD
                else:
                    temp += Snake.EMPTY
            print(temp)

    def generate_food(self):
        """if eaten generate new food"""
        self.food_pos = randint(1, self.WIDTH - 3), randint(1, self.HEIGHT - 3)


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
        self.headPos = self.START_POS

    def update(self) -> None:
        """updates game state by one tick of logic"""
        self.handle_input()
        self.move()
        self.consume()
        self.die()

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
        self.headPos = self.x, self.y
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
        if self.x == game.food_pos[0] and self.y == game.food_pos[1]:
            game.score += 1
            game.generate_food()

    def die(self) -> None:
        """handles snake death when it has collided with the wall"""
        if self.x == Game.WIDTH or self.x == 0 \
                or self.y == Game.HEIGHT or self.y == 0:
            print(f"Dead! score: {game.score} ")
            self.x, self.y = self.START_POS
            game.score = 0
            sleep(2)
            game.alive = False


if __name__ == '__main__':
    game = Game()
    game.game_loop()
