## funciones ##
#--- funciones sin parametros ni retornos. ---#


from audioop import mul
from logging import exception
from time import altzone
from tkinter import N


def suma2_3():
    print(2+3)

suma2_3()

#--- funciones con parametros---##
def multiplicar_dos_numeros(a,b):
    print(a*b)

multiplicar_dos_numeros(4,6)
multiplicar_dos_numeros(1,5)

def funcion(a):
    a = 7
    return a

print(funcion(5))

def producto(l):
    prod=1
    for num in l: #con num toma el valor de l en cada iteracion
        prod=prod*num
    return prod

l=[1,3,5,7] #declaramos un valor
p=producto(l) #colocamos la declaracion con sus valores dentrode la funcion

print(p)

def resta(a,b):
    return a-b

r=resta(7,4)
print(r)

def potencia(a,b):
    return a ** b

p=potencia(4,3)
print(p)

## --- parametros variables en numeros --- ##
def suma_numeros(l):
    return sum(l) #funcion sumar

s=suma_numeros([1,2,3])
print(s)

#-- desempaquetado--#
#--desempaquetar una lista--#
def suma_otro(a,b):
    return a+b

l=[5,7]
q=suma_otro(*l) #desempaquetamos y volvemos a varios valores, en esta ocasion serían 2 valores y ya no una lista
print(q)

#--desempaquetar una diccionario--#
def suma_dic(a,b):
    return a+b

d={"b":8, "a":1}
w=suma_dic(**d)
print(w)

#--recursividad--#
#--factorial--#
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

f=factorial(5)
print(f)

#--practica1--#
#--fibonacci--#

def fibonacci_n(n): #--llamada recursidad es cuando la funcion se llama a sí mismo.
    if n == 1 or n == 2:
        return 1
    return fibonacci_n(n-1) + fibonacci_n(n-2)

f=fibonacci_n(15)
print(f)

#---generar los valores#
def fibonacci(l):
    n_2, n_1 = 1, 1 
    yield 1
    yield 1

    for i in range(2,l):
        n = n_2+n_1
        yield n
        n_2=n_1
        n_1=n

for f in fibonacci(15):
    print(f)

##---el area de un polinomio---##
def polinomio(x, *coefi):
    fx=0
    for i in range(len(coefi)):
        fx = fx + coefi[i]*(x**i)
    return fx

pol=polinomio(3,7,2,5,0,1)
print(pol)

##--integral del polinomio--##
def integral(a,b,n):
    area=0
    ancho=(b-a)/n
    for i in range(n):
        x=a+i*(b-a)/n
        alto=polinomio(x,-1,2,1)
        area+= ancho+alto
    return area

integ=integral(a=0,b=5,n=10000)
print(integ)


#-- Scrable --#

def scrablle(palabra, multi=1, **puntos):# ** con esto empaqueta las variables en un diccionario)
    puntuaciones = 0
    for letra in palabra:
        if letra not in palabra:
            raise exception(f"La letra {letra} no tiene puntuación asociada.")
        puntuaciones = puntuaciones + puntos[letra]
    return puntuaciones * multi

m_noax = scrablle("NOAX", N=1, O=1, A=1, X=8)
print(m_noax)

m_academy = scrablle("ACADEMY", multi=3, A=1, C=3, D=2, E=1, M=3, Y=4)
print(m_academy)

#-------------#
def prod (l):
    if len(l) == 1:
        return l[0]
    return l[0] * prod(l[1:])
l = [1, 2, 3, 4, 5]
print(prod(l))

#sale 120

#----------#
#def prod (l):
#    return l[0] * prod(l[1:])
#l = [1, 2, 3, 4, 5]
#print(prod(l))

#sale un indexError

#-----#
a = 7
def modify (a):
    a = a * a
modify(a)
print(a)
#sale 7

#---#
#g = genps()
#for p in g:
#    print(p)
#    if p > 10000:
#        break
#no produce un bucle infinito, no imprime todos los numeros menores a 10000

#----#
l = [1, 2, 3]
def modify (l, *ns):
    l.extend(ns)
    l = []
modify(l, "a")
print(l)

#sale [1,2,3,'a']

#-----#

def genps ():
    n = 2
    while (True):
        isp = True
        for d in range(2, n):
            if n % d == 0:
                isp = False
                break
        if isp:
            yield n
        n = n + 1

print(genps)
#no produce bucle infinito, ni devuelve todos los primos

#----------#
def power (b, e=3):
    return b ** e
p = power(b=3)
print(p)
#sale 27

#------------#

def sort_two (a, b):
    if a < b:
        return a, b
    else:
        return b, a
print(sort_two("c", "a"))
#sale ('a', 'c')

#---------------#
def compute (m, *l):
    return m * sum(l)
c = compute(3, 1, 2, 3)
print(c)
#sale 18

#---------#

def f (a, b):
    a + b
tot=f(3,1)
print(tot)

#sale ninguna

