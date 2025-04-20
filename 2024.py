import pandas as pd


url = "https://kagealven.com/2025/02/2024/"
data = pd.read_html(url)
df = data[0]

df = df.fillna('')
df.to_csv('output_2024.csv', index=False, header=False)
