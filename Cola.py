from tda_cola_din import Cola, cola_numerica, cola_vacia, arribo, atencion, barrido_cola,tamanio, mover_final, en_frente
from tda_pila import Pila, apilar, desapilar, pila_vacia, barrido_pila, ordenar
from math import asin, sqrt, sin, cos, radians
from time import sleep
from random import randint, choice

#Ej1

def  vocales ( cola ):
    cola_aux  =  Cola ()
    while  not  cola_vacia ( cola ):
        x  =  atencion ( cola )
        if  x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U': 
            arribo ( cola_aux , x )
    cola  =  cola_aux
    print ( 'La cola sin vocales es: ' )
    barrido_cola ( cola )

#2

def invertir_cola(cola):
    pila = Pila()
    while not cola_vacia(cola):
        apilar(pila, atencion(cola))
    while not pila_vacia(pila):
        arribo(cola, desapilar(pila))
    print('Cola invertida: ')
    barrido_cola(cola)

#3

def palindromo():
    pila = Pila()
    cola = Cola()
    palindromo = True
    palabra = 'anana'

    print(palabra)
    for letra in palabra:
        apilar(pila, letra)
        arribo(cola, letra)
    for i in range(0, tamanio(cola)):
        dato_cola = atencion(cola)
        dato_pila = desapilar(pila)
        if dato_cola != dato_pila:
            palindromo = False
    if palindromo:
        print(True)
    else:
        print(False)


# EJ 4
def eliminacion(cola):
    cola = Cola()
    while not cola_vacia(cola):
        m = atencion(cola)
    for i in range (tamanio(cola)):
        m = en_frente(cola)
    for i in range (0, m):
        i+=1
        if ( m % i == 0):
            c_div += 1
    if c_div >= 3:
        atencion(cola)
    else:
        print(m)
        mover_final(cola)


# EJ 5
def invertiir(pila):
    cola = Cola()
    while not pila_vacia(pila):
        arribo(cola, desapilar(pila))
    while not cola_vacia(cola):
        apilar(pila, atencion(cola))
    print('Pila invertida: ')
    barrido_pila(pila)

# EJ 6
def cont_ocurrencias(cola):
    cont = 0
    busc = 3
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato == busc:
            cont += 1
    print('El elemento', busc, 'se repite', cont)


# EJ 7
def eliminar(cola):
    cola_aux = Cola()
    pos = 5
    if tamanio(cola) > pos:
        i = 0
        while i < pos:
            x = atencion(cola)
            arribo(cola_aux, x)
            i += 1
        eliminado = atencion(cola)
        print('El elemento eliminado es:', eliminado)
        while not cola_vacia(cola):
            arribo(cola_aux, atencion(cola))
        print('Cola:')
        barrido_cola(cola_aux)

# EJ 8
def cola_ordenada():
    cola = Cola()
    cola_aux = Cola()
    for i in range(10):
        dato = randint(1, 50)
        print(str(dato) + ' agregado')  
        while not cola_vacia(cola) and en_frente(cola) <= dato:
            arribo(cola_aux, atencion(cola))
        arribo(cola_aux, dato)
        while not cola_vacia(cola):
            arribo(cola_aux, atencion(cola))
        while not cola_vacia(cola_aux):
            arribo(cola, atencion(cola_aux))
    print('La cola ordenada es:')
    barrido_cola(cola)

#ej9

def cola_con_negativos(cola):
    while tamanio(cola) < 20:
        datos = int(randint(-30,30))
        arribo(cola,datos)
    print('cola')
    for x in range (tamanio(cola)):
        print(en_frente(cola))
        mover_final(cola)

    print(cola_con_negativos(cola))
    max = None
    min = None
    c = 0
    for i in range (tamanio(cola)):
        if (max == None) and (min == None) :
            max = en_frente(cola)
            min = en_frente (cola)
        else: 
            if (max < en_frente(cola)):
                max = en_frente(cola)
            if min > en_frente(cola):
                min = en_frente(cola)
        if en_frente(cola) < 0:
            c += 1
        mover_final(cola)

    print("El rango es entre" + str(min) + " y " + str(max))
    print("La cantidad de negativos es: " + str(c))


