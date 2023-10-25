def AreaSupesfera(raio):
    return 4*3.14*raio**2 

print("Area do quadrado da esfera")
raio = int(input("Qual o Raio?"))
ar = AreaSupesfera(raio)
print("Area superficie esfera",ar,"cm2")