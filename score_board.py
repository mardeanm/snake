from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center",
                   font=("Arial", 10, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", "w") as data:
                data.write(str(self.highscore))

        self.score = 0
        self.update_score()
    # def lost(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"You Lost Score: {self.score}", False, align="center", font=("Arial", 15, "bold"))
