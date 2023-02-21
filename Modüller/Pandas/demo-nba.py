import pandas as pd


df = pd.read_csv("datasets/youtube-ing.csv")

# İlk 10 kaydı getir
result = df.head(10)
# İkinci 5 kaydı getir
result = df[5:10]
# Datasette kolon isim ve sayıları
result = df.columns
result = len(df.columns)
# Aşağıda bulunan bazı kolonları silin 
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)
result = df
# # Beğenme ve beğenmeme sayılarının ortalaması
result = df["likes"].mean()
result = df["dislikes"].mean()
# İlk 50 video like ve dislike kolonları
result = df.head(50)[["title","likes","dislikes"]]
# En çok görüntülenen video
result = df[df["views"].max()==df["views"]][["title","views"]]
result = df[df["views"].max()==df["views"]]["title"].iloc[0]
# En az görüntülenen
result = df[df["views"].min()==df["views"]]["title"]
# En fazla görüntülenen ilk 10
result = df.sort_values("views",ascending=False)[["views","title"]].head(10)
# Kategoriye göre beğeni ortalamasıını sırala
result = df.groupby("category_id").mean("likes").sort_values("likes",ascending=False)
# Kategoriye göre yorum sayılarını sırala
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)
# Her kategoride kaç video vardır
result = df["category_id"].value_counts()
# Her videonun title uzunluğu b.ilgisini yeni bir kolonda gösteriniz
df["title_len"] = df["title"].apply(len)
# Her video için kullanılan tag bilgisini yeni bir kolonda gösteriniz
df["tag_count"]= df["tags"].apply(lambda x : len(x.split("|")))
# En popüler videolarını listeleyiniz (like/dislike oranına göre)
# df["popularity"] = df[df["likes"]/df["dislikes"]]

def popularity(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList)) 
    rateList = []

    for like,dislike in liste : 
        if (like + dislike) == 0:
            rateList.append(0)
        else:
            rateList.append(like/(like+dislike))

    return rateList

    print(liste)

df["ratelike"] = popularity(df)

print((df.sort_values("ratelike",ascending = False))[["title","likes","dislikes","ratelike"]])
# popularity(df)
# # print(df.columns)
# print(df)