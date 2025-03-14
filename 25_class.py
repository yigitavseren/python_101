#class

class Person:
    
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
    # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı')
        #methods


#object(instant)
p1 = Person(name = 'Yiğit',year = 2004)
p2 = Person(name = 'Mahmut',year = 2016)

#updating
p1.name = 'Ahmet'
p1.address = 'Kocaeli'

#accesing object attributes
print(f'p1: name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2: name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)