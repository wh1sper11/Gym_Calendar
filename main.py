from tkinter import *
import tkinter as tk
from datetime import date
from input import workout_func, workout


workout = workout


today = date(2023, 5, 31)

win= Tk()
win.title('')
#win.attributes('-alpha', 1)  # Set window transparency to 80% (slightly transparent)
#win.wm_attributes("-transparentcolor","black")
#win.overrideredirect(1)
win.geometry("500x150+3300+100")

def workout_plan():
    days_since_start = (date.today() - today).days
    workout_index = days_since_start % len(workout)
    #work = "Today's Workout:" +"\n"+ workout[workout_index]
    work = workout[workout_index]
    label.config(text=work)
    label.place(relx = 0.14,
                rely = 0.8,
                anchor= 'sw')
    

label = tk.Label(win,font=('Ariel 25 bold'),fg="white", bg="black")
label.pack()
label2 = tk.Label(win,text="Today's Workout:",font=('Ariel 25 bold'),fg="white", bg="black")
label2.pack()
workout_plan()
win.wm_attributes('-toolwindow', 'True')
win.configure(bg='white')
win.mainloop()
