# Cuento
energia = int(input("Ingrese su energia actual: "))

if energia >= 50:
    print("¡Felicidades! Puedes cruzar el puente de inmediato sin pagar nada.")
else:
    monedas = int(input("No tienes suficiente energía. Ingrese la cantidad de monedas que tiene: "))

    if monedas >= 5:
        print("Puedes pagar el peaje en la barca mágica para navegar hasta la orilla.")
    else:
        print("No cumples con los requisitos. Debes quedarte a descansar en la posada del bosque hasta recuperar tus fuerzas.")