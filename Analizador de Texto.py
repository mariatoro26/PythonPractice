Fuente = input("Ingrese su texto: ")
fuente_real = Fuente.lower()

Letra1 = input("Ingrese su primera letra: ")
Letra2 = input("Ingrese su segunda letra: ")
Letra3 = input("Ingrese su tercera letra: ")

Letra1=Letra1.lower()
Letra2=Letra2.lower()
Letra3=Letra3.lower()

Letras1 = Fuente.count(Letra1)
Letras2 = Fuente.count(Letra2)
Letras3 = Fuente.count(Letra3)

print("\n")
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado {Letras1} veces la letra {Letra1} en el texto")
print(f"Hemos encontrado {Letras2} veces la letra {Letra2} en el texto")
print(f"Hemos encontrado {Letras3} veces la letra {Letra3} en el texto")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = Fuente.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

print("\n")
print("LETRA INICIAL Y LETRA FINAL")

letra_inicio = Fuente[0]
letra_final = Fuente[-1]

print(f"La letra inicial del texto es '{letra_inicio}'")
print(f"La letra final del texto es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
texto_invertido = " ".join(palabras)

print(f"El texto invertido es: {texto_invertido}")

print("\n")
print("BUSCAR LA PALABRA PYTHON")
buscar_python = "python" in Fuente
dic = {True: "sí", False: "no"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")










