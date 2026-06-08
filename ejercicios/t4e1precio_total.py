#Solicita a la usuaria:
nombre = "Gusy Luz"
precio = 20
cantidad = 2
dto = 0.25
pregunta1 = "¿Cuál es el nombre del producto que vas a comprar?"
pregunta2 = "¿Cuál es el precio por unidad?"
pregunta3 = "¿Cuántos vas a comprar?"
pregunta4 = "¿Qué descuento te aplican?"

    #Nombre del producto
print (pregunta1)
print (nombre)
print ()

    #Precio por unidad
print (pregunta2)
print (precio, "€")
print ()

    #Cantidad a comprar
print (pregunta3)
print (cantidad, "uds")
print ()

    #Descuento en porcentaje
print (pregunta4)
print (float(dto), "(25%)")
print ()

#Crea una función que reciba el precio, la cantidad y el descuento y devuelva el precio con descuento aplicado
def precio_final (_precio, _cantidad, _dto):
    resultado = _precio * _cantidad
    pfinal = resultado * _dto
    ptotal = resultado - pfinal
    return ptotal

ptotal = precio_final (20,2,0.25)

print ("Precio con descuento aplicado:", ptotal, "€")
print ()

#Muestra la cantidad, el nombre del producto, el descuento y el precio total con descuento
print ("Cantidad:", cantidad)
print ("Nombre:", nombre)
print ("Descuento", float(dto), "(25%)")
print ("Precio total con descuento",int(ptotal), "€")
print ()

#Crea una función que reciba una cantidad y le agrege un 21% de IVA
def total_mas_iva (_precio, _cantidad, _dto, _iva):
    resultado = _precio * _cantidad
    iva = resultado * _iva
    ivafinal = resultado + iva
    pfinal = ivafinal * _dto
    piva = ivafinal - pfinal
    return piva

piva = total_mas_iva (20,2,0.25, 0.21)

print ("El total + un 21% de IVA es:", float(piva), "€")
print ()

#Muestra el total con IVA aplicado
print ("Cantidad:", cantidad)
print ("Nombre:", nombre)
print ("Descuento", float(dto), "(25%)")
print ("Precio total con descuento",int(ptotal), "€")
print ("Precio total con el IVA aplicado:", float(piva), "€")