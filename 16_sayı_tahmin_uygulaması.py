import random

sayi = random.randint(1,100)
hak = 5
sayac = 1
while (hak > 0):
    hak -= 1
    sayac += 1
    tahmin =int(input('Bir sayı giriniz: '))
    if(tahmin == sayi):
        print(f'Tebrikler{sayac}defada bildin.Toplam puanınız: {100 - (20) * (sayac)}')
        break
    elif(tahmin<sayi):
        print('Girdiğin sayı küçük daha büyük bir sayı yaz ibiş ')
    else:
        print('Girdiğin sayı büyük daha küçük sayı yaz la')
    if (hak == 0):
        print(f'Oyunu kaybettin.Tutulan sayı: {sayi}')       