#Pide a la usuaria un número entre 1 y 10
pregunta = "Elije un numero del 1 al 10"

print (pregunta)
respuesta = int(input())
print ()

#Crea una función que reciba un número y devuelva un mensaje de victoria si acierta y un mensaje de derrota si falla (el número ganador es el 4)
mensaje_victoria = "¡Has acertado!"
mensaje_derrota = "No has acertado :(. Vuelve a inetantarlo"

def numero (respuesta_numero):
    if respuesta_numero >=1 and respuesta_numero <=10:
        if respuesta_numero == 4:
            return mensaje_victoria
        elif respuesta_numero != 4:
            return mensaje_derrota

mensaje = numero (respuesta)

#Imprime el número elegido y el mensaje de resultado por pantalla
print ("El número elejido fue:", respuesta)
print ("El mensaje del resultado es:", mensaje)