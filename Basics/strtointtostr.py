try:
    x = input("Please enter a number for  x : ")
    y = input("Please enter a number for  y : ")


    

    length = max(len(x),len(y))
    lenmin = min(len(x),len(y))
    lendiff = length - lenmin

    

        



    """
    BURASI BIR STR TO INT TO STR SUM HESAP MODULU
    GELISTIRILECEKTIR!!!
    """
    
    if length == len(x):
        maxlen = len(x)
        for i in range(lendiff):
            y = ("0" +y)
    else:
        maxlen = len(y)
        for i in range(lendiff):
            x = ("0" + x)




    sum = ""
    hand = 0
    i = maxlen -1
    
    
    def strtoint(x,y):
        while i >= 0 :
            if (( int(x[i]) + int(y[i])) + hand) <= 9 : 
                sum = ((str(((int(x[i]) + int(y[i])) + hand)%10))+sum)
                hand = 0 
                
            else : 
                sum = ((str(((int(x[i]) + int(y[i])) + hand)%10))+sum)
                hand = 1
                
            i -= 1
    
    if length == len(x):
        maxlen = len(x)
        print(f"Max Len Uzunlugu X Sayisindadir ve Uzunlugu: {maxlen}'dir ")

       
    else:
        maxlen = len(y)
        print(f"Max Len Uzunlugu Y Sayisindadir ve Uzunlugu: {maxlen}'dir ")
        

    # # print(help(list.append))
    print(x)
    print(y)
    print("++++")
    print("______")
    print("Toplam sayi :", sum,"\n")

except Exception as Ex: 
    print("X ve Y sayilari icin sadece RAKAM giriniz . Hata kodu: ", Ex )
finally:
    print("Modül sonlandirildi.")
    

    

