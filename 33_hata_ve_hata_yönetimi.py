# error => hata

#Error
#print(a) => NameError
#int('1a2') => ValueError
#print(10/0) => ZeroDivisionError
#print('denem'e) => SyntaxError

# error handling => hata yönetimi
#try:
#    x = int(input('x: '))
#    y = int(input('y: '))
#    print(x/y)
#except ZeroDivisionError:
#    print('y için  sıfır girilemez')
#except ValueError:
#    print('x ve y için sayısal değer girmelisiniz.')
#böyle uzun uzun yazmak yerine aşağıdakini yapmak daha mantıklı
#try:
#    x = int(input('x: '))
#    y = int(input('y: '))
#    print(x/y)
#except (ZeroDivisionError,ValueError) as e:
#    print('Yanlış bilgi girdiniz')
#    print(e)
#try:
#    x = int(input('x: '))
#    y = int(input('y: '))
#    print(x/y)
#except : #burda hata tipini göremiyoz
#    print('Yanlış bilgi girdiniz')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as Ex: #burda ise hatanın adını gösteririz
        print('Yanlış bilgi girdiniz', Ex)
    else:
        break #burda ise bilgiyi alana kadar devam eder
    finally:
        print('try except sonlandı.') #bu her zaman çalışır maksat tanımlanana içeriklerin sonlanması dosya okunamsı