#def changename(n):        #Ben Ada tanımlamıştım fonksiyonda ama sonradan verdiğim yiğit değeri çıktı olarak gösterildi
#    n = 'Ada'
#name = 'Yiğit'
#changename(name)
#print(name)    

#def change(n):
#    n[0] = 'İstanbul'

#sehirler = ['Ankara','İzmir']
#n = sehirler[:] #Slicing işlemi

#n[0] = 'İstanbul'
#print(sehirler)
#print(n)    

#def add(a,b,c=0): #ikiside 30 oalrak çıkar
#    return sum((a,b))

#print(add(10,20))
#print(add(10,20,30))

#def add(a,b,c=0,d=0,e=0): #bunu sadece 5 parametreye kadar götürebilirsin 6 olursa aşağısını yapmalısın
#    return sum((a,b,c,))

#print(add(10,20))
#print(add(10,20,30))    

#def add(*params):
#    print(params) #öncesine yazasan gönderdiğimiz tüm argümanlar bir liste şeklinde gösterilir
#    return sum((params))

#print(add(10,20))
#print(add(10,20,30))
#print(add(40,67,83,45,89,0,98,76,31))

#def displayUser(**args):#bu tuple değil dictionary olucağı için 2 yıldız ekledik
#    print(type(args))
#    for key, value in args.items():
#        print(('{} is {}'.format(key,value)))

#displayUser(name = 'Çınar', age = 2,city = 'İstanbul')
#displayUser(name ='Ada', age = 12, city = 'Kocaeli', phone = 123132)
#displayUser(name ='Yiğit', age = 14, city = 'Ankara', phone = 123134, email = 'yigit@gmail.com')

#hepsini özetleyen güzel bir örnek
def myfunc(a , b ,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
print(myfunc(10,20,30,40,50,key1 = 'value1',key2 = 'value2'))