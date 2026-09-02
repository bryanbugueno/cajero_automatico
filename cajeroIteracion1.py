import os				#Necesario para limpiar la consola (cls o clear)
import time				#Necesario para asignar tiempos de esperas
	
#Objetos imprimibles
tarjeta = """
 ┌───────────────────────────────┐
 │ █████████ BANCO UNIVERSITARIO │
 │ ┌───────────────────────────┐ │
 │ │ #### #### #### 8912       │ │
 │ │  VALIDA HASTA  12/28      │ │
 │ │  TOMAS GONZALEZ           │ │
 │ └───────────────────────────┘ │
 │        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       │
 │        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ VISA  │
 └───────────────────────────────┘
"""

#Interfaces del Cajero
pantalla_inicial = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │           BIENVENIDO          │
 │                               │
 │   Bienvenido, inserte su      │
 │   tarjeta para continuar.     │
 │                               │
 │   1) Acceder con Tarjeta      │
 │   2) Salir                    │
 └───────────────────────────────┘
"""
pantalla_ingresarPIN = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │           BIENVENIDO          │
 │                               │
 │          ¡Hola Tomas!         │
 │   Identifícate con tu clave.  │
 │                               │
 │  Ingrese su PIN: [ _ _ _ _ ]  │
 │                               │
 └───────────────────────────────┘
"""
pantalla_errorPIN = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │           BIENVENIDO          │
 │                               │
 │            MENSAJE            │
 │       ¡CLAVE INCORRECTA!      │
 │                               │
 │      Intenta nuevamente...    │
 │                               │
 └───────────────────────────────┘
"""
pantalla_despedida = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │                               │
 │            MENSAJE:           │
 │                               │
 │          Hasta Luego          │
 │    Gracias por visitarnos     │
 │                               │
 │                               │
 └───────────────────────────────┘
"""

#Variables de control
accesoAutorizado = False
operacion = 0

#Credenciales de acceso
claveValida = 2026
claveActual = 0000

#Variables del cliente
saldoActual = 500000

#Sirve para limpiar la consola
def LimpiarPantalla():
	if (os.name == "nt"):
		os.system("cls")
		
	else: os.system("clear")
	
#Solo sirve para ejecutar "una animación" (digamos)
def LeerTarjeta():
	print(tarjeta)
	print("- Leyendo tarjeta")
	print("Por favor, espere un momento...")
	
	#Asigna un tiempo de espera, mientras procesa
	time.sleep(1)
	LimpiarPantalla()
	
#Determina si la clave es correcta (true/false)
def Autentificador():
	print(pantalla_ingresarPIN)
	
	#Prueba si la clave esta en el formato indicado
	try:
		claveActual = int(input(" PIN: "))
		if (claveActual == claveValida):
			return True
		
	#Sino, devolverá como acceso no autorizado	
	except:
		return False

#Arranca desde acá el simulador
while (True):
	print(pantalla_inicial)
	eleccion = input(" ELEGIR (1-2): ")
	
	#Te llevará al menu principal de operaciones
	if (eleccion == "1"):
		LimpiarPantalla()
		LeerTarjeta()
		
		if (Autentificador() == True):
			accesoAutorizado = True
			
			print("\n MENSAJE: Usuario ha sido validado.")
			print(" MENSAJE: Has iniciado sesión.")
			break
			
		#Si la clave no es correcta, se reinicia el bucle
		else:
			LimpiarPantalla()
			print(pantalla_errorPIN)
			
			print("  AVISO: Sesión Terminada.")
			volver = input("\n- Presiona ENTER para continuar")
			LimpiarPantalla()
	
	#Te lleva a la pantalla de salida
	elif (eleccion == "2"):
		LimpiarPantalla()
		print(pantalla_despedida)
		break
	
	#Cuando escribes cualquier otra cosa
	else:
		print("No es una opción válida")
		volver = input("\n- Presiona ENTER para continuar")
		LimpiarPantalla()
