import random 

class nodoCola(object):
    """crea una variable nodo cola"""
    def __init__(self):
        self.info, self.sig = None, None

class Cola(object):
    """TDA cola """

    def __init__(self):
        self.frente, self.final, self.tamanio = None, None, 0

def barrido_cola(cola):
    if tamanio(cola) > 0:
        nodo = cola.frente
        while nodo:
            print(nodo.info)
            nodo = nodo.sig

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if(cola.final is None):
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    aux = cola.frente.info
    cola.frente = cola.frente.sig
    if(cola.frente is None):
        cola.final = None
    cola.tamanio -= 1
    return aux


def cola_vacia(cola):
    return cola.tamanio == 0


def tamanio(cola):
    return cola.tamanio

def en_frente(cola):
    return cola.frente.info

def mover_final(cola):
    x = atencion(cola)
    arribo(cola, x)
    return x

def cola_numerica(cola):
    while tamanio(cola) < 10:
        x = int(random.randint(0,50))
        arribo(cola,x)
    print('cola')
    for i in range (tamanio(cola)):
        print(en_frente(cola))
        mover_final(cola)


