from os import write
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board= Scoreboard()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) <20:
        food.nom_nom()
        snake.extend()
        score_board.inc_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on= False
        score_board.render()
        score_board.game_over()

    for seg in snake.segment_family[1:]:
        if snake.head.distance(seg) <10:
            game_is_on= False
            score_board.render()

screen.exitonclick()