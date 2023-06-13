"""
Ejercicio 3
Se necesita elaborar un algoritmo que solicite el número de respuestas correctas,
incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje final
considerando que por cada respuesta correcta tendrá 3 puntos, respuestas
incorrectas tendrá -1 y respuestas en blanco tendrá 0.
"""
correctas = int(input("Ingrese el numero de respuesta/s correcta/s: "))
incorrectas = int(input("Ingrese el numero de respuesta/s incorrecta/s: "))
blanco = int(input("Ingrese el numero de respuesta/s en blanco: "))

puntaje_correctas = correctas * 3
puntaje_incorrectas = incorrectas * (-1)
puntaje_blanco = blanco * 0

puntaje_final = puntaje_correctas + puntaje_blanco + puntaje_incorrectas

print("Su puntaje final es: ", puntaje_final)