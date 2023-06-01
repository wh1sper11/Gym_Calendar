from tkinter import *
import tkinter as tk
from datetime import date
from tkinter import messagebox

win= Tk()

win.title('Workout Calendar')

win.geometry("800x400+600+280")

workout = []


def workout_func():
    
    for i, entry in enumerate(workout_entries):
        day = days[i]
        workout_text = entry.get()
        if workout_text == '':
            messagebox.showwarning("Empty Workout", f"You need to fill in the workout for {day} before saving!")
            return

    res = messagebox.askquestion('Save Confirmation', 'Save the desired workout plan?')
    if res == 'yes':
        for i, entry in enumerate(workout_entries):
            day = days[i]
            workout_text = entry.get()
            workout.append(f"{workout_text}")
    elif res == 'no':
        print("User cancelled without saving")
        return
    else:
        print("Invalid response from user")
        return

    print(workout)
    win.destroy()



userd = date.today()
#variables for the columms

workout_label_main = tk.Label(win, text="Enter your workout routine",font=("Ariel",15,'bold'))
workout_label_main.grid(row=0, column=1,pady=10)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
workout_labels = []
workout_entries = []
for i , day in enumerate(days):
    label = tk.Label(win, text=day + ":", font=("Arial", 13,'bold'))
    label.grid(row=i + 1, column=0,sticky='e')
    workout_labels.append(label)
    

    entry = tk.Entry(win, width=50)
    entry.grid(row=i + 1, column=1)
    workout_entries.append(entry)



example_text = [
    "Monday: Cardio",
    "Tuesday: Weights/Push day",
    "Wednesday: Pull exercises/Weights",
    "Thursday: Rest",
    "Friday: Boxing or bike riding",
    "Saturday: Hiking or ab workout",
    "Sunday: Leg workout"]

for i, text in enumerate(example_text):
    example_label = tk.Label(win, text=text, font=("Arial", 12))
    example_label.grid(row=i + 1, column=3, padx=10, sticky="w")



submit_button = Button(win, text="Submit", command=workout_func,width=10,font=("Arial", 12,'bold'),bg='black',fg='white')
submit_button.grid(row=9, column=1, columnspan=2, pady=10)

win.mainloop()