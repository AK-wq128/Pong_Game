from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, starting_coordinate):
        super(Paddle, self).__init__()
        self.starting_coordinate = starting_coordinate
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_coordinate)

    def go_up(self):
        '''Move the indicated paddle up the side of the screen'''
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''Move the indicated paddle down the side of the screen'''
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)




