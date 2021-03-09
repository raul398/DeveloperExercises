
#coding = UTF-8
import random

#Matriz

#Crear una matriz de 5x5 randomizada con números enteros, 
#encontrar secuencia de 4 números consecutivos horizontal 
#o vertical y si se encuentra mostrar la posición inicial y final.

class Matriz():

	def __init__(self):
		Matrix = self.getMatrix()
		dic = self.getCoincidences(Matrix)
		self.getFourCoincidences(dic)

	def getMatrix(self):
		#Se crea la matriz de 5x5
		Matrix = [[random.randint(0, 10) for e in range(5)] for e in range(5)]
		for row in Matrix:
			print(row)
		return Matrix

	def getCoincidences(self, lista):
		#Busca coincidencias horizontal y verticalmente
		dic = dict()
		for row in lista:
			for col in range(5):
				key = row[col]
				if key not in dic:
					dic[key] = 1
				elif key in dic.keys():
					if col > 0:
						prevCol = col-1
						if row[prevCol] == key:
							dic[key] += 1
					if lista.index(row) > 0:
						prevRow = int(lista.index(row))-1
						if lista[prevRow][col] == key:
							dic[key] += 1
		return dic

	def getFourCoincidences(self, dic):
		#Esta funcion busca un numero que tenga un valor 4
		flag = False
		for key, value in dic.items():
			if value == 4:
				flag = True
				print('El numero %s se repite 4 vertical u horizontalmente' %key)
		if not flag:
			print('No existen numeros que se repitan 4 veces vertical u horizontalmente')