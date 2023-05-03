import csv
from tkinter import *
from random import randint
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
# ---------------------------------------------HDNCN----------------------------------------------------#

data = pd.read_csv("data/1500_Frequency lists_Japanese.csv")

word = {}
number = 0
diff = []

def random_word():
    global number, word, flip_timer
    window.after_cancel(flip_timer)
    number = randint(1, len(data))
    row = data.iloc[number]
    word = row.to_dict()
    canvas.itemconfig(image, image=front_image)
    canvas.itemconfig(ja, text="Japanese", fill="black")
    canvas.itemconfig(ja_word, text=word['Japanese'], fill="black")
    flip_timer = window.after(3000, change_meaning)

def change_meaning():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(ja, text="Vietnamese", fill="white")
    canvas.itemconfig(ja_word, text=word['Vietnamese'], fill="white")

def not_know():
    diff_word = data.iloc[number].to_dict()
    diff.append(diff_word)
    new_data = pd.DataFrame(diff)
    new_data.to_csv("data/different_word.csv")

    random_word()

# ----------------------------------------------UI------------------------------------------------------#
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, change_meaning)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
ja = canvas.create_text(400, 150, text="Japanese", fill="black", font=(FONT_NAME, 40, "italic"))
ja_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=random_word)
button_right.grid(row=1, column=1)

left_image = PhotoImage(file="images/wrong.png")
button_left = Button(image=left_image, highlightthickness=0, command=not_know)
button_left.grid(row=1, column=0)

random_word()

window.mainloop()