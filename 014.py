def Second(segundos):
    return (segundos//3600),'h',(segundos%3600)//60,'s',(segundos%3600)%60,'s'

time = int(input("Quantos segundos?"))

print(Second(time))

