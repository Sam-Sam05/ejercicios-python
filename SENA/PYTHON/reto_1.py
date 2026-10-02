print ("=" * 50)
print("Tienda".upper())
print("=" * 50)
print()

print("Bienvenido a nuestra tienda".upper())
print()

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que comprará del producto: "))

# Calculo
total = precio * cantidad

# Condicion
if total > 200000:
    print("Usted tiene un 20% de descuento")
    print()
    descuento_20 = total * 0.2
    descuento_20 = total - int(descuento_20)
    print(f"Total a pagar: ${descuento_20:,.0f}".replace(",", "."))
elif total > 100000:
    print("Usted tiene un 10% de descuento")
    print()
    descuento_10 = total * 0.1
    descuento_10 = total - int(descuento_10)
    print(f"Total a pagar: ${descuento_10:,.0f}".replace(",", "."))
else:
    print("Usted no tiene descuento")
    print()
    print(f"Total a pagar: ${total:,.0f}".replace(",", "."))