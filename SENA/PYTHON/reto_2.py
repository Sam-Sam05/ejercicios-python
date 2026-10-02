peso = 70.5
altura = 1.75

# 1. Completa la fórmula matemática del IMC (peso dividido por la altura al cuadrado)
imc = peso / (altura * altura)
imc = round(imc, 1)
print(f"Tu IMC es: {imc}")

# Encuentra los 3 errores en esta estructura:
if imc < 18.5: # 1° error: faltaba poner los : al final.
    print("Diagnóstico: Bajo peso") #2° error: la sangría estaba por fuera de la condicion.
elif imc == 24.9: #3° error: Habia solo un signo de igual, asi que hace entender que esta asignando, en vez de comparar.
    print("Diagnóstico: Peso normal")
elif imc < 29.9:
    print("Diagnóstico: Sobrepeso")
else:
    print("Diagnóstico: Obesidad")