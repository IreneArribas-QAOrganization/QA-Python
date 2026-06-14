#Crea una función que pida a la usuaria cuántas notas desea introducir
def _pregunta ():
    pregunta = "¿Cuántas notas deseas introducir?"
    print (pregunta)
    respuesta = int(input())
    return respuesta

respuesta = _pregunta()
print ()

#Crea una función que solicite cada nota
def _notas (n_notas):
    for i in range (n_notas):
        notas = float(input())
        return notas

notas = _notas (respuesta)
print (notas)


#Crea una función que sume todas las notas


#Crea una función que devuelva la nota media


#Crea una función que imprima la nota por pantalla