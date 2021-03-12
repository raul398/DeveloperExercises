
#coding = UTF-8

from Circulo import Circulo

#Clases

#Escribir una clase en python llamada círculo que contenga un radio, 
#con un método que devuelva el área y otro que devuelva el perímetro del círculo. 
#Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error 
#amigable al usuario e impidiendo la instanciación.
#Si printeamos el objeto creado debe mostrarse una representación amigable.
#El objeto debe tener su atributo radio modificable, 
#si se le intenta setear un valor <= 0 mostrar un error y no permitir modificación.
#Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto 
#con el radio multiplicado por n. No permitir la multiplicación por números <= 0

class Clases():

	def __init__(self):
		print(' ')
		print('USTED ESTA EN EL EJERCICIO TRES')
		self.getValue()
			

	def getValue(self):
		print(' ')
		print('POR FAVOR INGRESE EL VALOR DEL RADIO')
		print('SINO INGRESE SALIR PARA TERMINAR')
		print(' ')
		radio = input('Ingrese radio: ') #Toma el valor ingresado
		if radio.upper() == 'SALIR':
			print('*****************************************')
			print('*************  HASTA LUEGO  *************')
			print('*****************************************\n')
			return False
		else:
			radio = self.getValidateInput(radio) #Valida que el ingreso sea un numero entero
			if not radio:
				self.getValue()
			else:
				obj = Circulo(radio)
				return obj

	def getValidateInput(self, value):
		try:
			value = int(value)
			if value <= 0:
				print('*************  DEBE INGRESAR EL VALOR MAYOR A CERO  *************\n')
				return False
			return value
		except ValueError:
			print('*************  DEBE INGRESAR EL VALOR EN NUMEROS  *************\n')
			return False

