from turtle import *
import turtle
from random import randrange
from freegames import square, vector
import time

record = []
level = 1
cost = 2 + level*3
wall = vector(100,100)
wallsy = []
wallsx = []
walls = []
def resetwalls():
    global wall, wallsx, wallsy, walls
    walls.clear()
    wallsx.clear()
    wallsy.clear()
    for i in range(int(level*3.5)):  
        wall.x = randrange(-19,19) * 20
        wall.y = randrange(-19,19) * 20
        wallsx.append(wall.x)
        wallsy.append(wall.y)
        walls.append(vector(wallsx[i],wallsy[i]))
    
resetwalls()
def draw_wall():
    global walls, wall, wallsy, wallsx
    for i in range(int(level*3.5)):
        square(wallsx[i], wallsy[i], 9, 'brown')
        

def start():
    global record
    global level
    global cost
    cost = 2 + level*3
    time.sleep(1)

    wn = turtle.Screen()
    wn.title('Snake by Omer826')
    wn.setup(width = 1.0, height = 1.0)
    wn.bgcolor('black')

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed("fastest")

    t.goto(-400,400)
    t.fillcolor("cyan")
    t.begin_fill()
    for i in range(4):
        t.forward(800)
        t.right(90)
    t.end_fill()

    t.hideturtle()

    port = turtle.Turtle()
    port.hideturtle()
    port.penup()
    port.speed("fastest")

    port.goto(400,40)
    port.fillcolor("yellow")
    port.begin_fill()
    for i in range(4):
        port.forward(80)
        port.right(90)
    port.end_fill()

    port.hideturtle()

    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)


    Long = turtle.Turtle()
    Long.hideturtle()
    Long.color('white')
    Long.penup()
    Long.goto(0, 400)
    Long.color('purple')
    Long.write(f'The snake is {len(snake)} meters long \n Your level is: {level}', align="center", font=("Courier New", 26, "normal")) 

    Drecord = turtle.Turtle()
    Drecord.hideturtle()
    Drecord.color('white')
    Drecord.penup()
    Drecord.goto(675, 475)
    Drecord.color("gold")
    Drecord.write(f'Your record is level {max(record, default=0)}', align="center", font=("Courier New", 22, "normal"))

    Howl = turtle.Turtle()
    Howl.hideturtle()
    Howl.color('white')
    Howl.penup()
    Howl.goto(450, 50)
    Howl.color('pink')
    Howl.write(f'{cost}M \nPortal', align="center", font=("Courier New", 16, "normal"))  

    def change(x, y):
        new_aim = vector(x, y)
        if len(snake) <= 1:
            aim.x = x
            aim.y = y
        if new_aim != -aim:
            aim.x = x
            aim.y = y

    def inside(head):
        return -410 < head.x < 400 and -410 < head.y < 400
    
    def move():
        global level
        head = snake[-1].copy()
        head.move(aim)
        if not inside(head) and not (30 >= head.y >= -40 and head.x >= 400 and len(snake) >= cost) or head in snake or head in walls:
            
            square(head.x, head.y, 9, 'red')
            record.append(level)
            Drecord.clear()
            Long.clear()
            Howl.clear()
            level = 1
            resetwalls()
            update()
            reset()
            start()
            return record
        draw_wall()
        if (30 >= head.y >= -40 and head.x >= 480 and len(snake) >= cost):
            level += 1
            Long.clear()
            Drecord.clear()
            Howl.clear()
            resetwalls()
            update()
            reset()
            start()
            return level
  
        snake.append(head)
        draw_wall()
        
        if head == food:
            food.x = randrange(-20, 20) * 20
            food.y = randrange(-20, 20) * 20
            Long.clear()
            Long.write(f'The snake is {len(snake)} meters long \n Your level is: {level}', align="center", font=("Courier New", 26, "normal")) 


        else:
            snake.pop(0)
        
        clear()

        for body in snake:
            square(body.x, body.y, 9, 'green')

        square(food.x, food.y, 9, 'blue')
        draw_wall()
        update()
        ontimer(move, int(200*pow(0.75,level-1)))

    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()  
    done()

start()








# for j in range(100):
#     print(int((5*(j)*(1+(j-1)*1.25))/(j+1)))