nombre = input("¿Cuál es tu nombre? ")
numero_secreto = 42  
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")
intentos = 0
max_intentos = 8
while intentos < max_intentos:
    
    eleccion = int(input(f"Intento {intentos + 1}/{max_intentos}: Ingresa tu número: "))

    
    if eleccion < 1 or eleccion > 100:
        print("El número que elegiste no está permitido. Debe estar entre 1 y 100.")
    elif eleccion < numero_secreto:
        print("Tu respuesta es incorrecta. Has elegido un número menor al número secreto.")
    elif eleccion > numero_secreto:
        print("Tu respuesta es incorrecta. Has elegido un número mayor al número secreto.")
    else:
        
        print(f"¡Felicidades, {nombre}! Has acertado el número secreto {numero_secreto} en {intentos + 1} intentos.")
        break  
    intentos += 1
if intentos == max_intentos and eleccion != numero_secreto:
    print(f"Lo siento, {nombre}, se agotaron tus intentos. El número secreto era {numero_secreto}.")