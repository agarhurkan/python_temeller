
# plakalar = [41,34]
# sehirler = ["kocaeli","istanbul"]

# # plaka şehir eşleştirmesini elle yapmak yerine bunu karşılıklı 
# # anlaşılabilecek bir duruma çevirelim o da aşağıdaki gibi yapılmaktadır.

# yeniPlakalar = {"kocaeli" : 41, "istanbul" : 34}

# print(yeniPlakalar)
# print(yeniPlakalar["istanbul"])

# yeniPlakalar["ankara"] = 6

# print(yeniPlakalar)

import my_projects.bookwriter as bookwriter

Result  = bookwriter.Chatbot("Nasılsın")
print(Result)