import pandas as pd
df= pd.read_csv('titanic.csv')
#explore (first step)
df.shape
df.info
df.isnull().sum()
df.describe()

#handle missing value (second step)
#small missing numbers- fill with median (numeric) & small mssing text- mode, 50% >>more-drop
#1.Fill missing age with median
df['Age']=df['Age'].fillna(df['Age'].median())
#2.Fill missing value of Embarked with mode
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
#3.Drop Cabin column-- missing vakalues
df=df.drop(columns= ['Cabin'])
print('\nMissing after fix:')
print(df.isnull().sum())

#duplicates
print("\nBefore duplicates:" ,len(df),"rows")
df= df.drop_duplicates()
print("After duplicates:",len(df),"rows" )
# #string- Name column
# print("\nSample names:")
# print(df['Name'].head(10))
# #str.extract- Pulls pattern and regrex
# df['Title']= df[]

#data types
print("\nBefore fixing types:")
print(df.dtypes)
#convert survived to category
df['Survived'] = df['Survived'].astype('category')
#convert pclass to category
df['Pclass']=df['Pclass'].astype('category')
#convert sex t=o category
df['Sex']=df['Sex'].astype('category')
#convert embarked to category
df['Embarked']=df['Embarked'].astype('category')

print("\nAfter fixing types:")
print(df.dtypes)

#String Cleaning-using extract and regrex
df['Title'] = df['Name'].str.extract(r',\s*([A-Za-z]+)\.')
#r'...'- ignore special character , look for comma skip spaces after cooma(capture)
print("\nTitle found:")
print(df['Title'].value_counts())

#clean-group rare titles to 'other'
df['Title']= df['Title'].replace(['Master','Dr','Rev', 'Col','Major','Ms', 'Sir','Lady','Capt','Don',"Mlle",'Jonkheer','Mme'],
'Other'
)
print("\nCleaned titles:")
print(df['Title'].value_counts())

#Feature Engineering
#create family size column
df['FamilySize']= df['SibSp']+df['Parch']+1 #siblings+parent/children+1= family on board
#is_alone?
df['IsAlone']= (df['FamilySize']==1).astype(int)
#create age group
df['AgeGroup']= pd.cut(df['Age'],bins= [0,12,18,35,60,100], #pd cut splits continuous number into defined groups bins
labels=['Child','Teen', 'Adult','Middle','Senior'])

print("\nFamily size distribution: ")
print(df['FamilySize'].value_counts())

print("\nTraveling alone:")
print(df['IsAlone'].value_counts())

print("\nAge groups:")
print(df['AgeGroup'].value_counts())


#saving clean file
df.to_csv('titanic_cleaned.csv', index=False)
print("\nNew file!")
print("Final shape:", df.shape)
print("\nFinal Columns:")
print(df.columns.tolist())
print("\nSample of cleaned data:")
print(df.head())