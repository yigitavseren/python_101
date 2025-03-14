#def square(num): return num ** 2
square = lambda num: num ** 2
numbers = [1,3,5,9,10,4]

#result = list(map(lambda num: num ** 2, numbers)) #bunda da lambdaya bir şey tanımlayarak kısaltabiliriz
#result = list(map(square, numbers)) #hatta bunu da akaptıp en alttaki gibi  de yapabilzir
#for item in map(square, numbers): #şu fonksiyona gerek kalmıyor lambda kullanınca
#    print(item)

#result = square(3) #direkt böyle de kullanabiliriz

#filter
def check_even(num): return num%2==0

#result =  list(filter(check_even, numbers))
result =  list(filter(lambda num: num%2==0, numbers))

print(result)