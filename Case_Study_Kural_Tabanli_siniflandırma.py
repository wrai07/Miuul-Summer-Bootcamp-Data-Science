import pandas as pd
import numpy as np
import os
import seaborn as sns
#Görev1
df=pd.read_csv("persona.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.corr())
print(df.loc[:,["SOURCE","SEX","COUNTRY"]].value_counts())
#Görev2
print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())
#Görev3
print(df["PRICE"].nunique())
#Görev4
print(df["PRICE"].value_counts())
#Görev5
print(df["COUNTRY"].value_counts())
#Görev 6
print(df.groupby("COUNTRY").agg({"PRICE":"sum"}))
#Görev 7
print([df["SOURCE"].value_counts()])
#Görev8
print(df.groupby("COUNTRY").agg({"PRICE":"mean"}))
#Görev9
print(df.groupby("SOURCE").agg({"PRICE":"mean"}))
#Görev10
print(df.groupby(["SOURCE", "COUNTRY"]).agg({"PRICE":"mean"}))#

#Görev 2 kırılmadaki kazançlar
print(df.groupby(["COUNTRY", "SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}))
#Görev3 Price çıktısı
agg_df = df.groupby(["COUNTRY", "SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE", ascending = False)
print(agg_df)
#Görev4
agg_df = agg_df.reset_index()
print(agg_df)
#Görev5
araliklar = [0, 18, 23, 30, 40, 70]
agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=araliklar, labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
print(agg_df)
#Görev6
at_cols = ["COUNTRY","SOURCE","SEX","AGE_CAT"]
print(agg_df[at_cols])
agg_df["customers_level_based"] = [value_list[0].upper()+"_"+value_list[1].upper()+"_"+value_list[2].upper()+"_"+value_list[3] for value_list in agg_df[at_cols].values]
agg_df["PRICE"] = agg_df.groupby("customers_level_based")["PRICE"].transform("mean")
#Görev 7
segment = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
print(segment)
agg_df["SEGMENT"]=segment
print(agg_df)
print(
agg_df.groupby("SEGMENT").agg({"PRICE":["mean","max","sum"]}))
#Görev8
new_user = "TUR_ANDROID_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])
new_user = "FRA_IOS_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])



