import pandas as pd
df=pd.read_csv("students.csv")
print(df)
print(df.info())
#checking missing values
print("/n        MISSING VALUES BEFORE CLEANING    ")
print(df.isnull().sum())
#filling missing  value with mean
df["AGE"]=df["AGE"].fillna(df["AGE"].mean())
print("DATA AFTER FILLING MISSING VALUES WITH MEAN")
print(df)
#remove duplicates
df=df.drop_duplicates()
print("DATA AFTER REMOVING DUPLICATES ")
print(df)
#CHECK DATA TYPES
print("DATA TYPES")
print(df.dtypes)
df.to_csv("cleaned_students.csv",index=False)
print("\ncleaned dataset saved successfully!")
print("FINLA CHECK")
#check missing values
print("missing values")
print(df.isnull().sum())
print("duplicate rows")
print(df.duplicated().sum())
#show final data
print("final  cleaned data")
print(df)