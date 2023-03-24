import random, turtle

class Shape:
    '''
    Purpose:
        An object of this class represents a shape.
    Instance variables:
        self.x - the x value initialized to 0
        self.y - the y value initialized to 0
        self.color - color of the shape which is a random choice
        between the given list

    Methods:
        __str__(self) - returns the location and color of the object like so
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
        An object of this type represents a shape specifically a circle
    Instance variables:
        Inherits from Shape class as well as has a
        self.rad which represents the radius
    Methods:
        __str__(self) - returns the circle location in string format
        similar to shape class but also includes the radius as a string
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
        return False

class Display:
    '''
    Purpose:
        managing the drawn shapes
    Instance variables:
        self.shapes - a list of shapes initialized empty
        self.t - no idea
    Methods:
    '''

    def __init__(self):
        self.shapes = []
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        turtle.delay(0)
        turtle.onscreenclick(self.mouse_event)
        # turtle.listen()
        turtle.mainloop()  #Required for some IDEs
    def mouse_event(self,x,y):
        randomm = random.randint(0,1)
        if randomm == 0:
            new_circ = Circle(x,y,random.randint(10,50))
            self.shapes.append(new_circ)
            new_circ.draw(self.t)
        else:
            new_rec = Rectangle(x,y,random.randint(10,50),random.randint(10,50))
            self.shapes.append(new_rec)
            new_rec.draw(self.t)
        for shape in self.shapes:
            if shape.contains(x,y) == True:
                print(shape.__str__())
            else:
                shape.draw(self.t)
    
Display()

class Rectangle(Shape):
    def __init__(self,x,y,width=20,height=20):
        Shape.__init__(self,x,y)
        self.width = width
        self.height = height
    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + f'{color}, w:{width}, h:{height}'
        # return f'(x={x}, y ={y}), {color}, w:{width}, h:{height}'
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


        # self.draw(self.t)
    def contains(self,x,y):
        if x > self.x and x < (self.x + self.width) and y > self.y and y < (self.y+self.height):
            return True
        return False
