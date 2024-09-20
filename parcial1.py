import numpy as np
class ColaSecuencial:
    __max_size:int
    __pr:int
    __ul:int
    __cant:int
    __elem:np.array
    
    def __init__(self, max_size =0):
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        self.__elem = np.empty(max_size,dtype=int)
        
    def crearCola(self):
        dim = int (input("Ingrese el tamaño de la cola:"))
        cola = ColaSecuencial(dim)
        return cola
    
    def vacia(self):
        flag = False
        if self.__max_size == 0:
            print("La cola esta vacia")
            flag = True
        return flag
    
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__pr, self.__pr + self.__cant):
                print (self.__elem[i])
        else:
            print("No se puede mostrar nada si la cola esta vacia")
            
    def insertar(self,x):
        if self.__cant <= self.__max_size:
            self.__elem[self.__ul] = x
            self.__ul +=1
            self.__cant+=1
            
    def suprmir ( self):
        if self.vacia():
            print("No hay nada para eliminar")
        else:
            x = self.__elem[self.__pr]
            self.__pr +=1
            self.__cant-=1
        return x
    
    
class PilaSecuencial:
    __tope:int
    __cant:int
    __elem:np.array
    
    def __init__(self,cant=0):
        self.__tope = -1
        self.__cant = cant
        self.__elem = np.empty(cant, dtype=int)
    
    def vacia(self):
        flag = False
        if self.__max_size == 0:
            print("La cola esta vacia")
            flag = True
        return flag
    
    def suprimir(self):
        if self.vacia():
            print("No hay nada para eliminar")
        else:
            x = self.__elem[self.__tope]
            self.__tope -=1
        return x             
    
