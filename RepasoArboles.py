class Nodo:
    __valor:int
    __izq:'Nodo'
    __der:'Nodo'
    
    def __init__(self,valor):
        self.__valor=valor
        self.__izq = None
        self.__der = None
    
    def getValor(self):
        return self.__valor
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setValor(self,valor):
        self.__valor = valor
    def setIzq(self,nodo):
        self.__izq =nodo
    def setDer(self,nodo):
        self.__der = nodo
    
class ABB:
    __raiz :Nodo
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self,nodo):
        self.__raiz =nodo
    
    def vacio(self):
        return self.__raiz is None
            
    
    def insertar(self,valor,nodo):
        if self.vacio():
            self.__raiz = Nodo(valor)
        elif valor < nodo.getValor():
            if nodo.getIzq() is None:
                nodo.setIzq(Nodo(valor))
            else:
                self.insertar(valor,nodo.getIzq())
        else:
            if nodo.getDer() is None:
                nodo.setDer(Nodo(valor))
            else:
                self.insertar(valor,nodo.getDer())
    
    def insertarIterativo(self,valor):
        nuevoNodo = Nodo(valor)
        if self.vacio():
            self.__raiz = nuevoNodo
            return nuevoNodo    
        nodoActual = self.__raiz
        flag = True
        while flag:
            if valor < nodoActual.getValor():
                if nodoActual.getIzq() is None:
                    nodoActual.setIzq(nuevoNodo)
                    flag=False
                else:
                    nodoActual = nodoActual.getIzq()
            else:
                if nodoActual.getIzq() is None:
                    nodoActual.setDer(nuevoNodo)
                    flag=False
                else:
                    nodoActual = nodoActual.getIzq()
    
    def inorden(self, nodo):                                                   
        if  nodo is not None:
            self.inorden(nodo.getIzq())                                   
            print(nodo.getValor(),end=" ")                                    
            self.inorden(nodo.getDer())
    
    def preorden(self, nodo):                                                
        if nodo is not None:
            print(nodo.getValor(), end=" ")                              
            self.preorden(nodo.getIzq())                          
            self.preorden(nodo.getDer())                               
        
    def postorden(self, nodo):                                                  
        if nodo is not None:
            self.postorden(nodo.getIzq())                                 
            self.postorden(nodo.getDer())                                   
            print(nodo.getValor(), end=" ")    

    def hijo(self,nodo,hijo, padre):
        if self.vacio():
            print("Arbol vacio")
            return False
        elif nodo is None:
            return False
        elif nodo.getValor() == padre:
            return nodo.getDer().getValor() == hijo or  nodo.getIzq().getValor() == hijo
        elif nodo.getValor() > padre:
            return self.hijo(nodo.getIzq(),hijo,padre)
        else: 
            return self.hijo(nodo.getDer(),hijo,padre)
        
    def buscar(self,nodo,valor):
        if self.vacio():
            print("ABB VACIO")
            return False
        if nodo is None:
            print("No existe el nodo")
            return False
        if nodo.getValor() == valor:
            print("Se encontro el elemento")
            return nodo.getValor()
        else:
            if valor < nodo.getValor():
                return self.buscar(nodo.getIzq(),valor)
            else:
                return self.buscar(nodo.getDer(),valor)
    
    def buscarIterativo(self,valor):
        actual = self.__raiz
        while actual is not None:
            if actual.getValor() == valor:
                return actual.getValor()
            elif valor < actual.getValor():
                actual = actual.getIzq()
            else:
                actual = actual.getDer()

    def nivel(self,valor):
        nivel = 1
        nodoActual = self.__raiz
        if self.vacio():
            print("ABB VACIO")
        else:  
            while nodoActual.getValor() != valor:
                if valor < nodoActual.getValor():
                    nodoActual = nodoActual.getIzq()
                    nivel+=1
                else:
                    nodoActual = nodoActual.getDer()
                    nivel+=1
        return nivel
        
    def nivelRecursivo(self,nodo, valor, nivel=1):
        if self.vacio():
            print("El arbol esta vacio")
        elif nodo is None:
            print("No se encuentra el elemento")
        elif nodo.getValor() == valor:
            print(F"Nivel de {valor} es: {nivel}")
        elif valor < nodo.getValor():
            self.nivelRecursivo(nodo.getIzq(),valor,nivel+1)
        else:
            self.nivelRecursivo(nodo.getDer(),valor,nivel+1)

    def altura(self,nodo):
        if nodo is None:
            return 0
        else:                                                
            return max(self.altura(nodo.getDer()),self.altura(nodo.getIzq())) + 1  #Como es una funcion recursiva incremento con el +1        
        
    def alturaIterativo(self):
        if self.vacio():
            print("Arbol vacio")
        else:
            nodoActual = self.__raiz
            alturaIzq=1
            alturaDer=1
            while nodoActual is not None:
                nodoActual = nodoActual.getIzq()
                alturaIzq+=1
            while nodoActual is not None:
                nodoActual = nodoActual.getDer()
                alturaDer+=1
            return (max(alturaDer,alturaIzq))
    def hoja (self,nodo,valor):
        if self.vacio():
            print("arbol vacio")
        elif nodo is None:
            print("no existe el nodo")
        elif nodo.getValor() == valor:
            return(nodo.getDer() is None and nodo.getIzq() is None)
        elif valor < nodo.getValor():
            return self.hoja(nodo.getIzq(),valor)
        else:
            return self.hoja(nodo.getDer(),valor)        
    
                
