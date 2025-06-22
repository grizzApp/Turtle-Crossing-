from turtle import Turtle
import random
import time

COLORS = [
        (236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), 
        (98, 197, 234), (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), 
        (143, 233, 216), (252, 136, 166), (165, 175, 233), (66, 45, 13), (72, 205, 170), 
        (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), 
        (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), 
        (98, 96, 186), (244, 159, 151), (83, 34, 39), (254, 9, 13), (66, 71, 42), (9, 19, 0)
]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.x_move = 10
        self.penup()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)

    def rand_pos(self) -> tuple:
        self.rand_x = random.randrange(230, -260, -70)
        self.rand_y = random.randrange(220, -150, -70)
        return ((self.rand_x, self.rand_y))
    
    def move(self) -> None:
        new_y = self.xcor() - self.x_move
        self.setx(new_y)
    
    def car_respawn(self):
        rand_num = random.randint(600, 700)
        self.goto(self.rand_x + rand_num, self.rand_y)
    
    def next_level(self):
        self.x_move *= 1
        self.move_speed *= 0.9