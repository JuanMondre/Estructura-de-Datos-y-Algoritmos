import numpy as np
class PilaSecuencial:
    __tope:int
    __cant:int
    __elem:np.array
    
    def __init__(self,cant=0):
        self.__cant=cant
        self.__tope=-1
        self.__elem=np.empy(cant,dtype=int)
        
    def vacia(self):
        flag= False
        if self.__tope ==-1:
            print("La pila esta vacia")
            falg =True
        return flag
    
    def insertar(self,x):
        if self.__tope < self.__cant -1:
            self.__elem[self.__tope] = x
            self.__tope +=1
        
    def eliminar(self):
        if self.vacia():
            print("No se puede eliminar si la pila esta vacia")
        else:
            x = self.__elem[self.__tope]
            self.__tope -=1
            return x
        
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer si la pila esta vacia")
        else:
            for i in range(self.__tope,-1,-1) :
                print (self.__elem[i])
class Nodo:
    __elem:int
    __sig:object
    def __init__(self):
        self.__elem = None
        self.__sig= None 
    def setElem(self,elem):
        self.__elem = elem
    def setSig(self,sig):
        self.__sig = sig
    def getElem(self):
        return self.__elem
    def getSig(self):
        return self.__sig            

class PilaEnlazada:
    __tope:Nodo
    __cant:int
    
    def __init__(self, cant=0 ):
        self.__tope= None
        self.__cant= cant
        
    def insertar(self,x):
        nuevo_nodo = Nodo()
        nuevo_nodo = nuevo_nodo.setElem(x)
        nuevo_nodo.setSig(self.__tope)
        self.__tope = nuevo_nodo
        self.__cant+1

    def vacia(self):
        flag= False
        if self.__tope ==-1:
            print("La pila esta vacia")
            falg =True
        return flag
    
    def eliminar(self):
        if self.vacia():
            print("No se puede eliminar la pila esta vacia")
        else:
            x = self.__tope
            aux = self.__tope.getElem()
            self.__tope = aux.getSig()
            self.__cant-=1
            return x
    
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer la pila esta vacia")
        else:
            aux=self.__tope
            while aux is not None:
                print(aux.getElem())
                aux = aux.setSig()

class ColaSecuencial:
    __max_size:int
    __pr:int
    __ul:int
    __cant:int
    __elem:np.array
    
    def __init__(self, max_size=0):
        self.__max_size=max_size
        self.__pr=0
        self.__ul=0
        self.__cant = 0
        self.__elem = np.empty(max_size, dtype=int)
    
    def vacia(self):
        flag= False
        if self.__tope ==-1:
            print("La pila esta vacia")
            falg =True
        return flag
        
    def insertar(self,x):
        if self.__cant <= self.__max_size:
            self.__elem[self.__ul] = x
            self.__ul +=1
            self.__cant +=1 
    
    def eliminar(self):
        if self.vacia():
            print("No se puede eliminar si la cola esta vacia")
        else:
            x = self.__elem[self.__pr]
            self.__pr +=1
            self.__cant -=1
        return x
    def recorrer(self):
        if self.vacia():
            print("No se puede eliminar si la cola esta vacia")
        else:
            for i in range (self.__pr, self.__pr + self.__cant):
                print(self.__elem[i])
    
class ColaEnlazada:
    __pr:Nodo
    __ul:Nodo
    __cant:int
    
    def __init__(self, pr=None, ul= None, cant=0):
        self.__pr = pr
        self.__ul=ul
        self.__cant = cant

    def vacia(self):
        flag= False
        if self.__tope ==-1:
            print("La pila esta vacia")
            falg =True
        return flag
    
    def insertar(self,x):
        nuevo_nodo = Nodo(x)
        nuevo_nodo.setSig(None)
        if self.__ul is None:
            self.__pr = nuevo_nodo
        else:
            self.__ul.setSig(nuevo_nodo)
            self.__ul = nuevo_nodo
        self.__cant += 1
        
    def eliminar(self):
        if self.vacia():
            print("print la cola esta vacia")
        else:
            x = self.__pr
            aux = self.__pr.getElem()
            self.__pr = self.__pr.getSig()
            self.__cant -=1
            
            if self.__pr is None:
                self.__ul = None
        del aux
        return x
    
    def recorrer(self):
        if self.vacia():
            print("No se puede recorrer la cola esta vacia")
        else:
            ux = self.__pr
            while aux is not None:
                print(self.__pr.getElem())
                aux= aux.getSig()
    
            
            