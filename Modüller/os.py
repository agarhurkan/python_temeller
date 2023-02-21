import os

result = dir(os)

# result = os.name # İşletim sistemi

# os.chdir("C:\\") # Konum değişir 
# os.chdir("../../..") # Mevcut konumdan geriye gider klasör olarak

# os.mkdir("newdirectory") # Klasör içerisine oluşturur
# os.makedirs("C:\\newdirectory/yeniklasor") #Klasör içerisine klasör oluşturur


# result = os.getcwd() # Hangi Klasör içerisinde olduğunu gösterir.

# listeleme
# result  = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

# result = os.stat("datetime1.py")


import datetime


# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) #Oluşturulma tarihi create
# result = datetime.datetime.fromtimestamp(result.st_atime) #Son erişilme tarihi access
# result = datetime.datetime.fromtimestamp(result.st_mtime) #Değiştirilme tarihi modify
 

# os.system("notepad.exe") # Klasör açar

# os.rename("newdirector","yeniklasor") #Klasör ismi değiştirir
# os.rmdir("newdirectory") # Klasör siler
# os.removedirs("yeniklasor") # Yine siler

# path #uzantı ile yapılır
 
# result = os.path.abspath("os.py")
# result = os.path.dirname(f"{result}")


result = os.path.dirname(os.path.abspath("os.py"))

result = os.path.exists(os.path.abspath("os.py"))
result = os.path.isdir(os.path.abspath("os.py"))
result = os.path.isfile(os.path.abspath("os.py"))

result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("os.py")
# result = result[0]
# result = result[1]


print(result)
 