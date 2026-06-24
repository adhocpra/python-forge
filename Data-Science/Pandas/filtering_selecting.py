
import pandas as pd

data= {
    "Name" : ["Alice", "Bob", "Diana", "Charlie", "Eva"],
    "Department" : ["HR", "IT", "IT", "HR", "IT"],
    "Salary" : [25000,400000,60000,45000,35000],
    "Age"        : [25,20,28,35,25]
    
}
df= pd.DataFrame(data)
print(df)
print("After")

#1. loc- select by label
print(df.loc[0])
print(df.loc[0,"Name"])
print(df.loc[0:2,["Name", "Salary"]])

#2. iloc-select by position
print(df.iloc[0])
print(df.iloc[0,1])
print(df.iloc[0:3, 0:2])

#3. Fiktering rows by conditiond
print(df[df["Salary"]>55000])
print(df[df["Department"]== "IT"])
df[(df["Department"]=="IT") & (df["Age"]<29)]