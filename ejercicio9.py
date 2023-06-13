"""
Obtener la liquidación del sueldo de un empleado y sus detalles, teniendo en cuenta que:
● La empresa empleadora, bonifica sobre el sueldo básico (SB) la antigüedad del empleado con un 1.2% por año. 
Además, paga el presentismo con un monto fijo del 8.33% (MP).
● Entre los descuentos, se deben contabilizar: el aporte jubilatorio (AJ) que representa un 11% del sueldo básico; 
aporte a obra social (OS) con un 3% del básico y el aporte gremial (AG) con un 1% del básico.
● El empleador paga además $ 800.00 por cónyuge y $ 400.00 por cada hijo.
● Son datos del problema: nombre y apellido del empleado, DNI, sueldo básico, antigüedad en años, 
estado civil ( 1 si es casado, 0 si es soltero ), número de hijos, presentismo ( 1 si corresponde cobrar, 0 si no cobra ).
Obtenga una salida con mensajes alusivos describiendo los haberes, los descuentos y el sueldo neto a cobrar.
"""

#Ingreso de datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dni = input("Ingrese su D.N.I: ")
sueldo_basico = float(input("Ingrese su sueldo basico: "))
antiguedad = float()(input("Ingrese su antiguedad: "))*0.012
estado_civil = float()(input("Ingrese su estado civil (1 = casado, 0 = soltero )"))
num_hijos = float()((input("Ingrese el numero de hijos que posee: ")))
presentismo = float()(input("¿Usted cobra presentismo? (1 = si, 0 = no)"))

#Beneficios (antiguedad y presentismo, conyuge e hijos)
sueldo_basico += sueldo_basico*antiguedad
sueldo_basico += num_hijos*400
if presentismo == 1:
    sueldo_basico += sueldo_basico*0.0833
if estado_civil == 1:
    sueldo_basico += 800
    
#Descuentos
sueldo_basico -= sueldo_basico*0.11  #jubilacion
sueldo_basico -= sueldo_basico*0.03  #obra social
sueldo_basico -= sueldo_basico*0.01  #gremio


#Mostrar
print("")







 