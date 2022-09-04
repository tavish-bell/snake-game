"""
Scoreboard class
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """
    create scoreboard
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        # read data.txt, convert str to int and save int
        # to self.high_score
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        update scoreboard
        """
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """
        increase score when snake gets food
        """
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        keep track of and reset high score
        """
        if self.score > self.high_score:
            self.high_score = self.score
            # rewrite contents of data file to replace
            # high score. Have to convert high score into
            # str, then write into data.txt file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     write game over
    #     """
    #     self.goto(0, 0)
    #     self.write(
    #         "GAME OVER",
    #         move=False,
    #         align=ALIGNMENT,
    #         font=FONT,
    # )
