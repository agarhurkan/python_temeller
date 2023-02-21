from datetime import datetime
from datetime import timedelta



simdi = datetime.now()

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = simdi.microsecond 
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y %B %A")

# Detay öğrenmek istersen google amcaya sor

t = "21 April 2019 hour 10:20:35"
# gun, ay , yil = t.split()
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
result = dt


birthday = datetime(1983,3,5,12,30,51)

result = datetime.timestamp(birthday) # Saniye
result = datetime.fromtimestamp(result) # Saniye to datetime
result = datetime.fromtimestamp(0) # 1970 başlangıç olarak kabul ediliyor

result = simdi-birthday # timedelta 

# result = result.days
# result = result.microseconds

result = simdi + timedelta(days=730, minutes=100)

result = simdi - timedelta(days=15)

print(result)

