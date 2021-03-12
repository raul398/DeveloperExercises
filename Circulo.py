
#coding = UTF-8


class Circulo():

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
				self.__init__(radio)

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
