from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
# noinspection SpellCheckingInspection
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPEATS = 0
TEXT = ""
Timer = "None"


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global TEXT
    global REPEATS
    REPEATS = 0
    window.after_cancel(Timer)
    TEXT = ""
    label1.config(text="Timer", fg=GREEN)
    label2.config(text=TEXT)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global TEXT
    if REPEATS % 2 == 1:
        TEXT += "✔"
        label2.config(text=TEXT)
        if REPEATS % 7 == 0:
            count_down(LONG_BREAK_MIN*60)
            label1.config(text="BREAK", fg=RED)
        else:
            count_down(SHORT_BREAK_MIN*60)
            label1.config(text="BREAK", fg=PINK)

    else:
        count_down(WORK_MIN*60)
        label1.config(text="WORK", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count == 0:
        global REPEATS
        REPEATS += 1

    minutes = int(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > -1:
        global Timer
        Timer = canvas.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ----------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=220, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=2, column=2)

label1 = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label1.grid(row=1, column=2)

label2 = Label(text=TEXT, fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0)
label2.config(pady=10)
label2.grid(row=3, column=2)

start = Button(text="Start", command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=3, column=3)

window.mainloop()
