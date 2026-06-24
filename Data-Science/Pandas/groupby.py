#groupby splits data into groups and apply agrregation to each groupss
#Aggregation -- Sum, mean, count 
#df.groupby("column")["other_column"].aggregation()

import pandas as pd

data= {
    "Name" : ["Alice", "Bob", "Alice", "Diana","Bob", "Diana"],
    "Department" : ["HR","IT", "HR","IT","IT", "HR"],
    "Salary" : [50000,4000,62000,6700,8000,9000]
}

df= pd.DataFrame(data)
print(df)
print()

#1.Average salary per department
print(df.groupby("Department")["Salary"].mean())
print()
#2.Total salary by department
print(df.groupby("Department")["Salary"].sum())
print()
#3.Count employees per department
print(df.groupby("Department")["Salary"].count())
print()

#4.Aggregations at once
print(df.groupby("Department")["Salary"].agg(["mean","sum","count"]))