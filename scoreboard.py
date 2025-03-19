from turtle import Turtle

ALIGN= "center"
FONT= ("Courier", 15, "normal")
FONT2= ("Courier", 25, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.highest_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} Highest Score: {self.highest_score}",align=ALIGN,font=FONT)

    def render(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT2)
        self.goto(0, -40)
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT2 )

    def inc_score(self):
        self.score +=1
        self.update()
