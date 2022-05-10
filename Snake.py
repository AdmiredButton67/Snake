"""Snake, classic arcade game.

Exercises

Nombre Luis Armando Mandujano Chávez

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random 

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(10, 0)


cs = random.randint(1,3)
if cs == 1:
    h = "blue"
elif cs == 2:
    h = "purple"
else:
    h = "yellow"

cf = random.randint(1,3)
if cf == 1:
    P = "organge"
elif cf == 2:
    P = "brown"
else:
    P = "grey"


 
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, h)

    square(food.x, food.y, 9, P)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()