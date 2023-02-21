import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])


# result = df
# result = df["Column1"]
# result = type(df["Column1"])
# result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[":","column"]


result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[2,2] # iloc indexe göre görüntüleme yapar
# result = df.loc [:,["Column1","Column2"]]
# result = df.loc [:,"Column1":"Column3"]

df["Column4"] = pd.Series(randn(3),["A","B","C"])
df["Column5"] = df["Column1"] + df["Column4"]

df.drop("Column5",axis=1 , inplace=False ) 
# Drop kodu inplace eşitti true iken maini değiştirir
# inplace eşittir false iken sadece kendi bağlı olduğu kopyasını değiştirir.



print(df)
