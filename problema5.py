#Escribir un progrma que dad una lista de numeros filtre aquellos que son
#impares. Se debera hacer uso de la funcion lambda.

def funcion1(p):
    return lambda p:p*p #elevacion al cuadrado

a=[1,2,3,4,5,6,7,8,9,10] #lista de numeros original
print a
print map(funcion1(a),a) #lista cuadratica