#Pide a la usuaria que elija un color:
pregunta = "Elije un color (rojo, verde, azul, amarrillo o morado)"

print (pregunta) 
respuesta = input()
respuesta = respuesta.lower()
print (respuesta)
print ()

#Crea una función que reciba un color y devuelva un mensaje según el color elegido:
mensaje_rojo = "mensaje de pasión y energía"
mensaje_verde = "mensaje de esperanza y crecimiento"
mensaje_azul = "mensaje de calma y serenidad"
mensaje_amarillo = "mensaje de felicidad y optimismo"
mensaje_morado = "mensaje de sabiduría y creatividad"

def r_color (_respuesta):
    if _respuesta == "rojo":
        return mensaje_rojo
    elif _respuesta == "verde":
        return mensaje_verde
    elif _respuesta == "azul":
        return mensaje_azul
    elif _respuesta == "amarillo":
        return mensaje_amarillo
    elif _respuesta == "morado":
        return mensaje_morado
    else:
        return "none"
    
mensaje = r_color (respuesta)

#Muestra por pantalla el color elegido y el mensaje
print ("Color elegido:", respuesta)
print ("Mensaje de respuesta:", mensaje)