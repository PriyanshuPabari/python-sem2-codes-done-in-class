#make a dataframe with name age city

import pandas as pd
names=["raghav","aniket"]
age=[0 ,18]
city=["amritsar","ghaziabad"]

df=pd.DataFrame({
    "names":names,
    "age":age,
    "city":city
})

print(df)

#filter_age=df[df["age"]>20]
#print(filter_age)

df["age"].fillna(df["age"].mean().astype(int))
print(df)