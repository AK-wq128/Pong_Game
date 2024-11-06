from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update the scoreboard with a point for the winner of the round'''
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        '''Increase the score of the left paddle'''
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        '''Increase the score of the right paddle'''
        self.r_score += 1
        self.update_scoreboard()

