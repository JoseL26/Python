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