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