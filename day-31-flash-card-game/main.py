from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ==================== READ DATA ==================== #

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/turkish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# known_words = []
# unknown_words = []

# ==================== UPDATE WORD ==================== #

def correct():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()





def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ==================== UI SETUP ==================== #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0,
                      command=correct)
known_button.grid(column=0, row=1)
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0,
                        command=next_card)
unknown_button.grid(column=1, row=1)

next_card()

window.mainloop()
