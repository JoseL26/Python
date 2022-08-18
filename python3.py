l = list(range(2, 11, 3))
print(l)

l = ["a", "b", 0, "c", 1]
for i in l:
    print(i)
    if i == 0:
        continue

l1 = list(range(3))
l2 = ["a", "b"]
for i in l1:
    for j in l2:
        print(j, i)

i = 0
while i < 100:
    i += 2
    if i == 50:
        break
else:
    print("Salida")

for i in range(100):
    print(i)
    if i % 3 == 0:
        break

d = {"a": 1, "b": 2}
for i in d:
    print(i)


s = "Hola, mundo"
print(s.split(","))

s = "Hola mundo"
print(s[3:7])

m = 100
age = int(input("Introduce tu edad "))
print(f"Te faltan {m - age} años")

s = "Hola mundo"
print(s[2:-2:2])

s = "Hola mundo"
a = s.split(" ")
print(":".join(a).title())

#    m = 100
#   age = input("Introduce tu edad")
#   print("Te faltan " + (m - age) + "años") sale error

