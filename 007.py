#Para Recuperar 

g = open("dados.txt", "r")
db= (g.read())

b = []
b = db.split(',')

for x in range(0,len(b)):
    if b[x] == "Ana":
        print(b[x])
    