import pandas as pd

df= pd.read_csv("students.csv")
print(df)
print()
df = pd.read_excel("stock.xlsx")
print(df)

#commands
print(df.shape)
print(df.columns)
print(df.head(2))
print(df.tail(2))
print(df.info())