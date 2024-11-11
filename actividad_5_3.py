#ejercicio 1
def devolver_distintos(a, b, c):
    suma = a + b + c
    if suma > 15:
        return max(a, b, c)
    elif suma < 10:
        return min(a, b, c)
    else:
        return sorted([a, b, c])[1]
#ejercicio 2
def letras_unicas_alfabeticas(palabra):
    letras_unicas = set(palabra)
    letras_ordenadas = sorted(letras_unicas)
    return letras_ordenadas
print(letras_unicas_alfabeticas("boca juniors"))
#ejercicio 3
def verificar_cero_consecutivo(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i-1] == 0:
            return True
    return False
print(verificar_cero_consecutivo(1, 2, 3, 0, 0, 4))
#ejercicio 4
import math

def contar_primos(n):
    
    def es_primo(num):
        if num < 2:  
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:  
                return False
        return True

   
    cantidad_primos = 0

    
    for i in range(n + 1):
        if es_primo(i):
            print(i, end=" ")  
            cantidad_primos += 1  

   
    return cantidad_primos


resultado = contar_primos(20)
print(f"\nCantidad de números primos encontrados: {resultado}")
