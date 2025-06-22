from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)
screen.colormode(255)

#countdown
time.sleep(2)

t = Player()
level = Level()

cars = []
for _ in range(20):
    car = Car()
    car.goto(car.rand_pos())
    cars.append(car)

screen.listen()
screen.onkey(t.go_up, 'Up')

is_alive = True
while is_alive:

    screen.update()
    time.sleep(car.move_speed)

    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.car_respawn() 
    
        if car.distance(t) < 30:
            t.game_over()
            is_alive = False 

    if t.ycor() > 280:
        level.increase_level()
        t.next_level()
        for car in cars:
            car.next_level()
        time.sleep(0.5)

screen.exitonclick()