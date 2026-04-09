import turtle as t
import pandas as pd

screen = t.Screen()
screen.setup(width=982, height=800)
screen.title("Indian States Guessing Game")

img = "india_map.gif"
t.addshape(img)

tim = t.Turtle()
tim.shape(img)

def get_mouse_click(x,y):
    print(f"{x}, {y}")
t.onscreenclick(get_mouse_click)

data = pd.read_csv("capitals.csv")
print(data)

screen.exitonclick()