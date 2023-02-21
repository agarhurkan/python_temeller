
def usalma(number) : 
    def inner(power):       
        
        return number**power
    return inner

number = input("Lütfen sayiyi giriniz: ")
power = input("Lütfen üs sayisini giriniz: ")

try:
    number = int(number)
    power = int(power)
    print(usalma(number)(power))


except Exception as ex: 
    print("Lütfen tam sayi giriniz!!",ex)



