import pandas as pd

data = pd.read_csv("data/example.csv")

print("Lab 1 analysis ran successfully.")
print(f"Rows: {len(data)}")
print(f"Mean value: {data['value'].mean():.2f}")
