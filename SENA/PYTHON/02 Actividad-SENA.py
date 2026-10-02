cantidad = int(input("Ingrese la cantidad de televisores vendidos: "))
print("----------------------------------------------------------------------")
valor_tv = int(input("Ingrese el valor de cada televisor: "))
print("----------------------------------------------------------------------")

monto_total = cantidad * valor_tv
IVA = monto_total * 0.18

if monto_total > 5000000:
    descuento = monto_total * 0.03
    monto_con_descuento = monto_total - descuento
else:
    descuento = 0
    monto_con_descuento = monto_total 

monto_final_bruto = monto_total + IVA

if descuento > 0:
    print(f"El monto con descuento (antes de IVA) es: ${monto_con_descuento:,.0f}")
else:
    print("No aplica descuento para esta venta.")

print(f"El valor del IVA (18%) es: ${IVA:,.0f}")
print(f"El monto final bruto es: ${monto_final_bruto:,.0f}")
print("--------------------------------------------------------")
