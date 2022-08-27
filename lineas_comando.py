cmd_input = input("Ingresa un valor        : ")

print("Valor ingresado         : ", cmd_input)
print("Tipo del Valor ingresado: ", type(cmd_input))

#..comparar valores..#
input_a = input("Ingrese el valor A: ")
input_b = input("Ingrese el valor B: ")

a = float(input_a)
b = float(input_b)

print("-")
print("Resultado: ")

if a > b:
    print(f"* {a} es mayor que {b}")
elif a < b:
    print(f"* {a} es menor que {b}")
else:
    print(f"* {a} es igual a {b}")

#-----------#

##import argparse

##parser = argparse.ArgumentParser(
##    description='Compare numbers.',
##)

##parser.add_argument(
##    'numbers', 
##    metavar='number', 
##    type=float, 
##    nargs=2,
##    help='an integer for the accumulator'
##)

#arguments = parser.parse_args()

#a, b = arguments.numbers

#if a > b:
#   print(f"{a} es mayor que {b}")
#elif a < b:
#    print(f"{a} es menor que {b}")
#else:
#    print(f"{a} es igual a {b}")