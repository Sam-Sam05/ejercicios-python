cantidad = int (input("Ingrese la cantidad de televisores vendidos: "))

print ("----------------------------------------------------------------------")

valor_tv = int (input("Ingrese el valor de cada televisor: "))

print ("----------------------------------------------------------------------")

monto_total = cantidad * valor_tv
IVA = monto_total * 0.18

if monto_total > 5000000:
    descuento = monto_total * 0.03
    print (f"El descuento aplicado es: {descuento}")
    print (f"El monto total a pagar con descuento es: {monto_total - descuento}")
    print (f"El valor del IVA es: {IVA}")
    print (f"El monto final bruto a pagar es: {monto_total + IVA}")
    print ("--------------------------------------------------------")
else:
    print (f"El valor del IVA es: {IVA}")
    print (f"El monto final bruto a pagar es: {monto_total + IVA}")
    print ("--------------------------------------------------------")