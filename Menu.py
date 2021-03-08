
#coding = UTF-8

from Simple import Simple
from Matriz import Matriz
from Clases import Circulo

""" Este modulo es el principal donde
    se aloja el menu de opciones para 
    los distintos ejercicios """

class Menu():

    def __init__(self):
        self.MesajePrincipal()

    def getValidationOption(self, op):
        #Esta funcion valida si el ingreso es correcto dentro del rango del menu
        self.op = op
        if 0 < self.op < 4:
            return self.op
        elif self.op == 4:
            print(' ')
            print('################################################')
            print('####### Gracias por participar. Adios!!! #######')
            print('################################################')
            exit()
        else:
           return False

    def MesajePrincipal(self):
        #Muestra el menu de opciones para que el usuario seleccione
        print('-------------------- Menu principal -----------------------')
        print('------------- Ingrese 1 para el Ejercico 1 ---------')
        print('------------- Ingrese 2 para el Ejercico 2 ---------')
        print('------------- Ingrese 3 para el Ejercico 3 ---------')
        print('---------------- Ingrese 4 para salir --------------')
        print('------------------------------------------------------------\n')
        op = int(input('Seleccione una opcion para el ejercicio deseado: '))
        res = self.getValidationOption(op)
        if res:
            if res == 1:
                obj = Simple()
            elif res == 2:
                obj = Matriz()
            else:
                obj = Circulo()
            obj
        else:
            print('###############################################')
            print('####### debe ingresar una opcion valida #######')
            print('###############################################')
        self.MesajePrincipal()


Menu()