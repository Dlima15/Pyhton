a = ['Número','Nome','Endereço','Tel',
     '1000','Paulo','Rua Hum 12','9800',
     '1500','Ana','Rua dois 33', '7900',
     '2000','Fabio','Rua Três 55','8800',
     '2500','Ana','Rua Quatro 67','7800'  
    ]

soma=0

for x in range(4,len(a),4):

    if a[x+1]=='Ana':
        soma = soma + int (a[x])

print("O total de Ana é: ",soma)


