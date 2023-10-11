a = ['Número','Nome','Endereço','Tel',
     '1000','Paulo','Rua Hum 12','9800',
     '1500','Ana','Rua dois 33', '7900',
     '2000','Fabio','Rua Três 55','8800',
     '2500','Ana','Rua Quatro 67','7800'  
    ]

for x in range(0,len(a),4):
    print(x,"\t", a [x], "\t", a [x+1], "\t",a [x+2], "\t",a [x+3], "\t")