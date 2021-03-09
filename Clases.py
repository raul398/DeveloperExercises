
#coding = UTF-8

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

class Circulo():

	exit = False
	pi = 3.14

	def __init__(self):
		self.radio = 0
		self.Diametro = 0
		self.getValue()
		if not self.exit:
			self.initProcess()

	def initProcess(self):
		self.getArea()
		self.getPerimeter()
		self.getMatriz()
		self.getExchageradio()

	def getValue(self):
		print(' ')
		print('USTED ESTA EN EL EJERCICIO TRES')
		print('POR FAVOR INGRESE EL VALOR DEL RADIO')
		print('SINO INGRESE SALIR PARA TERMINAR')
		print(' ')
		radio = input('Ingrese radio: ') #Toma el valor ingresado
		if radio.upper() == 'SALIR':
			print('*****************************************')
			print('*************  HASTA LUEGO  *************')
			print('*****************************************\n')
			self.exit = True
		else:
			radio = self.getValidateInput(radio) #Valida que el ingreso sea un numero entero
			if not radio:
				self.getValue()
			else:
				self.radio = radio
				self.Diametro = self.radio * 2 

	def getValidateInput(self, value):
		if not value or value <= '0':
			print('*************  DEBE INGRESAR EL VALOR MAYOR A CERO  *************\n')
			return False
		try:
			value = int(value)
			return value
		except ValueError:
			print('*************  DEBE INGRESAR EL VALOR EN NUMEROS  *************\n')
			return False



	def getArea(self):
		area = (self.radio ** 2) * self.pi
		print('El area del circulo es: %s \n' %area)

	def getPerimeter(self):
		diametro = self.Diametro * self.pi 
		print('El diametro del circulo es: %s \n' %diametro)

	def getMatriz(self):
		var = 0
		Matrix = [[var for e in range(self.Diametro)] for e in range(self.Diametro)]
		for row in Matrix:
			print(row)

	def getExchageradio(self):
		print('¿DESEA INGRESAR UNNUEVO VALOR PARA EL RADIO?')
		self.getValue()