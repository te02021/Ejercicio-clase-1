"""
Ingresar 3 valores numéricos y determinar e informar el mayor.
"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

mayor = num1

if num2 > mayor:
    mayor = num2
elif num3 > mayor:
    mayor = num3

print("El mayor es: ", mayor)