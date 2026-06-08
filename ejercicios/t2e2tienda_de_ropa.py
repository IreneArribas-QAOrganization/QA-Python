#Define los siguientes precios:
camiseta = 10
sudadera = 20.5
gorra = 5.5

#Pide a la usuaria la cantidad de cada artículo
pregunta1 = "Cuánto vale la camiseta?"
pregunta2 = "Cuánto vale la sudadera?"
pregunta3 = "Cuánto vale la gorra?"

print (pregunta1)
print (camiseta, "€")
print ()
print (pregunta2)
print (sudadera, "€")
print ()
print (pregunta3)
print (gorra, "€")
print ()

#Calcula el total de la compra
total = int(camiseta + sudadera + gorra)

print ("Total:"), print (total, "€")
print ()

#Añade el 21% de IVA al total
iva = float(total * 0.21)
print ("IVA:", iva, "€")
print ()

#Muestra el precio final
print ("Total + IVA:")
print (total + iva, "€")