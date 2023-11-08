import pandas as pd #data analysis library
import random
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.resizable(False, False)
root.geometry('600x200')
root.title('Double Entendre Showdown')

df = pd.read_csv("prompts_ff.csv") #reads spreadsheet 

safe = df['Safe'].dropna()
safe_clean = safe.values.tolist()

danger = df['Danger'].dropna()
danger_clean = danger.tolist()

#random.choice(safe_clean) + '\n' + random.choice(danger_clean)

def setTextInput(text):
    textExample.configure(state="normal")
    textExample.delete(1.0, "end")
    textExample.insert(1.0, text)
    textExample.configure(state="disabled")

textExample = tk.Text(
    root,
    height=10
)
textExample.pack()

button = tk.Button(
    root,
    height="5",
    width="50",
    #bd="10",
    text="Generate New Prompt",
    command=lambda: setTextInput(random.choice(safe_clean) + '\n' + random.choice(danger_clean))
)
button.place(x=20, y=150)
button.pack()

root.mainloop()