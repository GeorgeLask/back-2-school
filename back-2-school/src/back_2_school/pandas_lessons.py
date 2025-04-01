import pandas as pd

df = pd.read_csv('src/back_2_school/data.csv')
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isna().sum())

print(df[['Age','Gender']])