import turtle  #Required to use functions from the turtle module
turtle.forward(100)  #Move forward 100 units
turtle.left(90)  #Turn left 90 degrees
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.left (30)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)

def draw_square(length):
    length = (int('enter the side length:'))
    turtle.left(30)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

def draw_traingle(length):
    length = (int('enter the side length:'))
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)

shape = input('Enter shape toe (S or s for square, T or t for traingle):')
length = (int('enter the side length:'))

if shape.lower() == 't':
    draw_triangle(length)
elif shape.lower() == 's':
    draw_square(length)
else:
    print('Illegal shape type entered:')

def round_it(num):
    num = float(input('Enter float here:'))
    round(num, 0)

    if num > 0:
        num += 0.5
        num = round(num)
        print(num)
    elif num < 0:
        num -= 0.5
        num = round(num)
        print(num)
    else:
        print('0')

def print_letters(val):
    if val == 1 or val == 2 or val == 6:
        print(3)
    elif val == 4 or val == 5 or val == 9:
        print(4)
    else:
        print(5)

def return_letters(val):
    if val == 1 or val == 2 or val == 6:
        return 3
    elif val == 4 or val == 5 or val == 9:
        return 4
    else:
        return 5



def most_letters(x, y, z):
    x1 = return_letters(x)
    y1 = return_letters(y)
    z1 = return_letters(z)

    if x1 > y1 and x1 > z1:
        return x
    elif y1 > x1 and y1 > z1:
        return y
    elif z1 > x1 and z1 > y1:
        return z
    else:
        print('Tie!')
