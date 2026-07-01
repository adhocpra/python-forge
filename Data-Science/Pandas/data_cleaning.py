import pandas as pd
data= {
    "Name" :["Allice", "Bob", None, "alice", "Diana"],
    "Age" : [20, None, 21, 20,23],
    "Grade" :["A", "B","A", "A", "C"]
}
df= pd.DataFrame(data)
print(df)

#1.Drop missing value
df_clean= df.dropna()
print(df_clean)
print()
df_filled= df.fillna({"Name": "Unknown" , "Age":0})
print(df_filled)
print()
df_nodup= df.drop_duplicates()
print(df_nodup)
