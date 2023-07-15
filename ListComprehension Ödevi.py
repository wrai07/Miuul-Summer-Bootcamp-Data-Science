
import seaborn as sns
df=sns.load_dataset("car_crashes")
print(df.columns)
print(df.dtypes)
#Görevin çözümü 1
df.columns=["NUM_" + col.upper() if df[col].dtype != 'O' else col.upper() for col in df.columns]
print(df.columns)
#Görev 2 çözümü
df.columns= [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
print(df.columns)
#Görev 3 çözümü
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if not(col in og_list)]
new_df = df[new_cols]
print(new_df.head())