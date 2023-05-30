from tkinter import *
import tkinter as tk
from datetime import date


workout = ['Push day [Body weight]',
           'Pull day [Body weight]',
           'Leg day [Body weight]',
           'REST :)',
           'Push day [Weights]',
           'Pull day [Weights]',
           'Leg day [Weights]',
           'REST :)']

today = date(2023, 5, 30)

win= Tk()
win.title("Clock")
win.attributes('-alpha', 1)  # Set window transparency to 80% (slightly transparent)
win.wm_attributes("-transparentcolor","black")
win.overrideredirect(1)
win.geometry("+3300+100")

def workout_plan():
    days_since_start = (date.today() - today).days
    workout_index = days_since_start % len(workout)
    work = "Today's Workout:" +"\n"+ workout[workout_index]
    label.config(text=work)

label = tk.Label(win,font=('Ariel 30 bold'),fg="white", bg="black")
label.pack()
workout_plan()
win.mainloop()
