#x = 10

#if x > 5:
#    raise Exception("x 5 den büyük değer alamaz.")

#def check_password(psw):
#    import re
#    if len(psw) < 8:
#        raise Exception("parola en az 7 karakter olmalıdır.")
#    elif not re.search("[a-z]",psw):
#        raise Exception("parola küçük harf içermelidir.")
#    elif not re.search("[A-Z]",psw):
#        raise Exception("parola büyük  harf içermelidir.")
#    elif not re.search("[0-9]",psw):
#        raise Exception("parola rakam içermelidir.")
#    elif not re.search("[_@ß]",psw):
#        raise Exception("parola alpha numeric karakter içermelidir.")
#    elif re.search("\s",psw):
#        raise Exception("parola boşluk içermemelidir.")
#    else:
#        print("geçerli parola")

#password = "aB@12345678"

#try:
#   check_password(password)
#except Exception as ex:
#    print(ex)
#else:
#        print("geçerli parola")
#finally:
#    print("Validation tamamlandı")

class Person:
    def __init__(self, name, year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name

p = Person("Aliiiiiii",1999)