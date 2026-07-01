import pandas as pd

data = {
    "Product" : ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price"   : [999, 499,299,199],
    "Stock"   : [10,25,15,9]
}

df= pd.DataFrame(data)
print(df)

df["Category"] = ["Electronics", "Electronics", "Electronics,", "Electronics"]
print(df)

filter= df[df["Price"]>300]
print(filter)

price_sort= df.sort_values(by="Price")
print(price_sort)

price_sort.to_excel("stock.xlsx", index= False)
print("saved!")