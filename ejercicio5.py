"""
Ejercicio 5
Elaborar un algoritmo que permita calcular el número de micro discos 3.5 necesarios para hacer una copia de seguridad, 
de la información almacenada en un disco duro cuya capacidad se conoce. 
Hay que considerar que el disco duro está lleno de información, además expresado en gigabyte. 
Un micro disco tiene 1.44 megabyte y un gigabyte es igual a 1,024 megabyte.
"""

disco_duro_gb = float(input("Ingrese la capacidad del disco duro en Gb: "))
disco_duro_mb = disco_duro_gb * 1024

numero_micro_discos = disco_duro_mb/1.44

print("El numero de micro discos que necesita son: ", numero_micro_discos)
