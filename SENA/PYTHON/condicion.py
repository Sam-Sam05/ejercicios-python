edad = int(input("Ingresa la edad del asistente: "))
tiene_identificacion = True

# Nivel 1: if/else básico
if edad >= 18:
    print("Acceso permitido al área general.")
else:
    print("Acceso denegado. Es menor de edad.")

# Nivel 2: Agregando elif y operadores lógicos (and)
if edad >= 18 and tiene_identificacion:
    print("Acceso completo autorizado.")
elif edad >= 18 and not tiene_identificacion:
    print("Ve a la taquilla para verificar tu identidad.")
elif edad >= 13:
    print("Acceso permitido solo a la zona familiar.")
else:
    print("Acceso denegado.")