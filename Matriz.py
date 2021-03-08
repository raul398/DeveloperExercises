
#coding = UTF-8
import random

#Matriz

#Crear una matriz de 5x5 randomizada con números enteros, 
#encontrar secuencia de 4 números consecutivos horizontal 
#o vertical y si se encuentra mostrar la posición inicial y final.

class Matriz():

	def __init__(self):
		self.getMatrix()

	def getMatrix(self):
		print('ESTA ES LA FUNCION DEL EJECICIO TRES')
		Matrix = [[random.randint(0, 10) for e in range(5)] for e in range(5)]
		for row in Matrix:
			print(row)