import pandas as pd

df = pd.DataFrame({
    "Full_Name" :["Alice Smith", "Bob Jones", "Charlie Brown", "Evan Patrick Vaverka"]
})

split =df["Full_Name"].str.split(" ", expand = True)

df["Part1"]= split[0].fillna("")
df["Part2"]= split[1].fillna("")
df["Part3"]= split[2].fillna("")

print(df[["Part1", "Part2","Part3"]])