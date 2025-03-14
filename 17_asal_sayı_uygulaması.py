number = int(input('Please press a number: '))
asalmi = True

if number == 1:
    asalmi = False

for i in  range(2 , number):
    if (number % i == 0):
        asalmi = False
        break

if asalmi:
    print('Sayı asaldır.')
else:
    print('Sayı asal değildir')        