# EJ 10
def psw():
    cola = Cola()
    cola_aux = Cola()
    cola1=  Cola()
    cola2 = Cola()
    personajes = ['Breha Organa', 'Bail Organa', 'Killik', 'Chirpa el Ewok', 'Asha Fahn el Ewok', 
    'Kneesaa el Ewok','Saqueador Tusken','Dathcha el Jawa', 'Jabba el Hutt','Luke Skywalker', 'Han Solo', 'Yoda',
    'Jar Jar Binks']
    
    origen = ['Alderaan', 'Alderaan', 'Alderaan', 'Endor', 'Endor', 'Endor','Tatooine', 
    'Tatooine', 'Tatooine', 'Polis Massa', 'Corellia','Desconocido', 'Naboo']

    for i in range(0, len(personajes)):
        arribo(cola, [personajes[i], origen[i]])
    print('Personaje  -   Planeta de origen')
    barrido_cola(cola)
    while not cola_vacia(cola):
        x = atencion(cola)
        if x[1] == 'Alderaan' or x[1] == 'Endor' or x[1] == 'Tatooine':
            print(str(x[0]) + '  del planeta ' + str(x[1]))
        if x[0] == 'Luke Skywalker' or x[0] == 'Han Solo':
            print(str(x[0]) + 'del planeta ' + str(x[1]))
        if x[0] != 'Yoda':
            arribo(cola1, x)
        else:
            arribo(cola1, ['Sheev Palpatine', 'Naboo'])
            arribo(cola1, x)
        arribo(cola_aux, x)
        while not cola_vacia(cola_aux):
            x = atencion(cola_aux)
            if x[0] == 'Jar Jar Binks' and not cola_vacia(cola_aux):
                atencion(cola_aux)
            arribo(cola2, x)
    print('Agregar personaje antes de Yoda')
    print('Eliminar personaje despues de Jar Jar Binks')
    barrido_cola(cola2)

# EJ 11
def colas_combinadas():
    cola1 = Cola()
    cola2 = Cola()
    datos = [0, 2, 4, 7, 8, 10]
    datos2 = [1, 3, 5, 6, 9, 11]
    for i in range(0, len(datos)):
        arribo(cola1, datos[i])
        arribo(cola2, datos2[i])
    print('Cola 1 es :')
    barrido_cola(cola1)
    print('Cola 2 es:')
    barrido_cola(cola2)
    for i in range(0, tamanio(cola1)):
        if en_frente(cola1) < en_frente(cola2):
            mover_final(cola1)
        else:
            while en_frente(cola1) > en_frente(cola2):
                arribo(cola1, atencion(cola2))
            mover_final(cola1)
    while not cola_vacia(cola2):
        arribo(cola1, atencion(cola2))
    print('Combinacion de ambas colas: ')
    barrido_cola(cola1)

# EJ 12
def caracteres(cola):
    cola_d = Cola()
    cola_c = Cola()
    cont = 0
    num = False
    i = False
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato.isdigit():
            arribo(cola_d, dato)
        else:
            arribo(cola_c, dato)
    print('El tamaño de la cola de numeros es: ' + str(tamanio(cola_d)))
    print('El tamaño de la cola de caracteres es: ' + str(tamanio(cola_c)))
    while not cola_vacia(cola_c):
        dato = atencion(cola_c)
        if dato.isalpha():
            cont += 1
        if dato == '?':
            i = True
        if dato == '#':
            num = True
    print('Cantidad de letras en la cola de caracteres es de : ' + str(cont))
    if i:
        print('Hay signos de interrogacion en la cola')
    if num:
        print('Existen # en la cola')

