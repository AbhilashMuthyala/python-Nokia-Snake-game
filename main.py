
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def start():

    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    snake = Snake()
    screen.listen()
    food = Food()
    score = Scoreboard()

    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_is_on = True
    counter = 0

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.increase_snake()
            counter += 1
            score.current_score = counter
            score.board_refresh()
        # Detect collision with Wall

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            score.gameover()
            print("collision - wall")
            game_is_on = False

        if snake.check_tail_collision():
            print("collision - tail")
            score.gameover()
            game_is_on = False

    screen.exitonclick()

if __name__ == '__main__':
    start()


