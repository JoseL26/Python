#transformar las cadenas"
s = "hoLA MuNDo"

 #muestra todo en minus
print(s.lower())
print(s.upper()) # muestra todo en mayus
print(s.capitalize()) # muestra la primera letra en mayus
print(s.title()) # muestra la 1ra letra de cada palabra en mayus
print(s.swapcase()) #invierte las mayus y las minus

#limpiador de cadena
p = " Hola "
print(p.strip()) #elimina espacios al comienzo y al final
print(p.ljust(8)) #alinea a la izq. hasta alcanzar 8 caracteres
print(p.rjust(8)) #alinea a la der. hasta alcanzar 8 caracteres
print(p.center(8)) #centra hasta alcanzar 8 caracteres.

#tranformacion de cadenas

c = "Hola_mundo_adiós"
print(c.split("_")) #vuelve cadenas
print(c.split("d")) #vuelve cadenas hasta antes y despues de la letra d

#unir elementos de una lista en una cadena
l=["Hola", "mundo", "adiós"]
print("_".join(l)) #une todo por medio de un _
print(" ".join(l)) #une todo por medio de un espacio
print("##".join(l)) #une todo por medio de michis

#Busqueda de cadenas
x = "Hola mundo"
print(x.find("mun")) #nos devuelve el orden de la m
print(x.find("o")) #nos devuelve el orden de la primera o

print("Hola\nmundo")
print("Hola\tmundo")
print("Hola\\mundo")

s = "x = "
x = 3.5
print(s + str(x))

nombre = input("Escribe aquí tu nombre:")

print(f"!Hola,{nombre}!")

#----Scrable----#
puntuaciones = { #ESTO ES UN DICCIONARIO
    'A':1,
    'B':3,
    'C':3,
    'D':2,
    'E':1,
    'F':4,
    'G':2,
    'H':4,
    'I':1,
    'J':8,
    'L':1,
    'M':3,
    'N':1,
    'Ñ':8,
    'O':1,
    'P':3,
    'Q':5,
    'R':1,
    'S':1,
    'T':1,
    'U':1,
    'V':4,
    'X':8,
    'Y':4,
    'Z':10,
}

palabra = input("Ingrese una palabra: ")

if len(palabra) > 7:
    raise Exception("La palabra es demasiado larga.")

for letra in palabra.upper():
    if letra not in puntuaciones.keys():
        raise Exception(f"El simbolo '{letra}' no es valido.")

puntos = 0
for letra in palabra.upper():
    puntos = puntos + puntuaciones[letra]

print(f'Por jugar la palabra "{palabra.upper()}" has obtenido {puntos} puntos.')

