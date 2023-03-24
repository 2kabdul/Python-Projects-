import turtle

def disp_xy(x, y):
    print("Clicked at", x, y)

turtle.onscreenclick(disp_xy)
turtle.listen()

import random, turtle

class Shape:
    '''
    Purpose:
        An object of this class represents a shape
    Instance variables:
        self.x - the x value initialized to 0
        self.y - the y value initialized to 0
        self.color - color of the shape which is a random
        choice between the given list

    Methods:
        __str__(self) - returns the location and color of the object which is
        "(x="+str(self.x)+", y="+str(self.y)+"), " + col
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = random.choice(["red", "orange", "yellow",
                         "green", "blue", "purple"])
    def __str__(self):
        loc = "(x="+str(self.x)+", y="+str(self.y)+"), "
        col = self.color
        return loc + col

class Circle(Shape):
    '''
    Purpose:
        An object of this type represents a shape which is a circle
    Instance variables:
        Inherits from Shape class as well as has a
        self.rad which represents the radius
    Methods:
        __str__(self) - returns the circle location in string format
        similar to shape class but also includes the radius as a string
        draw: draws out the circles filling the color

    '''
    def __init__(self, x=0, y=0, rad=0):
        Shape.__init__(self,x,y)
        self.rad = rad
    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + ", rad="+str(self.rad)
    def draw(self,t):
        t.penup()
        t.setpos(self.x,self.y-self.rad)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.rad)
        t.end_fill()
    def contains(self,x,y):
        distance = (((self.x - x)**2) + ((self.y - y)**2))**0.5
        if distance < self.rad:
            return True
        else:
            return False

class Rectangle(Shape):
    def __init__(self,x,y,width=20,height=20):
        Shape.__init__(self,x,y)
        self.width = width
        self.height = height
    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + self.color + str(self.width) + str(self.height)
        # return f'(x={x}, y ={y}), {color}, w:{width}, h:{height}'
        # return "'" + "(" + "x" + "=" + self.x + "y" + "=" + self.y + ")" + ", " + self.color + ", " + 'w' + ":" + self.width + ", " + "h" + self.height + "'"
    def draw(self,t):
        t.penup()
        t.setpos(self.x,self.y)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.end_fill()
    def contains(self,x,y):
        if x > self.x and x < (self.x + self.width) and y > self.y and y < (self.y+self.height):
            return True
        else:
            return False


class Display:
    '''
        Purpose:
            manages the drawn shapes
        Instance variables:
            self.shapes - a list of shapes initialized empty
            self.t - referring to the turtle object
        Methods:
            mouse_event - follows the mouse and draws the new circle
    '''

    def __init__(self):
        self.shapes = []
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        turtle.delay(0)
        turtle.onscreenclick(self.mouse_event)
        turtle.listen()
        turtle.mainloop()  #Required for some IDEs
    def mouse_event(self,x,y):
        # # new_circ = Circle(x,y,random.randint(10,50))
        # # self.shapes.append(new_circ)
        # # new_circ.draw(self.t)
        # new_rec = Rectangle(x,y,random.randint(10,50))
        # self.shapes.append(new_rec)
        # new_rec.draw(self.t)
        ran = random.randint(0,1)
        # new_rec = Rectangle(x,y,random.randint(10,50))
        # self.shapes.append(new_rec)
        # new_rec.draw(self.t)
        for shape in self.shapes:
            if shape.contains(x,y) == True:
                print(shape)
                ran = 3
        if ran == 0:
            new_circ = Circle(x,y,random.randint(10,50))
            self.shapes.append(new_circ)
            new_circ.draw(self.t)
        elif ran == 1:
            new_rec = Rectangle(x,y,random.randint(10,50))
            self.shapes.append(new_rec)
            new_rec.draw(self.t)
        # for shape in self.shapes:
        #     if shape.contains(x,y) == True:
        #         print(shape)
        #     # else:
            #     shape.draw(self.t)
Display()
