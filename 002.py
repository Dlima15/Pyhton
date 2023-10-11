a = ['Número','Nome','Endereço','Tel',
     '1000','Paulo','Rua Hum 12','9800',
     '1500','Ana','Rua dois 33', '7900',
     '2000','Fabio','Rua Três 55','8800',
     '2500','Ana','Rua Quatro 67','7800'  
    ]

t=0

for x in range(4,len(a),4):
    
    t = t + int(a[x])

    print("O total da coluna 1 é: ",t)


