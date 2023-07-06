"""
Ejercicio 4
Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados,
por ABC club en el torneo apertura, se debe de mostrar su puntaje total, teniendo en cuenta que 
por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.
"""
ganados = int(input("Ingrese el numero de partidos ganados: ")) * 3
perdidos = int(input("Ingrese el numero de partidos perdidos: ")) * 0
empatados = int(input("Ingrese el numero de partidos empatados: ")) * 1

puntaje_total = ganados + perdidos + empatados

print("El ABC club tiene: ", puntaje_total, "puntos en el torneo apertura")
#probando modificando un archivo
