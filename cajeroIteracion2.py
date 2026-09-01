import os				#Necesario para limpiar la consola (cls o clear)
import time				#Necesario para asignar tiempos de esperas
import datetime			#Necesario para incluir la fecha de la operación
	
#Objetos imprimibles
billete = """
 ┌───────────────────────────────┐
 │   █████████████████████████   │
 │   │        ○○○○○○○○       │   │
 │ $ │   - BANCO CENTRAL -   │ $ │
 │   │        ○○○○○○○○       │   │
 │   █████████████████████████   │
 └───────────────────────────────┘
"""
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
pantalla_operaciones = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │           HOLA TOMAS          │
 │                               │
 │   1) Giro en efectivo         │
 │   2) Consulta de saldo        │
 │   3) Salir                    │
 │                               │
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

#Interfaces de las Operaciones
pantalla_girarDinero = """
 ┌───────────────────────────────┐
 │       CAJERO AUTOMÁTICO       │
 │     - Retiro de Efectivo -    │
 │                               │
 │    ¿CUÁNTO NECESITAS GIRAR?   │
 │       (En multiplos de 5)     │
 │                               │
 │                               │
 │     *Monto mínimo: $ 5000     │
 └───────────────────────────────┘
"""

#Variables de control
accesoAutorizado = False
claveValida = 2026
claveActual = 0000
operacion = 0

#Variables del cliente
saldoActual = 500000

#Sirve para limpiar la consola
def LimpiarPantalla():
	if (os.name == "nt"):
		os.system("cls")
		
	else: os.system("clear")
	
#Para mostrar el menú principal (tras ingresar el PIN)
def MenuOperaciones():
	print(pantalla_operaciones)
	
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
		
def ValidarGiro(saldo):
	try:
		solicitado = int(input(" MONTO: "))
		if (solicitado <= saldo):
			
			#Si el monto NO es divisible por '5' devolverá '0'
			if (solicitado % 5000 == 0 and solicitado >= 5000):
				return solicitado
				
			else: return 0
			
		#Si el saldo es insuficiente, devolverá -1 (para identificarlo)
		else: return -1
		
	#Si el cliente no ingreso una entrada válida
	except:
		return 0
		
#Determina las denominaciones (valor) de los billetes a entregar
def ProcesarBilletes(monto):
	denominaciones = [20000, 10000, 5000]	#Los tipos de billetes que maneja el cajero
	resultado = {}							#Guardamos el resultado en un diccionario
	restante = monto						#El monto que iremos restando
	
	for dinero in denominaciones:
		cantidadActual = restante // dinero
		
		if (cantidadActual > 0):
			resultado[dinero] = cantidadActual
			restante -= cantidadActual * dinero
			
	return resultado
		
def EntregarEfectivo():
	print("\n- Procesando...")
	time.sleep(0.5)
				
	print("- Preparando efectivo...\n")
	time.sleep(0.5)
	
	LimpiarPantalla()
	print(billete)
	time.sleep(0.25)
		
def EmitirComprobante(monto, saldo, fecha):
	print("┌───────────────────────────────┐")
	print("|       << COMPROBANTE >>       |")
	print("|                               |")
	print("	Monto: $", monto)
	print("	Saldo Actual: $", saldo)
	print("	Cuenta: Cuenta Vista")
	print("	Fecha:", fecha)
	print("└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘")
	
def MostrarSaldo(saldo, fecha):
	print(" ┌───────────────────────────────┐")
	print(" |     << CONSULTA DE SALDO >>   |")
	print(" |                               |")
	print("	Disponible: $", saldo)
	print("	Cuenta: Cuenta Vista")
	print("	Fecha:", fecha)
	print(" └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘")

#Arranca desde acá el simulador
while (True):
	print(pantalla_inicial)
	eleccion = input(" ELEGIR (1-2): ")
	
	#Te llevará al menu principal de operaciones
	if (eleccion == "1"):
		LimpiarPantalla()
		LeerTarjeta()
		
		if (Autentificador() == True):
			LimpiarPantalla()
			accesoAutorizado = True
			
			print(pantalla_operaciones)
			break
			
		#Si la clave no es correcta, se reinicia el bucle
		else:
			LimpiarPantalla()
			print(pantalla_errorPIN)
			
			#Muestra el típico mensaje de "clave inválida"
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
		
#Si su ingreso fue validado, podrá ver y operar con el Cajero
if (accesoAutorizado == True):
	operacion = input(" ELEGIR (1-3): ")
	
	#Para el caso de 'Retirar efectivo' (o girar dinero)
	if (operacion == "1"):
		while (True):
			LimpiarPantalla()
			print(pantalla_girarDinero)
			
			#El monto ingresado es validado, si no es válido, será '0'
			montoSolicitado = ValidarGiro(saldoActual)
			
			#Entonces si el monto es mayor a '0'. Se procede con el giro
			if (montoSolicitado > 0):
				
				#Procedimiento para clasificar los billetes necesarios
				billetes = ProcesarBilletes(montoSolicitado)
				print("- Preparando billetes: \n")
				
				#Para cada tipo de billete y su cantidad, se imprimirá por consola
				for valor, cantidad in billetes.items():
					print("  ", valor, "x", cantidad)
					time.sleep(0.35)
				
				#Solo imprime una representación de un billete en ASCII
				EntregarEfectivo()
				
				#Resta al saldo actual del cliente
				saldoActual -= montoSolicitado
				fechaRegistro = datetime.date.today()
				print("- Con fecha", fechaRegistro)
				
				print("  Se ha realizado el siguente giro: \n")
				EmitirComprobante(montoSolicitado, saldoActual, fechaRegistro)
				break
				
			#Si la 'ValidarGiro' devuelve -1, es porque excede el máximo disponible
			elif (montoSolicitado == -1):
				print("\n- Monto solicitado excede el máximo disponible")
				print(" SALDO DISPONIBLE:", saldoActual)
				
				#Vuelve a iniciar el while, usé un input como "boton de continuar"
				esperar = input("\n Presiona 'ENTER' para continuar")
				
			#Sino, se reinicia el while, usé un input como "boton de continuar"
			else:
				print("- NO es un monto válido.")
				esperar = input(" Presiona 'ENTER' para continuar")
		
	#Para consultar el saldo disponible
	elif (operacion == "2"):
		print("- Consultado...\n")
		fechaConsulta = datetime.date.today()
		
		time.sleep(0.25)
		MostrarSaldo(saldoActual, fechaConsulta)
		print("\n - Gracias por operar con nosotros -")
		
	#Sino, te llevará a la pantalla de cierre de sesión
	else:
		LimpiarPantalla()
		print(pantalla_despedida);

