from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
screen = Screen()
screen.colormode(255)
screen.listen()
screen.setup(600, 600)
screen.bgcolor("black")

screen.tracer(0)

fence = []


def make_horizontal_fence(x, y):
    for i in range(-x, x):
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(stretch_wid=0.5)
        segment.color("yellow")
        segment.penup()
        segment.right(0)
        segment.goto(10 * i, y)
        fence.append(segment)


def make_vertical_fence(y, x):
    for i in range(-y, y):
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(stretch_wid=0.5)
        segment.color("yellow")
        segment.penup()
        segment.right(90)
        segment.goto(x, 10 * i)
        fence.append(segment)


make_vertical_fence(30, 300)
make_vertical_fence(30, -300)
make_horizontal_fence(30, 300)
make_horizontal_fence(30, -300)

game_on = True

scorecard = Scoreboard()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")
    screen.onkey(snake.move_upwards, "Up")
    screen.onkey(snake.move_downwards, "Down")

    if snake.segments[0].distance(food) < 15:
        print(len(snake.segments) - 1)
        food.refresh()
        snake.extend()
        scorecard.clear()
        scorecard.increase_score()
        scorecard.update_scoreboard()
        scorecard.update_highscore()


    for brick in fence:
        if snake.segments[0].distance(brick)<10:


            scorecard.game_over()
            time.sleep(1)

            scorecard.clear()
            scorecard.reset()
            scorecard.update_scoreboard()
            scorecard.update_highscore()

            for segment in snake.segments:
                segment.goto(1000, 300)
            snake.hideturtle()

            snake = Snake()
            print("I hit fence")

    for x in range(1, len(snake.segments) - 1):
        if snake.segments[0].distance(snake.segments[x]) < 10:
            print("I hit myself")
            print(x)
            scorecard.clear()
            scorecard.reset()
            scorecard.update_scoreboard()
            scorecard.update_highscore()
            snake = Snake()
            break
screen.exitonclick()
