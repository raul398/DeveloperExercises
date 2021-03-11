
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
				obj = Círculo(radio)
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

class Círculo(Clases):

	pi = 3.14

	def __init__(self, radio):
		self.radio = radio
		self.Diametro = self.radio * 2 
		self.Perimeter = 0
		self.area = 0
		self.initProcess()

	def initProcess(self):
		self.getArea() #Calcula el area
		self.getPerimeter() #Calcula el perimetro
		self.getPrintCircle() #Dibuja el circulo
		self.getExchageradio() #Pregunta si continua y cambia el radio o finaliza

	def getArea(self):
		self.area = (self.radio ** 2) * self.pi
		print('El area del circulo es: %s \n' %self.area)

	def getPerimeter(self):
		self.Perimeter = self.Diametro * self.pi 
		print('El diametro del circulo es: %s \n' %self.Perimeter)

	def getPrintCircle(self):

		self.printCircle(self.Diametro, self.Diametro, self.radio, self.Perimeter)

	def printCircle(self, x, y, radio, perimeter):
		import turtle as t

		t.setup(perimeter, perimeter, 0, 0) #tamaño de la ventana
		t.screensize(self.area, self.area) #area donde se va a dibujar
		t.hideturtle() #Esconde el cursor
		t.goto(0,0) #Posocion del cursor
		t.pendown() #Baja el lapiz
		t.circle(radio) #Tamaño del circulo
		t.penup() #L4evanta el lapiz

	def getExchageradio(self):
		print('¿DESEA INGRESAR UN NUEVO VALOR PARA EL RADIO?')
		self.getontinueOtNot()


	def getontinueOtNot(self):
		values = ['SI', 'NO']
		value = input('Ingrese SI/NO: ') #Toma el valor ingresado
		if value.upper() not in values:
			print(' ')
			print('*************************************************************')
			print('*************  DEBE INGRESAR UNA OPCION VALIDA  *************')
			print('*************************************************************\n')
			print(' ')
			self.getontinueOtNot()

		if value.upper() == 'NO':
			print('*****************************************')
			print('*************  HASTA LUEGO  *************')
			print('*****************************************\n')
			return False
		else:
			Clases()