# EJ 14
def qe_onda_el_enunciado_wtf():
    cola = Cola()
    cola_aux = Cola()
    pila = Pila()
    base = ['Base Dantooine', 'Base Eco', 'Cuartel General de la Resistencia',
            'Gran Templo de Massassi', 'Puesto de avanzada Beta']
    latitud = [73, -23, -37, 45, 4]
    longitud = [-54, 166, -72, 4, 113]
    q1 = radians(randint(-90, 90)) 
    d1 = radians(randint(-180, 180)) 
    r = 6371 
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(base)):
        arribo(cola, [base[i], randint(10, 200), latitud[i], longitud[i]])
    print('Base - Tamaño de flota - Latitud - Longitud')
    barrido_cola(cola)
    print('La coordenada actual es :', round(q1, 6), ',', round(d1, 6))
    while not cola_vacia(cola):
        x = atencion(cola)
        q2 = radians(x[2])
        d2 = radians(x[3])
        formula = 2*r*asin(sqrt(sin((q1-q2)/2)**2+cos(q1)*cos(q2)*sin((d1-d2)/2)**2))
        dist = int(formula)
        print(x[0] + ' se encuentra a ' + str(dist) + 'km')
        apilar(pila, [dist, x[0], x[1]])
        arribo(cola_aux, [x[1], x[0], dist])
    print()
    pila = ordenar(pila)
    c1 = desapilar(pila)
    c2 = desapilar(pila)
    c3 = desapilar(pila)
    print('Las tres bases mas cercanas son:')
    print(c1[1] + ' se encuentra a ' + str(c1[0]) + 'km')
    print(c2[1] + ' se encuentra a ' + str(c2[0]) + 'km')
    print(c3[1] + ' se encuentra a ' + str(c3[0]) + 'km')
    if c1[2] > c2[2] and c1[2] > c3[2]:
        print(c1[1] + ' posee la mayor flota aerea')
    elif c2[2] > c1[2] and c2[2] > c3[2]:
        print(c2[1] + ' posee la mayor flota aerea')
    else:
        print(c3[1] + ' posee la mayor flota aerea')
    print()
    barrido_cola(cola_aux)
    cont = 0
    while not cola_vacia(cola_aux):
        dato = atencion(cola_aux)
        if dato[0] > cont:
            cont = dato[0]
            info = dato
    print()
    print(info[1], 'posee la mayor flota(' + str(info[0]) + ')')
    print('Se encuentra a:', info[2], 'km')

#ej16

cola = Cola()
id = 0
while tamanio(cola) < 7:
    id += 1
    dato =[0,0]
    dato[0] = id
    dato[1] = randint(1,8)
    arribo(cola, dato)
while not cola_vacia(cola):
    if (en_frente(cola)[1] > 4.5 ):
        sleep(4.5)
        en_frente(cola)[1] -= 4.5
        print('El proceso '+ str(en_frente(cola)[0]) +'se excedio de tiempo y fue aarribado')
        mover_final(cola)
    else:
        sleep(en_frente(cola)[1])
        x = atencion(cola)
        print(x)
    proc = input('¿Desea agregar un proceso a la cola?: ')
    if (proc.lower() == 'si'):
        id += 1
        dato[0] = id
        dato[1] = randint(1,8)

#17 

