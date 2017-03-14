#Escribir un progrma que dad una lista de numeros filtre aquellos que son
#impares. Se debera hacer uso de la funcion lambda.

def funcion1(x):
    return (lambda p:p%2)(x) #calculo del residuo de la division entre 2

a=[1,2,5,4,6,8,2,11,23,52,18,13,97,16,17,15,8,9,6] #lista de numeros
for v in a:
    if funcion1(v)!=0: #filtro para eliminar numeros pares
        print v     #impresion de numeros impares

