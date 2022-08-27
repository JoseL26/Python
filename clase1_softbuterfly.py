diccionario ={
    "color": "verde",
    "cantidad":35,
    "precio":"S/. 5.00"
}
for i in diccionario:
    print(diccionario[i])

#---Funciones softbuterfly---#

def get_schoolar_anual_mean_score(student_name, score1, score2, score3, score4):
    accumulated_score = score1 + score2 + score3 + score4
    anual_mean_score = accumulated_score / 4

    print(f"El promedio anual del alumno {student_name} es {anual_mean_score}")

get_schoolar_anual_mean_score("Whithmann", 18, 15, 15, 18)

#---------------#
def mean(number1, number2):
    return (number1 + number2) / 2


print(mean(5, 6))
#-----------#
def mean1(*args):
    # sum me da la suma de los valores al interior de una lista o tupla (u otros tipos iterables)
    # len me da la cantidad de valores al interior de una lista o tupla (u otros tipos iterables)
    return sum(args) / len(args)

print(mean1(1, 2, 3, 4, 5, 6, 7, 8, 9))
#-----------# *Args (entran valores sin nombres) y *kwargs (entran valores con nombre)
def describe(**kwargs):
    print("-" * 6)
    for key, value in kwargs.items():
        print(f"Key  : {key}")
        print(f"Value: {value}")
        print("-" * 6)

describe(eduardo=1, martin=2)

#-------------#
def read_arguments(*args, **kwargs):
    for i, arg in enumerate(args, 1):
        print(f"{i}. {arg}")

    for j, (key, value) in enumerate(kwargs.items(), 1):
        print(f"{i+j}. {key}: {value}")

read_arguments("python", "c++", "java", paradigma="POO", compilados=False)
#-- nivel intermedio----------#
#------decoradores-----------------# para debuguear, modificar, mapeo de errores
def logger(func):
    def log_func(*args):#recibe los argumentos(3,3) luego va a imprimir el runing
        print('Running "{}" with arguments {}'.format(func.__name__, args)) #1er espacio en blanco(func.__name), segundo (args),recepciona argumentos 
        print(func(*args))

    return log_func

@logger
def add(x, y):
    return x + y  

add(3, 3)

#---- creacion de archivos---#
