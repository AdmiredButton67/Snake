"""Snake, classic arcade game.
Luis Armando Mandujano Chávez // A01655899
Lisa Valeria Rodríguez Alanís // A01656306

"""

from random import randrange
from timeit import repeat
from turtle import *
import random 

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


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


    #Mover comida aletariamente dentro de los limites
    cont=0
    if (cont%4==0):
        food.x+= randrange(-10,11,10)
        food.y+= randrange(-10,11,10)
    if -200>food.x: #Si arrevaza el limite de x, y lo regresa
        food.x += 15
    if food.x>190:
        food.x-= 15
    if -200>food.y: #Si arrevaza el limite de y, y lo regresa
        food.y += 15
    if food.y>190:
        food.y-= 15
             
    square(food.x, food.y, 9, 'blue') #Dibuja la comida 

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
