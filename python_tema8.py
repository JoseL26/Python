def f(l, it):
    for i in range(len(l)//2):
        if l[i] == it:
            return True
    return False

lista=[1,3,2,4,8,6,9]
mostrar=f(lista, 2)
print(f"mostrando {mostrar}")