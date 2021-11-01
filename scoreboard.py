from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-10,260)
        self.board_refresh()

    def board_refresh(self):
        self.clear()
        self.write(f"Score = {self.current_score}",move=False, align='center',font=('Courier', 14, 'normal'))

    def gameover(self):
        #self.clear()
        self.goto(0,0)
        self.write(f" Gameover",move=False, align='center',font=('Courier', 14, 'normal'))