if __name__ == "__main__":
    arbol = ABB()
    arbol.insertar(10, arbol.getRaiz())
    arbol.insertar(5, arbol.getRaiz())
    arbol.insertar(8, arbol.getRaiz())
    arbol.insertar(4, arbol.getRaiz())
    arbol.insertar(15, arbol.getRaiz())
    arbol.insertar(7, arbol.getRaiz())
    arbol.insertar(12, arbol.getRaiz())
    arbol.insertarIterativo(6)
    arbol.inorden(arbol.getRaiz())
    print()
    arbol.preorden(arbol.getRaiz())
    print()
    arbol.postorden(arbol.getRaiz())
    if arbol.hijo(arbol.getRaiz(), 4,5):
        print("\nEl nodo 5 es padre del nodo 4")
    else:
        print("\nLos nodos ingresados no son descendientes directos")
     
    arbol.buscar(arbol.getRaiz(),33)
    if arbol.buscarIterativo(7):
        print("\nSe encontro el elemento",arbol.buscarIterativo(7))
    else: print("\nNo se encontro el elemento")  
    print("\nNivel iterativo:")
    print("\nEl nivel del nodo 10 es:",arbol.nivel(10))
    print("\nEl nivel del nodo 5 es:",arbol.nivel(5))
    print("\nEl nivel del nodo 8 es:",arbol.nivel(8))
    print("\nEl nivel del nodo 4 es:",arbol.nivel(4))
    print("\nEl nivel del nodo 15 es:",arbol.nivel(15))
    print("\nEl nivel del nodo 7 es:",arbol.nivel(7))
    print("\nEl nivel del nodo 12 es:",arbol.nivel(12))
    print("\nNiverlRecursivo")
    arbol.nivelRecursivo(arbol.getRaiz(),10)
    arbol.nivelRecursivo(arbol.getRaiz(),5)
    arbol.nivelRecursivo(arbol.getRaiz(),8)
    arbol.nivelRecursivo(arbol.getRaiz(),4)
    arbol.nivelRecursivo(arbol.getRaiz(),15)
    arbol.nivelRecursivo(arbol.getRaiz(),7)
    arbol.nivelRecursivo(arbol.getRaiz(),12)
    print("\nLa altura del arbol es:",arbol.altura(arbol.getRaiz()))
    print("\nla altura del arbolrecursivo es:", arbol.alturaIterativo())
    if arbol.hoja(arbol.getRaiz(),7):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja(arbol.getRaiz(),4):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja(arbol.getRaiz(),15):
        print("\nEs hoja")
    else: print("\nNo es hoja")

    
    