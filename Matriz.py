
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
		print(' ')
		print('USTED ESTA EN EL EJERCICIO DOS')
		print('SE GENERA UNA MATRIZ DE 5 X 5')
		print(' ')
		#Se crea la matriz de 5x5
		Matrix = [[random.randint(0, 9) for e in range(5)] for e in range(5)]
		for row in Matrix:
			print(row)
		return Matrix

	def getCoincidences(self, lista):
		#Busca coincidencias horizontal y verticalmente
		dic = dict() #Se crea un dicionario general para los diccionarios
		dic['dicVert'] = dict() #diccionario vertical
		dic['dicHorz'] = dict() #diccionario horizontal
		# recorre la matrix --> lista
		#row es cada fila 
		#len(row) es el rango de la fila que permitira recorrer cada elemento de la fila
		for row in lista:
			for col in range(0, len(row)):
				key = row[col] #valor de un elemento que se utiliza para clave
				# Si no existe la clave en el diccionario la crea
				#Guarda una lista con elementos dict() que contiene clave (x, y) para el indice
				if key not in dic['dicVert']:
					dic['dicVert'][key] = [{'x':lista.index(row), 'y':col}]
				elif key not in dic['dicHorz']:
					dic['dicHorz'][key] = [{'x':lista.index(row), 'y':col}]
				else:
					#Si es mayor a uno resta 1 para contar con el valor anterio de fila o columna
					#si es igual hace append() sobre la lista de indices
					if col > 0:
						prevCol = col-1
						if row[prevCol] == key:
							dic['dicHorz'][key].append({'x':lista.index(row), 'y':col})
						elif 0<len(dic['dicHorz'][key])<2:
							dic['dicHorz'][key] = [{'x':lista.index(row), 'y':col}]
					if lista.index(row) > 0:
						prevRow = int(lista.index(row))-1
						if lista[prevRow][col] == key:
							dic['dicVert'][key].append({'x':lista.index(row), 'y':col})
						elif 0<len(dic['dicVert'][key])<2:
							dic['dicVert'][key] = [{'x':lista.index(row), 'y':col}]
		return dic

	def getFourCoincidences(self, dic):
		#Esta funcion busca un numero que tenga un valor 4
		#recorre cada dict()
		horz = False
		for key, value in dic['dicHorz'].items():
			if len(value) == 4:
				horz = True
				print('El numero %s se repite 4 veces horizontalmente' %key)
				print('Su posición inicial es %s y su posición final es %s' %(value[0], value[-1]))
		if not horz:
			print(' ')
			print('No existen numeros que se repitan 4 veces horizontalmente\n')
		vert = False
		for key, value in dic['dicVert'].items():
			if len(value) == 4:
				vert = True
				print('El numero %s se repite 4 veces verticalmente' %key)
				print('Su posición inicial es %s y su posición final es %s' %(value[0], value[-1]))
		if not vert:
			print(' ')
			print('No existen numeros que se repitan 4 veces verticalmente\n')

