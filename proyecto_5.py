import random

# Lista de palabras secretas
palabras_secretas = ["casa", "perro", "gato", "coche", "avion"]

def ahorcado():
    # Elegir palabra secreta aleatoria
    palabra_secreta = random.choice(palabras_secretas)
    
    # Inicializar guiones para la palabra secreta
    guiones = ["_"] * len(palabra_secreta)
    
    # Inicializar vidas
    vidas = 6
    
    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes", vidas, "vidas.")
    
    while "_" in guiones and vidas > 0:
        print(" ".join(guiones))
        letra = input("Ingrese una letra: ").lower()
        
        if len(letra) != 1:
            print("Ingrese una letra sola.")
        elif letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    guiones[i] = letra
        else:
            vidas -= 1
            print(f"Letra incorrecta. Te quedan {vidas} vidas.")
    
    if "_" not in guiones:
        print(" ".join(guiones))
        print("¡Felicidades! Ganaste.")
    else:
        print(f"La palabra secreta era {palabra_secreta}.")
        print("¡Lo siento! Perdiste.")

ahorcado()


# *Funcionamiento:*

# 1. Se elige una palabra secreta aleatoria de la lista.
# 2. Se inicializan guiones para representar la palabra secreta.
# 3. Se establecen 6 vidas.
# 4. En cada turno, el jugador ingresa una letra.
# 5. Si la letra está en la palabra secreta, se reemplaza el guión correspondiente.
# 6. Si la letra es incorrecta, se resta una vida.
# 7. El juego continúa hasta que se adivine la palabra o se agoten las vidas.

# *Notas:*

# - El programa utiliza una lista de palabras secretas predefinidas.
# - La palabra secreta se elige aleatoriamente en cada partida.
# - El juego no tiene elementos gráficos, pero muestra el estado actual de la palabra y las vidas restantes.