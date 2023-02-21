
import requests
import json


class user :

    def __init__(self,usarname,password,email):
        self.username = usarname 
        self.password = password
        self.email = email

class userWork :
    def __init__(self):
        self.users = []
        self.loggedIn = False
    

    def kullanici(self,user):
        pass # User karşılama
        
    
    def login(self):
        pass

    def register(self,user):
        pass





class doviz:

    def __init__(self,base,to):
        self.base = base
        self.to = to


    def tekliDoviz(self):
        url = "https://v6.exchangerate-api.com/v6/f2f4abcc3fd169179044462f/latest/"
        url = url + base
        url = requests.get(url)
        data =json.loads(url.text)

        dovizler = data["conversion_rates"]
        # result=json.loads(result)

        for i in dovizler:
            a = 0
            if i == to :
                a += 1 
                print(  1,"",base,"=",dovizler[i],"",i)
                break
       
        if a == 0 :
            print("Aradiginiz doviz cinsi bulunamadi .!")

    def tumDovizler(self):
        url = "https://v6.exchangerate-api.com/v6/f2f4abcc3fd169179044462f/latest/"
        url = url + base
        url = requests.get(url)
        data =json.loads(url.text)

        dovizler = data["conversion_rates"]
        # result=json.loads(result)

        for i in dovizler:
            print(1,"",base,"=",dovizler[i],"",i)

       
            
           



        
        


while True:
    print("\n")
    print("MENÜ".center(50,"*"))
    choose = input("\nLütfen menüdeki seçeneklerden birini seçiniz : \n1- Doviz Hesabi Yapmak\n2- Guncel Tekli Doviz Goruntuleme\n3- Guncel Tum Dovizleri Goruntulume\n4- Cikis Yapmak\n\nLutfen birini seciniz:  ")
    if choose == "1" :
        username = input("Lütfen kullanici adinizi giriniz:")
        password = input("Lütfen sifrenizi giriniz:")
        

        # kullanici(username)
    elif choose == "2" :
        base = input("Çevirmek istediğiniz dovizin kisaltmasini giriniz(Example:CAD) : ")
        to = input("Lütfen çevirilicek doviz cinsini giriniz :")
        to= to.upper()
        base = base.upper() 
        dcinsi = doviz(base,to)
        dcinsi.tekliDoviz()
    elif choose == "3" : 
        base = input("Çevirmek istediğiniz dovizin kisaltmasini giriniz(Example:CAD) : ")
        base = base.upper()
        to = ""
        to= to.upper()
        dcinsi = doviz(base,to)
        dcinsi.tumDovizler()

    elif choose == "4" : 
        break    
    else :
        print("\nLutfen seceneklerden biriniz giriniz !")