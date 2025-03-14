import random 

#result = dir(random)
#result = help(random)

#result = random.random() #0.0 -1.0
#result = random.random() * 100 #0.0 - 1.0
#result = int(random.uniform(10,100))
#result = random.randint(1,100) #direkt tam sayı

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
#result = names[random.randint(0,len(names))] #3 demememizin sebebi sonucunun dinamik olması
result = random.choice(names) #direkt bunu yazabilirsin
result = random.choice(greeting)

liste = list(range(10))

result = liste
random.shuffle(liste) #listeyi karıştırır

liste = range(100)
result = random.sample(liste, 3) #listenin içerisinden 3 tane farklısayı seç
result = random.sample(names,2)


print(result)