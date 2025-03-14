#global scope
#x = 'global x'

#def function():
    #local scope
#    x = 'local x' #bunu da kaparsan 2krana 2 kez global scope gelir
#    print(x)
    
#function()
#print(x)
######
#name = 'Çınar'

#def changeName(new_name):
#    name =new_name
#    print(name)

#changeName('Ada')
#print(name)    
#######

name = 'global string'

def greeting():
    #name = 'Çınar'
    
    def hello():
        # name = 'Ada'
        print('hello '+ name)
    
    hello()
    
greeting()        

########

#x = 50
#def test(x):
#    print(f'x: {x} ')
    
#    x = 100
#    print(f'changed x to {x} ')

#test(x)
#print(x)    

x = 50
def test():
    global x #dışarda tanımlı olan x burdaki fonksiyonda da kullanmak i.in global değişkeni kullanılır
    print(f'x: {x} ')
    
    x = 100
    print(f'changed x to {x} ')

test()
print(x)