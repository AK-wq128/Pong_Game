from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_rate = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        '''Move the ball around the boundaries of the screen'''
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''Bounce the ball along the y axis'''
        self.y_move *= -1

    def bounce_x(self):
        '''Bounce the ball along the x axis'''
        self.x_move *= -1
        self.move_rate *= 0.9

    def reset_position(self):
        '''Return the ball to the center of the screen'''
        self.goto(0, 0)
        self.move_rate = 0.1
        self.bounce_x()


