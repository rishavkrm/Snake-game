from turtle import Turtle

with open("highscore.txt", mode="r") as file:
    high_score = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.str_score = str(self.score)
        self.high_score = high_score
        self.hideturtle()
        self.update_scoreboard()
        self.update_highscore()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("orange")
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0

    def update_scoreboard(self):
        self.penup()
        self.color("yellow")
        self.goto(0, 235)
        self.write(f"Score : {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def update_highscore(self):
        self.penup()
        self.goto(0, 265)
        self.color("red")
        self.write(f"High Score : {self.high_score}", move=False, align="center", font=("Courier", 25, "normal"))

    def increase_score(self):
        self.score += 1
