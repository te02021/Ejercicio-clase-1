"""
Se ingresa un número entero como dato. Determine si es par o impar e informe un mensaje alusivo.
"""

numero = int(input("Ingrese el numero entero: "))

if numero % 2 == 0:
    print("El numero ", numero,"es par")
else:
    print("El numero ", numero,"es impar")