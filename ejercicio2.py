"""
Ejercicio 2
Se necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales N1, N2 y N3.
"""
nombre_estudiante = input("Ingrese su nombre: ")

N1 = float(input("Ingrese la primer nota: "))
N2 = float(input("Ingrese la primer nota: "))
N3 = float(input("Ingrese la primer nota: "))

promedio = (N1+N2+N3)/3

print("El promedio de ", nombre_estudiante, " es: ", promedio)