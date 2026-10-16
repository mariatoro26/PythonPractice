def caracteres_unicos (palabra):
    caracteres = set()
    for letra in palabra:
        caracteres.add(letra)
    mi_lista = list(caracteres)
    mi_lista.sort()
    return mi_lista

print(caracteres_unicos("Maria"))




