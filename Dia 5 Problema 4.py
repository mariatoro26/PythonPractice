def numeros_primos (num):
    mi_lista = range(2,num+1)
    primos = 0
    for numero in mi_lista:
        if num % numero == 0:
            primos += 1
    return primos

print(numeros_primos(215))

