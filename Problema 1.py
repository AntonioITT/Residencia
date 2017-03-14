# Numero factorial usando recursividad

u=1

while u>=1:
    a = input('Numero= ')
    def factorial(x):
        if x < 0:
            return 0
        elif x > 1:
            return x * factorial(x - 1)
        return 1
    print factorial(a)
    u=input('Desea ingresar otro numero= (1=Si , 0=No)')
