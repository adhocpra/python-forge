import pandas as pd

data ={
    "Full_Name" : ["Alice Smith","Evan" ,"Evan P. Veverka", "E.Vaverka", "Evan V."],
    "Material"  : ["Wood", "Metal", "Glass","Wood", "Glass"],
    "Shipping"  : ["Store", "Shipped", "Store", "Shipped", "Store"]
}

df= pd.DataFrame(data)

#splitname
split= df["Full_Name"].str.split(" " ,expand=True)

df["Part1"]= split[0].fillna("")
df["Part2"]= split[1].fillna("")
df["Part3"]= split[2].fillna("")

#result-table
result= df[["Part1", "Part2", "Part3", "Material", "Shipping"]]

#sort by material
output= result.sort_values(by="Material").reset_index(drop=True)
print(output)

#into excel
output.to_excel("fanxy_names.xlsx", index=False)
print("Saved!")