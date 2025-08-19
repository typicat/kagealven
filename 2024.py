import pandas as pd


url = "https://kagealven.com/2025/02/2024/"
df = pd.read_html(url)[0]
df = df.fillna("")
df.to_csv("output_2024.csv", index=False, header=False)
