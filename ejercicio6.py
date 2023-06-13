"""
Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano,
elabore el algoritmo que permita obtener la distancia entre A y B.
"""

#Pedir variables
x_1 = float(input("Ingrese la coordenada x del punto A: "))
y_1 = float(input("Ingrese la coordenada y del punto A: "))
x_2 = float(input("Ingrese la coordenada x del punto B: "))
y_2 = float(input("Ingrese la coordenada y del punto B: "))

#Calcular distancia
distancia = ((x_2 - x_1)**2 + (y_2-y_1)**2)**0.5

#Imprimir distancia
print("La distancia entre el punto A y el punto B en el cuadrante positivo del plano cartesiano es: ", distancia)