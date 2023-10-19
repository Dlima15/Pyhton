a = ['Número','Nome','Endereço','Tel',
     '1000','Paulo','Rua Hum 12','9800',
     '1500','Ana','Rua dois 33', '7900',
     '2000','Fabio','Rua Três 55','8800',
     '2500','Ana','Rua Quatro 67','7800'  
    ]

D = open("dados.txt","a", encoding = "utf-8")

for x in a:
    D.write(x+",")

D.close()



