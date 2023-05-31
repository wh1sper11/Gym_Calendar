from tkinter import *
import tkinter as tk
from datetime import date

win= Tk()
win.title('Workout Calendar')

win.geometry("800x400+600+280")


def workout_func():
    workout.append(workout_entry1.get())
    workout.append(workout_entry2.get())
    workout.append(workout_entry3.get())
    workout.append(workout_entry4.get())
    workout.append(workout_entry5.get())
    workout.append(workout_entry6.get())
    workout.append(workout_entry7.get())

    print(workout)

workout = []

#variables for the columms

workout_label_main = tk.Label(win, text="Enter your workout routine",font=("Ariel",15,'bold'))
workout_label_main.grid(row=0, column=1,pady=10)


workout_label1 = tk.Label(win, text="Monday:", font=("Arial", 12))
workout_label1.grid(row=1, column=0)
workout_entry1 = tk.Entry(win,width=50)
workout_entry1.grid(row=1, column=1)

workout_label2 = tk.Label(win, text="Tuesday:", font=("Arial", 12))
workout_label2.grid(row=2, column=0, padx=10,pady=5)
workout_entry2 = tk.Entry(win,width=50)
workout_entry2.grid(row=2, column=1)

workout_label3 = tk.Label(win, text="Wednesday:", font=("Arial", 12))
workout_label3.grid(row=3, column=0, padx=10,pady=5)
workout_entry3 = tk.Entry(win,width=50)
workout_entry3.grid(row=3, column=1)

workout_label4 = tk.Label(win, text="Thursday:", font=("Arial", 12))
workout_label4.grid(row=4, column=0, padx=10,pady=5)
workout_entry4 = tk.Entry(win,width=50)
workout_entry4.grid(row=4, column=1)

workout_label5 = tk.Label(win, text="Friday:", font=("Arial", 12))
workout_label5.grid(row=5, column=0, padx=10,pady=5)
workout_entry5 = tk.Entry(win,width=50)
workout_entry5.grid(row=5, column=1)

workout_label6 = tk.Label(win, text="Saturday:", font=("Arial", 12))
workout_label6.grid(row=6, column=0, padx=10,pady=5)
workout_entry6 = tk.Entry(win,width=50)
workout_entry6.grid(row=6, column=1)

workout_label7 = tk.Label(win, text="Sunday:", font=("Arial", 12))
workout_label7.grid(row=7, column=0, padx=10,pady=5)
workout_entry7 = tk.Entry(win,width=50)
workout_entry7.grid(row=7, column=1)

workout_label1 = tk.Label(win, text="Monday:", font=("Arial", 12))
workout_label1.grid(row=8, column=0, padx=10,pady=5)
workout_entry1 = tk.Entry(win,width=50)
workout_entry1.grid(row=8, column=1)


Example = tk.Label(win, text="Examples:", font=("Arial", 12,'bold'))
Example.grid(row=0, column=3,padx=10, sticky="w")

Example = tk.Label(win, text="Monday: Cardio", font=("Arial", 12))
Example.grid(row=1, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Tuesday: Weights/Push day ", font=("Arial", 12))
Example.grid(row=2, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Wednesday: Pull exercises/Weights", font=("Arial", 12))
Example.grid(row=3, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Thursday: Rest", font=("Arial", 12))
Example.grid(row=4, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Friday: Boxing or bike riding", font=("Arial", 12))
Example.grid(row=5, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Saturday: Hiking or ab workout", font=("Arial", 12))
Example.grid(row=6, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Sunday: Leg workout", font=("Arial", 12))
Example.grid(row=7, column=3,padx=10,sticky="w")

Example = tk.Label(win, text="Rest: Its important to rest twice within 8 days! ", font=("Arial", 12),fg='red')
Example.grid(row=8, column=3,padx=10,sticky="w")

submit_button = Button(win, text="Submit", command=workout_func,width=10,font=("Arial", 12,'bold'),bg='black',fg='white')
submit_button.grid(row=9, column=1, columnspan=2, pady=10)
win.mainloop()