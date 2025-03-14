#Inheritance (Kalıtım): Miras alma

#Person => name,lastname,age,eat(),run(),drink()
#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastName = lname
        print('Person created')
        
    def who_am_i(self):
        print('I am a person')
    
    def eat(self):
        print('I am eating')    
        
class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student created')
    #override
    def who_am_i(self):
        print('I am a student')
    
    def sayHello(self):
        print('Hello ı am a student')
        
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
        
        
    

p1 = Person('Ali','Yılmaz')
s1 = Student('Çınar','Turan', 1256)
t1 = Teacher('Serkan', 'Yılmaz', 'Math')
print(p1.firstname + ' ' + p1.lastName)
print(s1.firstname + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()

