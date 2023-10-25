def menu(E):
    if(E == "q"): AreaQuadrado()
    if(E == "r"): AreaRetangulo()

def AreaRetangulo():
    b = int(input("Qual a base do retângulo?: "))
    h = int(input("Qual a altura do retângulo?: "))
    print('Area retangulo', (b*h), "cm2")

def AreaQuadrado():
    L = int(input("Qual o lado do quadrado?: "))
    print('Area retangulo', L**2, "cm2")


Escolha = input('Escolha a area do quadrado "q" e a area do retângulo "r": ')
menu(Escolha)


