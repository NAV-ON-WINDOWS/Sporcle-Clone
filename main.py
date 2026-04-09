import turtle as t
import pandas as pd

screen = t.Screen()
screen.setup(width=982, height=760)
screen.title("Indian States Guessing Game")

img = "india_map.gif"
t.addshape(img)

tim = t.Turtle()
tim.shape(img)

# def get_mouse_click(x,y):
#     print(f"{x}, {y}")
# t.onscreenclick(get_mouse_click)

data = pd.read_csv("capitals.csv")
# print(data)

guessed_capitals = []
capitals = data["Capital"].to_list()

while len(guessed_capitals) < len(capitals):
    answer = screen.textinput(title=f"{len(guessed_capitals)} / 27",
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

    if answer in capitals:
        guessed_capitals.append(answer)
        tpen = t.Turtle()
        tpen.hideturtle()
        tpen.penup()
        capital_data = data[data.Capital == answer]
        tpen.goto(capital_data["x"].item(), capital_data["y"].item())
        tpen.write(answer)

screen.mainloop()