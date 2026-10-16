from statistics import median


def devolver_distintos (*args):
    suma = sum(args)
    if suma > 15:
        numero= max(args)
    elif suma < 10:
        numero= min(args)
    else:
        numero=median(args)
    return numero

print (devolver_distintos(3,2,11))