from operator import truediv
from ssl import cert_time_to_seconds


def cero_consecutico (*args):
    mi_lista = list(args)
    contador = 0
    for elemento in mi_lista:
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False

print(cero_consecutico(0,2,8,5,6,7,0,5,4))


