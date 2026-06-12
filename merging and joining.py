import pandas as pd
df1= pd.DataFrame({
 "EmpID" : [1,2,3,4],
 "Name"   : ["ALice", "Bob", "Diana", "Charlie"]
})

df2= pd.DataFrame({
    "EmpID" :[1,2,3,5],
    "Salary" :[2500,3000,4500,5000]
})

#1. Inner Join-- only matching empids
inner= pd.merge(df1,df2, on= "EmpID", how= "inner")
print("INNER:\n", inner)

#2. Left Join-- all from df1 match from df2 if exists
left= pd.merge(df1,df2,on= "EmpID", how= "left")
print("LEFT:\n", left)

#3. Right join-- all from df2 match from d1 if exists
right= pd.merge(df1,df2,on= "EmpID", how= "right")
print("RIGHT:\n",right)

#4.outer join=everything from both
outer=pd.merge(df1,df2,on="EmpID", how= "outer")
print("OUTER:\n",outer)