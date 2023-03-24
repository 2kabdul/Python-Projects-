def div27(num):
    for i in range(2,8):
        if num % i == 0:
            return True
    return False

import turtle, random
turtle.speed(0)
turtle.delay(0)

def filled_square(side):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def spiro(num, side):
    for i in range(num):
        turtle.left(360/num)
        filled_square(side)

def mul(a,b):
    prod = 0
    for i in range(b):
        prod = a + prod
    return prod

def mul2(a,b):
    i = 1
    prod = 0
    while i <= b:
        prod = a + prod
        i = i + 1
    return prod

def expo(x,y):
    i = 1
    prod = 1
    while i <= y:
        prod = x * prod
        i = i + 1
    return prod

import turtle, random
turtle.speed(0)
turtle.delay(0)

def drunkwalk():
    i = 0
    while i <= 200:
        turtle.forward(30)
        turtle.setheading(random.randint(0,3) * 90)
        i += 1

import turtle, random
turtle.speed(0)
turtle.delay(0)

def drunkwalk():
    count = 0
    while turtle.xcor() <= 300 and turtle.ycor() >=-300 and turtle.xcor() >=-300 and turtle.ycor() <=300:
        turtle.forward(30)
        turtle.setheading(random.randint(0,3) * 90)
        count += 1
    turtle.write(count, font=("Arial", 20, "normal"))
