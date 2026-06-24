#creating the first table
import pandas as pd
#pd.dataframe turns into a table
data= {
    "Name" : ["alice", "bob", "charlie"],
    "Age"  : [20,21,22],
    "city" : ["NY", "KTM", "BRT"]
}

df =pd.DataFrame(data)
print(df)


#viewing a single column
print(df["Name"])
print(df["Age"])

#viewing single row
#iloc= index location
print(df.iloc[0]) #first row
print(df.iloc[1])

#add column
df["Country"]=["USA","Nepal", "Nepal"]
print(df)

df["Grade"]=["A","B","C"]
print(df)

#Filter Rows
filtered= df[df["Age"]>20]
print(filtered)

new= df[df["Grade"]=="A"]
print(new)

a= df[df["city"]=="KTM"]
print(a)

#sorting table
#1.sorting by age
#youngest to oldest-- ascending
sorted_df= df.sort_values(by="Age")
print(sorted_df)

#oldest t youngest-- flip
sort_1= df.sort_values(by= "Age", ascending= False)
print(sort_1)

#grade
sort_2= df.sort_values(by="Grade")
print(sort_2)

sort_3= df.sort_values(by= "Grade", ascending=False)
print(sort_3)

#sort by columns: Name

sort_column =df.sort_values(by= "Name")
print(sort_column)

