l = [7,1,4,3,9,11,5]

print(f"El elemento 9 está en la lista: {9 in l}")
print(f"El elemento 6 está en la lista: {6 in l}")

def busca_lineal(lista, elemento):
    for el in lista:
        if el==elemento:
            return True
    return False
#dlinea=busca_lineal(l,9) uso esta para volverlo objeto
print(f"El elemento 9 está en la lista: {busca_lineal(l,9)}")
print(f"El elemento 9 está en la lista: {busca_lineal(l,6)}")

#--busca dicotomica--#

l_ord=[1,3,4,5,7,8,9]

def busca_ordenado(lista1, otro_elemento):
    comienzo,final=0, len(lista1)
    while comienzo<=final:
        centro=comienzo+int((comienzo-final)/2)
        if lista1[centro] == otro_elemento:
            return True
        elif lista1[centro]>otro_elemento:
            final=centro
        elif lista1[centro]<otro_elemento:
            comienzo=centro+1
    return False


print(f"El elemento 9 está en la lista: {busca_ordenado(l,9)}")
print(f"El elemento 9 está en la lista: {busca_ordenado(l,6)}")

lista_grande=list(range(0, 300000000, 3))
print(f"La lista tiene {len(lista_grande)} elementos.")
# con %%timeit se mide el tiempo de ejecucion

#--diseño de algoritmos--#
l=[7,1,4,3,9,11,5]
print(f"La lista ordedana es: {sorted(l)}") #sorted devuelve la lista pero ordenada

def esta_ordenada(list):
    for i in range(len(list)-1): #con range recorremos los elementos de una lista.
        if list[i] >list[i+1]:
            return False
    return True

l1=[5,2,1,6,3,4]
l2=sorted(l1)

print(f"¿La lista {l1} está ordenada?: {esta_ordenada(l1)}")
print(f"¿La lista {l2} está ordenada?: {esta_ordenada(l2)}")

def ordena(list):
    #si esta ordenada
    if esta_ordenada(list):
        return list
    #si no esta ordenada
    list_ord = []
    while len(list) > 0:
        m=min(list)
        list_ord.append(m)
        list.remove(m)
    return list_ord

l=[5,2,1,6,3,4]
li=ordena(l)
print(f"La lista ordenada es: {li}")

##--invertir los elementos de una lista --##

def invertir(lista_n):
    lista_inv=[]
    for i in range(len(lista_n), 0, -1) :
        lista_inv.append(lista_n[i-1])
    return lista_inv

l_inver=[5,2,1,6,3,4]
l_inver=invertir(l_inver)
print(f"La lista invertida es: {l_inver}")

#--- creacion de un programa que ordene una lista de mayor a menor ---#
#--colocar la funcion ordenada dentro de la invertida.

#---- practica 3: El cambio---#
#cuando queremos dar el minimo numero de monedas, comenzamos dando las monedas mas grande
#diccionario caja

def cambio_minimo(cambio, caja):
    monedas=[]
    #el tendero buscara monedas iterativamente hasta completar el cambio.
    while cambio > 0:
        #obtenemos las monedas disponibles.
        monedas_disponibles = list(reversed(sorted(caja.keys())))

        #no podremos entregar el cambio si no hay monedas o la moneda mas pequeña es mayor que el cambio a devolver
        if len(monedas_disponibles) == 0 or monedas_disponibles[-1] > cambio:
            raise Exception("No hay suficientes monedas en caja para devolver")

        #buscar la moneda de mayor valor que podemos entregar.
        moneda_mayor = 0
        for moneda in monedas_disponibles:
            if moneda <= cambio:
                moneda_mayor=moneda
                break

        #anadimos la moneda a la lista de cambio
        monedas.append(moneda_mayor)
        #actualizar el cambio
        cambio= round(cambio-moneda_mayor, 2)
        #actualizar la caja
        caja[moneda_mayor] = caja[moneda_mayor] - 1
        if caja[moneda_mayor] == 0:
            caja.pop(moneda_mayor)
    return monedas


cambio_1 = 3.57
caja_1 ={
    0.01 : 17,
    0.02 : 3,
    0.05 : 4,
    0.1 : 7,
    0.2 : 3,
    0.5 : 3,
    2 : 6
}
monedas=cambio_minimo(cambio_1, caja_1)
print(f"Las monedas del cambio son: {monedas}")

#-------------#
#una tupla permite valores repetidos pero no se puede modificar, la lista si
#tupla =[
# (valor1, valor2, valor3),
# (valor1, valor2, valor3)]

#-----------#
#diccionario
#diccionario=[
# in:dentro,
# out:fuera]