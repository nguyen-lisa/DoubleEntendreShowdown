import pandas as pd #data analysis library
import random

df = pd.read_csv("prompts_ff.csv") #reads spreadsheet 

safe = df['Safe'].dropna()
safe_clean = safe.values.tolist()

danger = df['Danger'].dropna()
danger_clean = danger.tolist()

print(random.choice(safe_clean) + random.choice(danger_clean))