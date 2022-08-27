#filename = "asistentes_al_taller_de_python.txt"
#filehandler = open(filename, mode="r", encoding="utf-8")
#filehandler = open(filename, mode="r", encoding="utf-8")

#contents = filehandler.read()
#contents

import os
#os.mkdir("./sample_directory/")

if os.path.exists("./sample_directory/"):
    print("El directortio ya existe")
else:
    os.mkdir("sample_directory")
    print("Se ha creado el directortio")

sample_file = "./sample_directory/sample_file.txt"

file_handler = open(sample_file, mode="w", encoding="utf-8")
file_handler.write("sample content")
file_handler.close()

arch=open('archivo1.txt', 'w')
arch.write('hola mundo')
arch.close

for file in os.listdir("./sample_directory/"):
    file_path = f"./sample_directory/{file}"
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"archivo {file_path}")