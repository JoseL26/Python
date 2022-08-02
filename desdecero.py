from ast import Try
from xml.etree.ElementTree import tostring


nombre = "axel"
edad = 22
print ("mi nombre es:"+nombre)
calcu=2
restra=3
suma=calcu+restra
print(suma)
print("la suma de tres mas dos es:" + repr(suma))
a=3+5
print(a)
#tamaño del texto
len("hola mundo cruel")
#array
l=[1.54,"hola","mundo",3]
#agrego al array
l.append("adios")
#insertar en un elemento en una posicion especifica
l.insert(2,"que tal")
#para remover un elemento
#l.remove(1.54) y lo remueve
#para borrar de una posicion
#del l[1]
print(l)
#acceder al elemento
mostrar=l[2]
print(mostrar)
#si quiero excluir el ultimo de la lista
#l[1:3]
tamaño=len(l)
print(tamaño)
#ordena en orden alfabetico, en el caso de numeros los ordena en orden
k=["o","j","i","h"]
sorteado=sorted(k)
print(sorteado)

#matrices
#clave "c1" y su valor es 1 . es diccionario
d={"c1":1, 3:"hola","b2":True, "a_":1.4}
print(d)
#tupla
#t=(1,3,4)
#tarea
c=10000 #capital
i=0.015 #interes
n=5     #años
#capital inicial
m=c*((1+i)**n) #la potencia es igual a doble asterisco **
print(m)
#con el f adelante puede mostrar el resultado de m. para visualizar 2 decimales se coloca m:.2 y cerramos con f
print(f"el capital final es de: {m:.2f} ")
f=5
g=f*12*n
print(f"el gasto en comisiones es {g:.2f}")
saldo=m-g
print(f"el saldo final, quitando comisiones de {n} años, es {saldo:.2f}")
#vefiricando si hay ahorro o no
hay_ahorro= saldo > c
print(f"¿hemos incrementado el capital al finalizar?->{hay_ahorro}")

#----------------------------------#
#lista

lista_clase=["juan gonzales", "maria moreno", "jose navarro", "fatima gutierrez"]

#almacenar las notas 
#lista vacia
notas=[]
#añadimos las notas con append y dentro irá una tubla con sus 3 valores(3 notas)
notas.append((7.5,6.2,8.1))
notas.append((9.3,7.4,7.7))
notas.append((5.6,4.1,4.4))
notas.append((3.8,4.1,6.4))
suma_notas=sum(notas[0])
promedio=sum(notas[0])/len(notas[0])
print(lista_clase[0])
print(suma_notas)
print(promedio)
#agregando a notas medias
print(lista_clase)
print(notas)
#aca sale error
notas_medias={}
notas_medias[lista_clase[0]]=sum(notas[0])/len(notas[0])
#print(notas_medias)
#metemos las notas medias usando los nombres de la lista de clase
notas_medias[lista_clase[0]]=sum(notas[0])/len(notas[0])
notas_medias[lista_clase[1]]=sum(notas[1])/len(notas[1])
notas_medias[lista_clase[2]]=sum(notas[2])/len(notas[2])
notas_medias[lista_clase[3]]=sum(notas[3])/len(notas[3])

for nombre, nota_media in notas_medias.items():
    print(f"La nota media de {nombre} es un {nota_media:.1f}.")


#visualizar a los aprobados
aprobados={}
aprobados[lista_clase[0]]=notas_medias[lista_clase[0]] >= 5
aprobados[lista_clase[1]]=notas_medias[lista_clase[1]] >= 5
aprobados[lista_clase[2]]=notas_medias[lista_clase[2]] >= 5
aprobados[lista_clase[3]]=notas_medias[lista_clase[3]] >= 5

print(aprobados)
print(f"En total han aprobado {sum(aprobados.values())} estudiantes.")

# ejercicio
d = {'a': 8, 'b': 7, 'c': 9}
d['d'] = 5
d[1] = 'e'
print(5 in d)
#----
a, b = 1, 3
c = 2
print(b + 3 * c)
#------
l1 = [1, 3, 2]
l2 = [3, 1, 2]
print(l1[2] <= l2[1])
#-------
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l = l2 + l1
l[2:6] = [0, 0]
print(l)
#------
d = {'a': 8, 'b': 7, 'c': 9}
d['b'] = 8
del d['b']
print(len(d))
#------
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l = l2 + l1
print(l[3:-3])
#------
my_var1='hola'
print(my_var1)
#------
a, b = 1, 2
c = a / b
print(type(c))

