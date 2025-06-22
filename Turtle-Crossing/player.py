from turtle import Turtle

MOVE_SPEED = 10
ALIGNMENT = 'center'
FONT = ('Brass Mono Regular', 30, 'bold')

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('salmon4')
        self.shape('turtle')
        self.penup()
        self.goto(0, -220)
        self.setheading(90)
    
    def go_up(self) -> None:
        new_y = self.ycor() + MOVE_SPEED
        self.sety(new_y)
    
    def next_level(self) -> None:
        self.goto(0, -220)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.color('black')
        self.write('GAME OVER', font=FONT, align=ALIGNMENT)