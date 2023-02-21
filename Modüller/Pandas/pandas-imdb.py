import pandas as pd

df =pd.read_csv("IMDB.csv")





# Dosyada hakkındaki bilgiler
result = df
result = df.columns
result = df.info
# İlk 5 kaydı göster
result = df.head()
# İlk 10 kaydı göster
result = df.head(10)
# Son 5 kaydı göster
result = df.tail()
# Son 10 kaydı göster
result = df.tail(10)
# Sadece Title Kolonunu alın
result = df["Title"]
# Sadece Title Kolonunun ilk 5 kaydı
result = df["Title"].head()
# Title ve Rating ilk 5 
result = df[["Title","imdbRating"]].head()
# Title ve Rating son 7
result = df[["Title","imdbRating"]].tail(7)
# Title ve Rating ikinci 5  
result = df[5:10][["Title","imdbRating"]]
# Title ve Rating ve imdb > 8 ilk 50 
result = df[["Title","imdbRating"]][df["imdbRating"] >= 8.0].head(50)
# Yayın tarihi 2014 ile 2015 arasında filmlerin ismi
result = df[(df["Year"]>=2014) & (df["Year"]<2016)][["Title","Year","imdbRating"]]
# Değerlendirme  100k dan büyük olan yada imdb 8 ile 9 arası
# result = df[(([df["imdbVotes"]>100000]) | (([df["imdbRating"] >=8]) & ([df["imdbRating"]<=9]))) ]
df["imdbVotes"].apply(int) 
result = df[df["imdbVotes"]>100000]
#







print(result)