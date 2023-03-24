import turtle, random

class Game:
    '''
Purpose: This controls the game and moves the snake around and implements the different classes
Instance variables: turtle.setup: This is setup the turtle game  and the wrold and speed
Self,gameloop: allows the game to work and move around the snake and eat
Methods: gameloop: is able to check the game and end the game over if the snake hits a boundary or itself
'''

    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.player = Snake(315, 315, 'green')
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.listen()
        turtle.mainloop()





    def gameloop(self):
        self.player.move()
        if self.player.check_game() == True:
            turtle.write("Game Over")
            turtle.done()
        turtle.ontimer(self.gameloop, 200)



class Snake:
    '''
Purpose: The snake that can grow and eat pellet is repesented
Instance variables: self.x: is the x coordinate, self.y: is the y coordinate, self.color:
is the color of the snake, self.segments: parts of the snake, self.foods: represents the pellet
Methods: Grow: builds the snake and the move moves the snake around. move: allows the snake to grow and move
CHeck_game: checks if the snake hits the boundaries.  
'''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0
        self.foods = Food()
    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x == self.foods.pellet.xcor():
            if self.y == self.foods.pellet.ycor():
                self.grow()
                self.foods.random_spot()
        # elif
        #     self.grow()
        #     self.foods.random_spot()
        else:
            for x in range(len(self.segments)-1):
            # move on to each segment
                (self.segments[x].setpos(self.segments[x+1].xcor(), self.segments[x+1].ycor()))
            #implement the food pellet
            self.segments[-1].setpos(self.x, self.y)
    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_up(self):
        self.vx = 0
        self.vy = 30
    def check_game(self):
        if self.segments[-1].xcor() <= 0 or self.segments[-1].xcor() >=600:
            return True
        if self.segments[-1].ycor() <= 0 or self.segments[-1].ycor() >= 600:
            return True
        for i in range(len(self.segments)-1):
            if self.segments[i].xcor() == self.segments[-1].xcor():
                if self.segments[i].ycor() == self.segments[-1].ycor():
                    return True
class Food:
    '''
Purpose: Represent the food pellet that the snake is going to eat
Instance variables: self.x: is the x coordinate, self.y: is the y coordinate
self.pellet: is the red pellet for the snake to eat
Methods: The method used for this is random_spot that brings the pellet after eaten into a new spot
'''

    def __init__(self):
        #move to a random grid aligned postion
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.color = 'red'
        self.pellet = turtle.Turtle()
        self.pellet.speed(0)
        self.pellet.fillcolor(self.color)
        self.pellet.shape('circle')
        self.pellet.shapesize(1.5, 1.5)
        self.pellet.penup()
        self.pellet.setpos(self.x, self.y)
        # self.segments.append(pellet)
        # foods = 15 + 30*random.randint(0,19)
    def random_spot(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.x, self.y)


Game()
