import numpy as np
class pilaSecuencial:
    __tope:int
    __cant:int
    __elem:np.array
    
    def __init__(self,cant):
        self.__tope = 0
        self.__cant = cant
        self.__elem = np.zeros(cant, dtype= int)
        
    def vacia(self):
        return self.__tope ==0
        
        
    def insertar(self, x):
        if self.__tope == self.__cant:
            print("La pila esta llena")
        else:
            self.__elem[self.__tope] = x
            self.__tope +=1
    
    def eliminar(self,x):
        if self.vacia():
            print("La pila esta vacia")
        else:    
            x = self.__elem[self.__tope-1]
            self.__tope -= 1
        return x
    
    def recorrer(self):
        if self.vacia():
            print("La pila esta vacia")
        else:      
            for i in range(self.__tope-1,-1,-1):
                print(self.__elem[i], end=" ")
                
"""
if __name__ == '__main__':
    pila = pilaSecuencial(8)
    n=4
    while n > 0:
        resto = n%2
        pila.insertar(resto)
        n = n//2
    pila.recorrer()    
"""        
    
class colaCircular:
    __pr:int
    __ult:int
    __max_size:int
    __elem:np.array
    __cant:int
    
    def __init__(self,max_size):
        self.__pr=0
        self.__ul=0
        self.__cant = 0    
        self.__max_size = max_size
        self.__elem = np.zeros(max_size, dtype=int)
    
    def vacia(self):
        return self.__cant == 0
        
    def insertar(self,x):
        if self.__cant == self.__max_size:
            print("La cola esta llena")
        else:
            self.__elem[self.__ul]=x
            self.__ul = (self.__ul+1) % self.__max_size
            self.__cant +=1
            
    def eliminar(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            x = self.__elem[self.__pr]
            self.__pr    = (self.__pr+1) % self.__max_size
            self.__cant -=1        
        return x
        
    def recorrer(self):
        if self.vacia():
            print("Nada que eliminar")
        else:
            i = self.__pr
            j = 0
            while j < self.__cant:
                print(self.__elem[i])
                i = (i+1) % self.__max_size
                j +=1
                
if __name__ == '__main__':
    cola = colaCircular(4)
    for i in range(4):
        cola.insertar(i)
    cola.recorrer()
    cola.eliminar()
    cola.recorrer()
    

class Nodo:
    __elem:int
    __sig:object
    
    def __init__(self):
        self.__elem = None
        self.__sig = None
        
    def getElem(self):
        return self.__elem
    
    def getSig(self):
        return self.__sig
    
    def setElem(self,elem):
        self.__elem = elem
    
    def setSig(self,sig):
        self.__sig = sig 

class ListaEncadana:
    __cabeza: Nodo
    __cant: int
    
    def insertar(self, elem, posicion):
        """Inserta un elem en una posición específica."""
        if posicion < 0 or posicion > self.__cant:
            print("Posición fuera de rango")

        nuevo_nodo = Nodo(elem)

        if posicion == 0:
            nuevo_nodo.setSig(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            nodo_actual = self.__cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.getSig()

            nuevo_nodo.setSig(nodo_actual.getSig())
            nodo_actual.setSig(nuevo_nodo)

        self.__cant += 1

    def vacia(self):
        return self.__cant ==0
    
    def anterior(self,pos):
        if pos < 0 or pos> self.__cant:
            print("posicion fuera de rango")
        if 
            