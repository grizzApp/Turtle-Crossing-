from turtle import Turtle

ALIGNMENT = 'left'
FONT = ('Brass Mono Regular', 20, 'normal')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-250, 250)
        self.level_text()
        self.hideturtle()

    def level_text(self) -> None:
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.clear()
        self.level_text()