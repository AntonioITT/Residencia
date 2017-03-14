class Circulo:
    def __init__(self,radio):
        self.r=radio
    def get_area(self):
        return self.r*self.r*3.1415

u=1
while u>=1:
    a = input('Radio del circulo= ')
    circle=Circulo(a)
    n=1
    while n>=1:
        print 'Que desea realizar'
        print '1. Ver radio'
        print '2. Calular area del circulo'
        print 'Otro: Ninguna de las anteriores'
        x=input()
        if x==1:
            print circle.r
        elif x==2:
            print circle.get_area()
        n = input('Desea realizar otra opcion= (1=Si , 0=No)')
    u=input('Desea crear otro circulo= (1=Si , 0=No)')

