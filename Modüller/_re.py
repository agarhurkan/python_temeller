import re

result = dir(re)

# regular expression

str = "Python Kursu : Python Programlama Rehberiniz | 40 saat"

# result = re.findall("Python",str) # Bu kelimeyi bul
# result = len(result) # Bulduğun kelimeden kaç tane var

# result = re.split(" ", str)
# result = re.split("r",str)

# result = re.sub(" ", "-", str) # Değiştirme işlemi
# result = re.sub("\r", "-", str) # Değiştirme işlemi


# result = re.search("Python",str) 
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.string

# result = re.findall("[sat]",str)
# result = re.findall("[PpCca]",str)
# result = re.findall("[^Phon]",str)   # ^ İŞARETİ HARİÇ DİĞERLERİ DEMEKTİR

# result = re.findall("^P",str)  # Liste içerisinde değilse ^ işareti başlangıç sorgulama demektir

# Belirtilen karakterle bitiyor mu ?
"""" 
a$ => a : 1 match
   => lamba : 1 match
   => Python : No match

"""


result = re.findall("t$",str)

"""" 
ma*n => mn : 1 match
   => man : 1 match
   => maaan : 1 match
   => main : 0 match

"""


result = re.findall("sa*t",str)

"""
DETAYLARA İNTERNETTEN BAK VEYA BTKAKADEMİ  
https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877

15.3 Ders


"""

result = re.sub("\s","",str)
 



print(result)



