import ttkbootstrap as ttk
import tkinter
import pandas as pd
import random
from ttkbootstrap.constants import *
from tkinter import *

app = ttk.Window(themename="vapor")
app.resizable(False, False)
app.geometry('670x450')
app.title('Double Entendre Showdown')

'''
click_btn= PhotoImage(file='btn.png')
img_label= Label(image=click_btn)
'''

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
label.config(font=("Courier New CE", 20))

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

ttk.Label(prompt_frame, text="Prompt", font=("BIZ UDPGothic", 12, "bold")).pack(side="left", padx=5)
#ttk.Text(prompt_frame).pack(side="left", fill="x", expand=True, padx=5)

stl = ttk.Style()
stl.configure('C.TLabel',padding=[10,10,10,15], anchor="center")

stl.map('C.TLabel',
    foreground = [('pressed','grey'),('active','black')],
    background = [('pressed','!disabled','dark grey'),('active','light blue')],
    relief=[('pressed', 'sunken'),
            ('!pressed', 'raised')]
)

button_frame = ttk.Frame(app)
button_frame.pack(padx=5, pady=5, fill="x", anchor="center")
genButton = ttk.Button(button_frame,
           text="Generate New Prompt", 
           style='C.TLabel',
           command=lambda: setTextInput(random.choice(safe_clean) + '\n' + random.choice(danger_clean)),
           )
genButton.configure() #'''image = click_btn'''
genButton.pack()


app.mainloop()