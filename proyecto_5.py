import random


palabras_secretas = ["casa", "perro", "gato", "coche", "avion"]

def ahorcado():
    
    palabra_secreta = random.choice(palabras_secretas)
    
     
    guiones = ["_"] * len(palabra_secreta)
    
    
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


