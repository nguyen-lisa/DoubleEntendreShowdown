import ttkbootstrap as ttk
import tkinter
import pandas as pd
import random
from ttkbootstrap.constants import *
from tkinter import *

app = ttk.Window(themename="superhero")
app.resizable(False, False)
app.geometry('650x350')
app.title('Double Entendre Showdown')

df = pd.read_csv("prompts_ff.csv") #reads spreadsheet 

safe = df['Safe'].dropna()
safe_clean = safe.values.tolist()

danger = df['Danger'].dropna()
danger_clean = danger.tolist()

label = ttk.Label(
    app,
    text="Double Entendre Showdown"
)
label.pack(pady=30)
label.config(font=("Arial", 20, "bold"))

prompt_frame = ttk.Frame(app)
prompt_frame.pack(
    pady=5,
    padx=5,
    fill="x"
)

def setTextInput(text):
    textExample.configure(state="normal", font=("Comic Sans", 12))
    textExample.delete(1.0, "end")
    textExample.insert(1.0, text)
    textExample.configure(state="disabled")

textExample = ttk.Text(
    app,
    height=5
)
textExample.configure(state="disabled")
textExample.pack()

ttk.Label(prompt_frame, text="Prompt").pack(side="left", padx=5)
#ttk.Text(prompt_frame).pack(side="left", fill="x", expand=True, padx=5)

button_frame = ttk.Frame(app)
button_frame.pack(pady=5, padx=5,fill="x")
ttk.Button(button_frame,
           text="Generate New Prompt",
           bootstyle="info",
           command=lambda: setTextInput(random.choice(safe_clean) + '\n' + random.choice(danger_clean))
           ).pack(padx=10)

app.mainloop()