nombre = (input("Ingrese su nombre: "))
ventas = float(input("Ingrese el valor de sus ventas: "))
Comision = round(ventas *0.13,2)

print(f"Hola {nombre}. Este mes ganaste ${Comision} por ventas.")