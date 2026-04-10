import turtle as t
import pandas as pd
import tkinter as tk
from tkinter import messagebox

screen = t.Screen()
screen.setup(width=982, height=760)
screen.title("Indian States Guessing Game")

img = "india_map.gif"
t.addshape(img)

tim = t.Turtle()
tim.shape(img)

data = pd.read_csv("capitals.csv")

guessed_capitals = []
capitals = data["Capital"].to_list()


class Countdown:
    def __init__(self, root):
        self.root = root
        self.remaining_seconds = 5 * 60
        self.timer_window = tk.Toplevel(self.root)
        self.timer_window.title("Time left:")
        self.timer_window.geometry("200x100")

        # This line keeps the timer on top
        self.timer_window.attributes("-topmost", True)

        self.label = tk.Label(self.timer_window, text="", font=("Helvetica", 48))
        self.label.pack(expand=True)
        self.update_timer()

    def update_timer(self):
        if self.remaining_seconds >= 0:
            mins, secs = divmod(self.remaining_seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            self.label.config(text=time_format)
            self.remaining_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("OOPS!", "You ran out of time")
        screen.bye()


root = screen.getcanvas().winfo_toplevel()
timer = Countdown(root)

while len(guessed_capitals) < len(capitals):
    answer = screen.textinput(title=f"{len(guessed_capitals)} / 28",
                              prompt="Enter your answer: ").title()

    if answer == "Exit":
        missing_capitals = []
        for capital in capitals:
            if capital not in guessed_capitals:
                missing_capitals.append(capital)
        print("Capitals you couldn't guess are:")
        print(f" \n".join(missing_capitals))
        screen.bye()
        break

    if answer in capitals and answer not in guessed_capitals:
        guessed_capitals.append(answer)
        tpen = t.Turtle()
        tpen.hideturtle()
        tpen.penup()
        capital_data = data[data.Capital == answer]
        tpen.goto(capital_data["x"].item(), capital_data["y"].item())
        tpen.write(answer)

    if len(guessed_capitals) == len(capitals):
        print("Congratulations, you've guessed it all!")
        screen.bye()

screen.mainloop()