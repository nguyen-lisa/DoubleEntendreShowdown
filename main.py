import ttkbootstrap as ttk
import tkinter
import pandas as pd
import random
from ttkbootstrap.constants import *
from tkinter import *

#random prompt generator using ttkbootstrap

app = ttk.Window(themename="darkly")
app.resizable(True, True)
app.geometry('670x450')
app.title('Double Entendre Showdown')

click_btn= PhotoImage(file='btn.png')
img_label= Label(image=click_btn)

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
label.config(font=("Courier New CE", 20, "bold"))

def frameOne():
    #make a menu here
    vcmd = (app.register(app.callback))

    w = Entry(app, validate='all', validatecommand=(vcmd, '%P')) 
    w.pack()

def callback(self, P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

def frameTwo():
    prompt_frame = ttk.Frame(app)
    prompt_frame.pack(
        pady=5,
        padx=5,
        fill="x"
    )

    def setTextInput(text):
        textExample.configure(state="normal", font=("BIZ UDPGothic", 12))
        textExample.delete(1.0, "end")
        textExample.insert(1.0, text)
        textExample.configure(state="disabled")

    textExample = ttk.Text(
        app,
        height=5
    )
    textExample.configure(state="disabled")
    textExample.pack()

    promptLabel = ttk.Label(prompt_frame, text="Prompt", font=("BIZ UDPGothic", 12, "bold"))
    promptLabel.configure(anchor=W)
    promptLabel.pack(padx=5)
    #ttk.Text(prompt_frame).pack(side="left", fill="x", expand=True, padx=5)

    stl = ttk.Style()
    stl.configure('C.TLabel',padding=[-12,-12,-15,-12], anchor="center") #10,10,10,15

    stl.map('C.TLabel',
        foreground = [('pressed','grey'),('active','black')],
        background = [('pressed','!disabled','black'),('active','white')],
        relief=[('pressed', 'sunken'),
                ('!pressed', 'raised')]
    )

    button_frame = ttk.Frame(app)
    button_frame.pack(padx=10, pady=20, fill="x", anchor="center")
    genButton = ttk.Button(button_frame,
            text="Generate New Prompt", 
            style='C.TLabel',
            command=lambda: setTextInput(random.choice(safe_clean) + '\n' + random.choice(danger_clean)),
            )
    genButton.configure(image = click_btn) 
    genButton.pack()

app.mainloop()