from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.title("Snake Game")
snake = Snake()
food=Food()
food.refresh()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.grow()
    pos=snake.head.pos()
    if pos[0]>315 or pos[0]<-315 or pos[1]>315 or pos[1]<-315:
        snake.reset()
        score.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset()
            score.reset()
screen.exitonclick()