#condicionales
a=12
if a<15:
    a = a + 1   
    print("Hola")

print("Adiós")

#------- try: except: tiene que contener algo porque sino sale error de tipeado
try:
    auto=5
    print(auto)
except:
    pass

#---- try: except: else:
#try:
#    c=a/b
#   print(c)
#except:
#       print("ha ocurrido un error")
#finally:
#       print("Adiós")
#si le agregamos a except Excetion as e , el error se almacena en "e" (puede ser otra letra) y se imprime con print(e)
#ejercicio tema 3
if saldo>c:
    print("la inversion ha sido rentable")
else:
    print("la inversion no ha sido rentable")

#------
l = [1, 3, 5, 7, 11]
print(3 in l[2:-1])
#-------
#
#----------
l = [1, 2, 3]
if len(l*2) > 5:
    print("caso 1")
else:
    print("caso 2")
#-----
#-----
a = 10
if a > 2:
    print("caso 1")
elif a > 5:
    print("caso 2")
else:
    print("caso 3")
#--------
l1 = [1, 3, 4, 5]
l2 = [2, 1, 3, 3]
if l1 < l2:
    print("caso 1")
elif l2 < l1:
    print("caso 2")
else:
    print("fin")
#----
a = 10
if a > 2:
    print("caso 1")
if a > 5:
    print("caso 2")
else:
    print("caso 3")
#----
l = list(range(5, 0, -1))
if l[1] / l[-1] > 0:
    print("caso 1")
else:
    print("caso 2")
#---- bucles tema 4
n=1
while n <=10:
    print(n)
    n=n+1 

#--- comprension de listas

#l=[]
#for el in l: #-- col es los elementos de la lista
#    if el % 2 == 1:
#        l.append(el * 2)
#    else:
#        l.append(-1)

#otra opcion para comprencion de listas

#-- l=[el * 2 for el in col] col es la lista

#-- otro ejemplo

#-- l_in = [3, -4, 0, 7, -1, 4, 2, 0]
#-- dos claves -> nombre y nota
estudiantes = [
    {"nombre":"José Fernandez", "nota":7.8},
    {"nombre":"Marina Jimenez", "nota":8.5},
    {"nombre":"Francisco Rios", "nota":4.3},
    {"nombre":"Josefa Sanchez", "nota":8.1},
    {"nombre":"Lucia Pisuerga", "nota":4.8},
    {"nombre":"Antonio Callao", "nota":3.8},
    {"nombre":"Felipe Barreno", "nota":9.7},
    {"nombre":"Elena Gonzales", "nota":5.1}
]

for estudiante in estudiantes:
    if estudiante["nota"] >= 5:
        print(estudiante["nombre"] + " ha aprobado la asignatura")
    else:
        print(estudiante["nombre"] + " ha suspendido la asignatura")

# nota promedio

nota_suma=0

for estudiante in estudiantes:
    nota_suma = nota_suma + estudiante["nota"]
nota_promedio = nota_suma / len(estudiantes)
print(f"la nota promedio es {nota_promedio:.2f}")

#-------- capital con bucle ------------
#tipo de interes ( en %, sobre 1)

i = 0.015

#Periodo en años

n=10

#comisiones mensuales(en euros)

f=5

#-- range(entre 0, hasta 20000, avanza de 5 en 5) capital (C)
# gastos asociados a comisiones (G) -- ** es potencia
# capital final (M)
# saldo final de la cuenta (S)
G = f * 12 * n
for C in range(0,20000,5):
    M = C * (1 + i) ** n
    S = M - G
    if S >= C:
        print(f"Si aportas almenos {C:.2f} euros, no tendrás perdidas.") #podemos imprimir el capital con {str(C)}
        break
if S < C:
    print("aunque aportes todo tu capital, tendrás perdidas.")

#------#
#metodo de biseccion

a = 2
b = 4
E = 1E-8

m = (a+b)/2

fm = m**3 - 3 * m**2 + 3 * m-4

while abs(fm) > E:
    if fm < 0:
        a = m
    else:
        b = m

m = (a+b)/2
fm = m**3 - 3 * m**2 + 3 * m-4

print(f"La función se anula en el punto x = {m:.4f}")

#-----------------------#
