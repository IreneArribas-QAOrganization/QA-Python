#Pide a la usuaria una cantidad en euros
pregunta = "Dime un cantidad X en €"

print (pregunta)
cantidad = int(input())
print ()

#Crea una función reciba la cantidad en euros y devuelva el total en Dólares (1 euro = 1.1 dólares)
def money_dolar (euro, valor):
    dolar = euro * valor
    return dolar

dolar = money_dolar (cantidad, 1.1)

#Crea una función que reciba la cantidad en euros y devuelva el total en Libras (1 euro = 0.87 libras)
def money_libra (euro, valor):
    libra = euro * valor
    return libra

libra = money_libra (cantidad, 0.87)

#Muestra la cantidad en Euros, en Dólares y en Libras
print ("Cantidad en euros:", cantidad, "€")
print ("Conversión a dólares:", float(dolar), "$")
print ("Conversión a libras:", float(libra), "£")