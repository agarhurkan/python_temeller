


def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    studentName = liste[0]
    notlar = liste[1]

    notlar = notlar.split(",")
    not1 = int(notlar[0])
    not2 = int((notlar[1]))
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >=85 and ortalama <=100 :
        harfNotu = "AA"
    elif ortalama <85 and ortalama >=60:
        harfNotu = "BB"
    else :
        harfNotu = "FF"
    
    return studentName + ": " + harfNotu + "\n"






def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file :
            print(not_hesapla(satir))

def not_gir():
    name = input("Öğrenci adi: ")
    surname = input("Öğrenci soyadi: ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")

    with open ("sinav_notlari.txt","a",encoding=("utf-8")) as file:
        file.write(name+" "+ surname+":"+not1+","+not2+","+not3+"\n")


def notlari_kayitet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file : 
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2 :
            for i in liste : 
                file2.write(i)
            

             



while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")
    if islem =="1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitet()
    else:
        break



    