def consultorio():
    Corig = Cola()
    cola_aux = Cola()
    C1 = Cola()
    C2 = Cola()
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1000):
        arribo(Corig, [choice(letras), randint(000, 999)])
    barrido_cola(Corig)
    while not cola_vacia(Corig):
        dato = atencion(Corig)
        if dato[0] == 'A' or dato[0] == 'C' or dato[0] == 'F':
            arribo(C1, dato)
        if dato[0] == 'B' or dato[0] == 'D' or dato[0] == 'E':
            arribo(C2, dato)
        arribo(cola_aux, dato)
    print('Cantidad turnos A, C o F: ' + str(tamanio(C1)))
    print('Cantidad turnos B, D o E: ' + str(tamanio(C2)))
    if tamanio(C1) > tamanio(C2):
        print('La cola 1 tiene mayor cantidad de turnos')
    elif tamanio(C2) > tamanio(C1):
        print('La cola 2 tiene mayor cantidad de turnos')
    else:
        print('Son iguales')
    print('')
    A, C, F = 0, 0, 0
    B, D, E = 0, 0, 0
    while not cola_vacia(C1):
        dato1 = atencion(C1)
        if dato1[0] == 'A':
            A += 1
        if dato1[0] == 'C':
            C += 1
        if dato1[0] == 'F':
            F += 1
    while not cola_vacia(C2):
        dato2 = atencion(C2)
        if dato2[0] == 'B':
            B += 1
        if dato2[0] == 'D':
            D += 1
        if dato2[0] == 'E':
            E += 1
    print('La cola 1 contiene:')
    print('A: ' + str(A) + ', C: ' + str(C) + ', F: ' + str(F))
    print('La cola 2 contiene:')
    print('B: ' + str(B) + ', D: ' + str(D) + ', E: ' + str(E))
    print('')
    if A > C and A > F:
        print('En cola 1, mayoria de letras A')
    elif C > A and C > F:
        print('En cola 1, mayoria de letras C')
    else:
        print('En cola 1, mayoria de letras F')
    if B > D and B > E:
        print('En cola 2, mayoria de letras B')
    elif D > B and D > E:
        print('En cola 2, mayoria de letras D')
    else:
        print('En cola 2, mayoria de letras E')
    c = 0
    while not cola_vacia(cola_aux):
        dato = atencion(cola_aux)
        if dato[1] <= 506:
            c += 1
    print('Cantidad de turnos con numero menor a 506: ' + str(c))

# EJ 19
def peaje():
    C1, C2, C3 = Cola(), Cola(), Cola()
    vehiculos = ['Automovil', 'Camioneta', 'Camion', 'Colectivo']
    cab1, cab2, cab3 = 0, 0, 0
    aut1, cta1, cmn1, col1 = 0, 0, 0, 0
    aut2, cta2, cmn2, col2 = 0, 0, 0, 0
    aut3, cta3, cmn3, col3 = 0, 0, 0, 0
    for i in range(30):
        arribo(C1, choice(vehiculos))
        arribo(C2, choice(vehiculos))
        arribo(C3, choice(vehiculos))
    print('Tarifas:')
    print('Automoviles $47, Camionetas $59, Camiones $71, Colectivos $64')
    while not cola_vacia(C1): 
        v = atencion(C1)
        if v == 'Automovil':
            cab1 += 47
            aut1 += 1
        if v == 'Camioneta':
            cab1 += 59
            cta1 += 1
        if v == 'Camion':
            cab1 += 71
            cmn1 += 1
        if v == 'Colectivo':
            cab1 += 64
            col1 += 1
    while not cola_vacia(C2):  
        v = atencion(C2)
        if v == 'Automovil':
            cab2 += 47
            aut2 += 1
        if v == 'Camioneta':
            cab2 += 59
            cta2 += 1
        if v == 'Camion':
            cab2 += 71
            cmn2 += 1
        if v == 'Colectivo':
            cab2 += 64
            col2 += 1
    while not cola_vacia(C3):  
        v = atencion(C3)
        if v == 'Automovil':
            cab3 += 47
            aut3 += 1
        if v == 'Camioneta':
            cab3 += 59
            cta3 += 1
        if v == 'Camion':
            cab3 += 71
            cmn3 += 1
        if v == 'Colectivo':
            cab3 += 64
            col3 += 1
    print('La cabina 1 recaudo: $' + str(cab1))
    print('La cabina 2 recaudo: $' + str(cab2))
    print('La cabina 3 recaudo: $' + str(cab3))
    if cab1 > cab2 and cab1 > cab3:
        print('La cabina 1 recuado mayor cantidad de pesos')
    elif cab2 > cab1 and cab2 > cab3:
        print('La cabina 2 recuado mayor cantidad de pesos')
    else:
        print('La cabina 3 recuado mayor cantidad de pesos')
    print('--EN CABINA 1 INGRESARON--')
    print('Automoviles: ' + str(aut1))
    print('Camionetas: ' + str(cta1))
    print('Camiones: ' + str(cmn1))
    print('Colectivos: ' + str(col1))
    print('--EN CABINA 2 INGRESARON--')
    print('Automoviles: ' + str(aut2))
    print('Camionetas: ' + str(cta2))
    print('Camiones: ' + str(cmn2))
    print('Colectivos: ' + str(col2))
    print('--EN CABINA 3 INGRESARON--')
    print('Automoviles: ' + str(aut3))
    print('Camionetas: ' + str(cta3))
    print('Camiones: ' + str(cmn3))
    print('Colectivos: ' + str(col3))

