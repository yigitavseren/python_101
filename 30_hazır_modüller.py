#YÖNTEM 1
#import math
#import math as islem #takma isim de verebiliriz

#value = dir(math) #modüldeki bütün her şeyi gösteriri
#value = help(math) #onları açıklar
#value = help(math.factorial) #twk bir fonksiyonu açıklar
#value = math.sqrt(49)
#value = math.factorial(5)
#value = math.floor(5.9)
#value = math.ceil(5.9)
#value = islem.factorial(5)

#YÖNTEM 2
#from math import * # her şeyi math oluyor

from math import factorial,sqrt #sadece seçili olanları yapar
def sqrt(x):
    print('x :'+ str(x))
#value = factorial(5)
value = sqrt(9)
#value = ceil(5.9)
#ilgili fonksiyonlardan hangisi en son tanımalrsa onu takar sistem mesela burda en son yazdığımız fonksiyon etkili oldu
print(value)