import random

#Punto1
"""municipios = []
municipio = int(input("Ingresa cantidad de municipios: "))
for i in range(municipio):
    municipio = input(f"Digita el municipio {i + 1}: ")
    municipios += [municipio]

remover_elemento = municipios.pop()

print(municipios)"""

"""
Municipios = ['Bogota', 'Medellin', 'Popayan', 'Cali', 'Pereira']

nomostrarMunicipio = random.randint(0, 5 -1)
for i in range(len(Municipios)):
      if i != nomostrarMunicipio:
            print(Municipios[i])
"""


    #Punto2

"""
numeros = []

numeroD = int(input("Numeros totales a mostrar: "))

numeroI = int(input("Numero a inicializar: "))

for i in range(numeroD):
    numeros.append(numeroI)
    numeroI = numeroI + 4

print(numeros)
"""


    #Punto3


"""
DiccDepartamentos = {}

codigo = int(input("Ingresa el codigo: "))
nombre = input("Ingresa el nombre: ")
poblacion = int(input("Ingresa la poblacion: "))

municipiosCant = int(input("Ingresa la cantidad de municipios a digitar(pon 3): "))

for i in range(municipiosCant):
    municipios = input(f"Ingresa el municipio {i + 1}: ")
    DiccDepartamentos = {"codigo":codigo, "nombre":nombre, "poblacion":poblacion, "municipios":municipios}
    municipios = municipiosCant - 1
    print(DiccDepartamentos)
"""

"""
DicDepartamentos = {"codigo":"12",
"nombre":"luis",
"poblacion":"1.000.321",
"municipios":["Medellin", "Barbosa", "Envigado"]}

print(DicDepartamentos+DicDepartamentos["municipios"[1]])
"""

"""
Departamentos = {

   "Nombre":"Luis",
   "Codigo":"013",
   "Poblacion":"102312342",
   "Municipios":["Medellin","Bogota","Barranquilla"]

}

Departamentos["Municipios"] = Departamentos["Municipios"][1]
print(Departamentos)
"""

