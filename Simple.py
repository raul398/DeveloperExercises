
#coding = UTF-8

#Simple

#Hacer una función que genere una lista de diccionarios que contengan id y edad,
#donde edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10 elementos. 
#retornar la lista.
#Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a menor. 
#Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

class Simple():

    def __init__(self):
        self.row = 0
        self.Lista_Edad = list()
        le = self.getValue()
        self.getPrintDict(le)

    def getValue(self):
        edad = None
        print('USTED ESTA EN EL EJERCICIO UNO')
        print('POR FAVOR INGRESE DE 10 EDADES (UNA POR VEZ)')
        print(' ')
        while self.row < 10:
            self.row += 1
            edad = input('Ingrese edad: ')
            edad = self.getValidateInput(edad)
            if not edad:
                self.getValue()

            if 0 < edad < 100:
                self.Lista_Edad.append({self.row : edad})
            else:
                print('******  El rango de edad debe ser de 1 a 100  ******')
                self.getValue()
        return self.Lista_Edad

    def getValidateInput(self, edad):
        try:
            edad = int(edad)
            return edad
        except ValueError:
            print('*************  DEBE INGRESAR EL VALOR EN NUMEROS ENTEROS  *************\n')
            return False

    def getPrintDict(self, Lista_Edad):
        lista = sorted(Lista_Edad, key=lambda x: list(x.values()), reverse=True)
        print('El id de la edad mas joven es %s' %(list(lista[-1].keys()))[0])
        print('El id de la edad mas vieja es %s' %(list(lista[0].keys()))[0])
        print('El orden de mayor a menor es: \n')
        for row in lista:
            print(row)
        print(' ')



