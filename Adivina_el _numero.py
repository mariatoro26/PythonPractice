nombre= (input("Introduce tu nombre: "))
intentos = 8
from random import randint
numero_secreto = randint(1,100)

print(f"Hola {nombre}, he pensado un número del 1 al 100. Tienes 8 intentos para adivinar")

while intentos > 0:
    numero_usuario = int(input("Introduce tu respuesta:"))
    if numero_usuario == numero_secreto:
        print("¡Felicidades, haz ganado!")
        intentos = -1
    elif numero_usuario > numero_secreto:
        intentos = intentos - 1
        print (f"El número elegido es mayor al número secreto. Te quedan {intentos} intentos ")
    elif numero_usuario < numero_secreto:
        intentos = intentos - 1
        print (f"El número elegido es menor al número secreto. Te quedan {intentos} intentos ")
    elif numero_usuario < 1 or numero_usuario > 100:
        print("Debes elegir un número entre 1 y 100 para poder jugar.")

if intentos == 0:
    print("Lo siento, no has logrado adivinar. ¡Intentalo de nuevo!")

