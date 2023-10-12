a = ['Número','Nome','Endereço','Tel',
     '1000','Paulo','Rua Hum 12','9800',
     '1500','Ana','Rua dois 33', '7900',
     '2000','Fabio','Rua Três 55','8800',
     '2500','Ana','Rua Quatro 67','7800'  
    ]

soma=0

n = input('De quem você quer os dados? ')

for x in range(4,len(a),4):

    if a[x+1]==n:
        soma = soma + int (a[x])

print("O total de",n,"é",soma)

import os

os.remove("Arquivo.txt")

f = open('Arquivo.txt', "a")

for x in a:
    f.write(x+',')

f. close()

#Para Recuperar 


g = open("Arquivo.txt", "r")
db= (g.read())

for x in range(0,len(a),4):
    print(x,"\t", a [x], "\t", a [x+1], "\t",a [x+2], "\t",a [x+3], "\t")

b = []
b = db.split(',')
#print(b)





