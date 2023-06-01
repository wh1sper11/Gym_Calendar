from tkinter import *
import tkinter as tk

def workout_func():
    workout = []
    for i, entry in enumerate(workout_entries):
        day = days[i]
        workout.append(f"{day}: {entry.get()}")

    print(workout)

win = Tk()
win.title('Workout Calendar')
win.geometry("800x400+600+280")

workout_labels = []
workout_entries = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

workout_label_main = tk.Label(win, text="Enter your workout routine", font=("Arial", 15, 'bold'))
workout_label_main.grid(row=0, column=1, pady=10)

for i, day in enumerate(days):
    label = tk.Label(win, text=day + ":", font=("Arial", 12))
    label.grid(row=i + 1, column=0)
    workout_labels.append(label)
    

    entry = tk.Entry(win, width=50)
    entry.grid(row=i + 1, column=1)
    workout_entries.append(entry)

Example = tk.Label(win, text="Examples:", font=("Arial", 12, 'bold'))
Example.grid(row=0, column=3, padx=10, sticky="w")

example_text = [
    "Monday: Cardio",
    "Tuesday: Weights/Push day",
    "Wednesday: Pull exercises/Weights",
    "Thursday: Rest",
    "Friday: Boxing or bike riding",
    "Saturday: Hiking or ab workout",
    "Sunday: Leg workout"
]

for i, text in enumerate(example_text):
    example_label = tk.Label(win, text=text, font=("Arial", 12))
    example_label.grid(row=i + 1, column=3, padx=10, sticky="w")

submit_button = Button(win, text="Submit", command=workout_func, width=10, font=("Arial", 12, 'bold'), bg='black', fg='white')
submit_button.grid(row=len(days) + 1, column=1, columnspan=2, pady=10)

win.mainloop()
