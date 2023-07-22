import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Görev1
df=sns.load_dataset("Titanic")
print(df)
#Görev2
df.info()
print("Erkek ve kadın yolcuların sayısı")
print(df["sex"].value_counts())
#Görev3
print("Her sutuna ait unique değerlerin sayısını bulunuz")
print(df.nunique())
#Görev4
print("pclass değişkeninin unique değerlerinin sayısını bulunuz")
print(df["pclass"].nunique())
print(df["pclass"].value_counts())
#Görev5
print("pclass değişkeninin ve parch değişkeninin unique değer sayısı :",df[["pclass","parch"]].nunique())
#Görev6
print("embarked değişkeninin tipini kontrol ettim ve tipini category olarak değiştirdim ayrıca kontrol ettim")
print(df["embarked"].dtype)
df["embarked"]=df["embarked"].astype("category")
print(df["embarked"])
#Görev7
print("embarked değeri C olan tüm bilgilerini gösterdim.")
print(df.loc[df["embarked"]=="C"])
#Görev8
print("embarked değeri S olmayanların tüm bilgilerini gösterdim.")
print(df.loc[df["embarked"]!="S"])
#Görev9
print("görev9")
print((df[(df['age']<30) & (df['sex']=='female')]))
#Görev10
print("görev10")
print(df[(df['fare']>500) | (df['age']>70)])
#Görev11
print("boş ifadeleri topladım")
print(df.isnull().sum())
#Görev12
df.drop('who', axis='columns', inplace=True)#who kolomunu  çıkardım
print(df.info())
#Görev 13
df['deck'].fillna(df['deck'].mode()[0], inplace=True)

print(df['deck'])
#Görev14
df['age'].fillna(df['age'].median(), inplace=True)
#Görev15
print(df.groupby(['pclass','sex']).agg({'survived':['sum','count','mean']}))
#Görev16
df['age_flag'] = df['age'].apply(lambda x: 1 if x<30 else 0)
df.head()
#Görev17
tip_df = sns.load_dataset('tips') # Task-17: Define the tips data set from the Seaborn library.
print(tip_df.head())
#Görev18
print(tip_df.groupby('time').agg({'total_bill':['min','max','mean']}))
#Görev19
print(tip_df.groupby(['day','time']).agg({'total_bill':['min','max','mean']}))
#Görev20
print(tip_df.head())
print(tip_df[(tip_df['time']=="Lunch") & (tip_df['sex'] == "Female")].groupby(['day']).agg({'total_bill':['min','max','mean'],'tip':['min','max','mean']}))
#Görev21
print(tip_df.loc[(tip_df['size']<3) & (tip_df['total_bill']>10), :].mean(numeric_only=True))
#Görev22
tip_df['total_bill_tip_sum'] = tip_df['total_bill'] + tip_df['tip']
print(tip_df.head())
#Görev23
new_titanic_df = tip_df.sort_values(by="total_bill_tip_sum", ascending=False)[:30]
print(new_titanic_df)