#EJ 20
def aeropuerto():
    Cdesp = Cola()
    Cater = Cola()
    empresas = ['Singapore Airlines', 'Fly Emirates', 'LATAM', 'Qatar Airways',
            'Aerolineas Argentinas', 'Iberia', 'Turkish Airlines', 'Avianca']
    hs = [00.30, 02.00, 04.45, 07.15,
          12.15, 15.30, 18.05, 20.40]
    hl = [03.10, 04.30, 08.00, 11.25,
          14.30, 17.50, 21.20, 23.45]
    aeropuertos = ['Aeropuerto Alfa', 'Aeropuerto Beta', 'Aeropuerto Gamma',
            'Aeropuerto Delta', 'Aeropuerto Lambda', 'Aeropuerto Sigma',
            'Aeropuerto Omega', 'Aeropuerto Epsilon', 'Aeropuerto Kappa']
    tipo = ['Negocios', 'Carga', 'Pasajeros']
    te = [9, 3, 5]
    tater = [12, 5, 10]
    print('     Empresa      - Hora salida - Hora llegada -    Origen   -    Destino  - Tipo de vuelo')
    for i in range(len(empresas)):
        arribo(Cdesp, [empresas[i], hs[i], hl[i], choice(aeropuertos), choice(aeropuertos), choice(tipo)])
    barrido_cola(Cdesp)
    while not cola_vacia(Cdesp) or not cola_vacia(Cater):
        if not cola_vacia(Cater):
            avion = atencion(Cater)
            pos = tipo.index(avion[5])
            tiempo = tater[pos]
            print('Aterrizando avion de la empresa: ' + str(avion[0]))
            print('Horario de llegada: ' + str('{0:.2f}'.format(avion[2]).zfill(5)) + 'hs')
            print('Tipo de vuelo: ' + str(avion[5]))
            sleep(tiempo)
        else:
            avion = atencion(Cdesp)
            pos = tipo.index(avion[5])
            tiempo = te[pos]
            print('Despegando avion de la empresa: ' + str(avion[0]))
            print('Horario de salida: ' + str('{0:.2f}'.format(avion[1]).zfill(5)) + 'hs')
            print('Tipo de vuelo: ' + str(avion[5]))
            sleep(tiempo)
            arribo(Cater, avion)


# EJ 21
def personajes_marvel():
    cola = Cola()
    pers = ['Carol Danvers', 'Natasha Romanoff', 'Gamora Zen Whoberi',
                 'Tony Stark', 'Scott Lang', 'Steve Rogers', 'Stephen Strange']
    sh = ['Capitana Marvel', 'Black Widow', 'Gamora', 'Iron Man',
                  'Ant-Man', 'Capitan America', 'Doctor Strange']
    gen = ['F', 'F', 'F', 'M', 'M', 'M', 'M']
    for i in range(len(pers)):
        arribo(cola, [pers[i], sh[i], gen[i]])
    print('Nombre del personaje | Nombre del superheroe | Genero')
    barrido_cola(cola)
    print('')
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato[1] == 'Capitana Marvel':
            print('El personaje de la Capitana Marvel es: ' + dato[0])
        if dato[2] == 'F':
            print(dato[1] + ', personaje femenino')
        if dato[2] == 'M':
            print(dato[1] + ', personaje masculino')
        if dato[0] == 'Scott Lang':
            print('El nombre del superheroe de Scott Lang es: ' + dato[1])
        cad = dato[0]
        if cad[0] == 'S' or cad[0] == 'S':
            print('El personaje ' + dato[0] + ' empieza con S')
            print('El superheroe ' + dato[1] + ' empieza con S')
        if dato[0] == 'Carol Danvers':
            print('El superheroe de Carol Danvers es: ' + dato[1])

