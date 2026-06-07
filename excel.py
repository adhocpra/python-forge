import pandas as pd 
data= {
    "Name" : ["alice", "bob", "charlie"],
    "Age"  : [20,21,22],
    "city" : ["NY", "KTM", "BRT"]
}

df= pd.DataFrame(data) #converting to table

df["Country"]= ["USA","Nepal","Nepal"]
df["Grade"] = ["A","B", "C"]
print(df)

sorted_column= df.sort_values(by= "Name")

#to excel
sorted_column.to_excel("test.xlsx", index= False)
print("File saved")

#string splitting

df = pd.DataFrame({
    "Full_Name" : ["Alice Smith", "Bob Jones", "Charlie Brown"]
})

print (df["Full_Name"].str.split(" ")) #gives list

#expand  (into separate columns)

split = df["Full_Name"].str.split(" ", expand=True)
print(split)

#name columns
df["Part 1"]= split[0]
df["Part 2"] = split[1]
print(df)
