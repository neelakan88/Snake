"""action items
1: create snake body
2: move the snake
3: control the snake
4: detect collision with food
5: create a scoreboard
6: detect collsion with wall
7: detect collision with tail"""


# from turtle import Turtle, Screen
# from random import randint

# is_race_on = False
# screen = Screen()
# screen.setup(width = 500, height = 400)

# user_bet = screen.textinput(title = "make your bet", prompt = "Which turtle will win the race? Pick a color: ")
# colors_in_game = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_position = -125
# all_turtles = []


# for turtle_index in range(0,6):
#     new_turtle = Turtle(shape = "turtle")
#     new_turtle.up()
#     new_turtle.goto(-230, y_position + 50*turtle_index)
#     new_turtle.color(colors_in_game[turtle_index])
#     all_turtles.append(new_turtle)


# if user_bet:
#     is_race_on = True

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won, the {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost, the {winning_color} turtle is the winner!")
#             is_race_on = False
#         random_distance = randint(0,10)
#         turtle.forward(random_distance)
    



# screen.exitonclick()







from turtle import Screen#, Turtle can be removed
import time
from snake import Snake
from food import Food
from score import Scoreboard



screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Game of Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food using distance() method from Turtle class. distance() method measures the distance from your turtle object to whatever you put insite the parenthesis
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    
    #detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    
    

    


    



screen.exitonclick()






