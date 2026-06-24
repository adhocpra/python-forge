import pandas as pd
import os
#create a messy data
import pandas as pd

# Step 1: Create the messy data
data = {
    'Name':       ['Alice Johnson', 'bob smith', 'Carol White', 
                   'David Brown', 'Alice Johnson', 'frank wilson',
                   'Grace Moore', 'Henry Taylor', 'James Thomas', 'bob smith'],
    'Age':        [28, 32, 25, 45, 28, None, 31, 27, 29, 32],
    'Email':      ['alice@email.com', 'BOB@EMAIL.COM', 'carol@email.com',
                   'david@email.com', 'alice@email.com', 'frank@email.com',
                   'grace@email.com', 'HENRY@EMAIL.COM', 'james@email.com', 'BOB@EMAIL.COM'],
    'Salary':     [55000, 62000, 48000, None, 55000, 43000, 
                   58000, 52000, 'james_salary', 62000],
    'Department': ['Engineering', 'marketing', 'Engineering', 'Sales',
                   'Engineering', 'HR', 'Marketing', 'Sales', 'Sales', 'marketing']
}

df = pd.DataFrame(data)

# Save as messy CSV
df.to_csv('messy_data.csv', index=False)
print("Messy data created!")
print(df)

#reading and inspecting 
df= pd.read_csv('messy_data.csv')
#see details
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("n\Column info:")
print(df.info())

#cleaning the data

#1.stripping extra spaces from Name and add capitalization on Name
df['Name']= df['Name'].str.strip().str.title()
#2. Stanndardize Department  capitalization
df['Department']= df['Department'].str.strip().str.title()
#3.Lower case email
df['Email']=df['Email'].str.lower().str.strip()

print("After fixing texts:")
print(df[['Name','Email','Department']])

#2.Searching,Splitting and Exctracting
df['Name']= df['Name'].str.replace(" ","")
print(df['Email'].str.contains('@gmail')) #searching
print(df['Name'].str.startswith('A'))
print(df['Name'].str.endswith('son'))
print(df['Name'].str.len())

#splitting into list
print(df['Name'].str.split('  '))
print(df['Name'].str.split(' ').str[0])
print(df['Email'].str.split('@').str[1])