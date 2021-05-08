from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("Purple")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
             file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
