from random import choice

# Definir Variables
palabras = ["panadero", "dinosaurio", "helipuerto", "tiburon"]
abecedario = "abcdefghijklmnñopqrstuvwxyz"

# Función para elegir la palabra oculta
def elegir_palabra(lista_palabras):
    return choice(lista_palabras)


# Función para mostrar tablero
def mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas):
    tablero = []
    for letra in palabra:
        if letra in letras_correctas:
            tablero.append(letra)
        else:
            tablero.append("_")
    print("\n" + "*" * 20)
    print(" ".join(tablero))
    print("Letras incorrectas:" + " ".join(letras_incorrectas))
    print("Vidas:", vidas)
    print("*" * 20 + "\n")

# Función para pedir letra al usuario
def pedir_letra(letras_utilizadas):
    es_valida = False
    while not es_valida:
        letra = input("Elige una letra: ").lower()
        if letra in abecedario and len(letra) == 1:
            if letra in letras_utilizadas:
                print("Ya has elegido esa letra. Elige otra.")
            else:
                es_valida = True
        else:
            print("Letra inválida. Elige otra.")
    return letra


# Función para verificar si la letra es correcta
def chequear_letra(letra, palabra, letras_correctas, letras_incorrectas, vidas):
    if letra in palabra:
        letras_correctas.append(letra)
    else:
        letras_incorrectas.append(letra)
        vidas -= 1
    return vidas


# Función para verificar si ha ganado
def verificar_victoria(palabra, letras_correctas):
    for letra in palabra:
        if letra not in letras_correctas:
            return False
    return True


# Función para iniciar Juego
def jugar():
    palabra = elegir_palabra(palabras)
    letras_correctas = []
    letras_incorrectas = []
    vidas = 6
    juego_terminado = False

    while not juego_terminado:
        mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
        letras_usadas = letras_correctas + letras_incorrectas
        letra = pedir_letra(letras_usadas)
        vidas = chequear_letra(letra, palabra, letras_correctas, letras_incorrectas, vidas)

        if vidas == 0:
            mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
            print("Has perdido. La palabra era:", palabra)
            juego_terminado = True
        elif verificar_victoria(palabra, letras_correctas):
            mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
            juego_terminado = True
            print("¡Ganaste! La palabra era:", palabra)


jugar()


