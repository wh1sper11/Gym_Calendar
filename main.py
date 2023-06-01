from tkinter import *
import tkinter as tk
from datetime import date
from input import workout_func,userd,workout
import datetime




today =  userd 

win= Tk()
win.title('Workout of the day')
#win.attributes('-alpha', 1)  # Set window transparency to 80% (slightly transparent)
#win.wm_attributes("-transparentcolor","black")
#win.overrideredirect(1)


win.geometry("+600+280")

def workout_plan():
    current_day = datetime.datetime.today().weekday()
    # Calculate the workout index based on the current day
    workout_index = (current_day) % 7  # Offset the current day to align with the workout list
    work = workout[workout_index]
    label.config(text=work)


label = tk.Label(win,font=('Ariel 25 bold'),fg="white", bg="black")
label.grid(row=1,column=2,sticky='nsew')
label2 = tk.Label(win,text="Today's Workout",font=('Ariel 25 bold'),fg="white", bg="black")
label2.grid(row=0,column=2,sticky='nsew')
workout_plan()
win.wm_attributes('-toolwindow', 'True')
win.configure(bg='white')
win.mainloop()
