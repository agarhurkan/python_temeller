import pandas as pd

# df = pd.DataFrame()""
# df = pd.DataFrame([1,2,3,4])

list = ([["Ahmet",50],["Ali",60],["Yağmur",80],["Çınar",90]])
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}



# df = pd.DataFrame(list, columns=["Name","Grade"],index=[1,2,3,4])
df = pd.DataFrame(dict,index=[212,232,568,542])


print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)