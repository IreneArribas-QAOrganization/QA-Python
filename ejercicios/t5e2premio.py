#Pide a la usuaria 5 veces que introduzca un color
mensaje_feliz = "¡Premio! Has acertado"
mensaje_triste = "Prueba otro color"

for i in range (5):
    print ("Introduce un color: ")
    valor = (input ().lower())
    if valor == "azul":
        print (mensaje_feliz)
    elif valor != "azul":
        print (mensaje_triste)
        
#Si la usuaria introduce el color azul, muestra que el premio ha sido conseguido. Si no, dile que pruebe otro color


