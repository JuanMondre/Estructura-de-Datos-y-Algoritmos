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
    
    def hijo1(self, nodo,hijo,padre):
        if nodo is not None:
            if padre == nodo.getValor():
                if nodo.getDer().getValor() == hijo or nodo.getIzq().getValor() == hijo:
                    return True
            elif padre < nodo.getValor():
                return self.hijo1(nodo.getIzq(),hijo,padre)
            else:
                return self.hijo1(nodo.getDer(),hijo,padre)
        
    def buscar(self,nodo,valor):
        if self.vacio():
            print("ABB VACIO")
            return False
        if nodo is None:
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

    def nivelIterativo(self,valor):
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
    
    def nivel(self, nodo,valor, nivel=1):
        if nodo is not None:
            if valor == nodo.getValor():
                return nivel
            elif valor < nodo.getValor():
                return self.nivel(nodo.getIzq(),valor,nivel+1)
            else:
                return self.nivel(nodo.getDer(),valor,nivel+1)
        else:
            print("No existe el nodo")
    

    def altura(self,nodo):
        if nodo is None:
            return 0
        else:                                                
            return max(self.altura(nodo.getDer()),self.altura(nodo.getIzq())) + 1  #Como es una funcion recursiva incremento con el +1        
    
    def altura1(self,nodo):
        if nodo is None:
            altura = 0
            return altura
        else:
            altura = max(self.altura(nodo.getDer()), self.altura(nodo.getIzq())) + 1
            return altura
        
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
        
    def hoja1 (self, nodo, valor):
        if nodo is not None:
            if valor == nodo.getValor():
                if nodo.getDer() is None and nodo.getIzq() is None:
                    return True
            elif valor < nodo.getValor():
                return self.hoja(nodo.getIzq(),valor)
            else:
                return self.hoja(nodo.getDer(),valor)
        else:
            print("No se encuentra el elemento")
            return False
        
    def cuentaDescendientes(self, nodo, valor):
        if nodo is not None:
            if nodo.getValor() == valor:
                return self.contarDescendientes(nodo)-1
            elif valor < nodo.getValor():
                return self.cuentaDescendientes(nodo.getIzq(), valor)
            else:
                return self.cuentaDescendientes(nodo.getDer(), valor)
        else: return 0

    # Función auxiliar para contar todos los nodos en un subárbol
    def contarDescendientes(self, nodo):
        if nodo is None:
            return 0
        return 1+self.contarDescendientes(nodo.getIzq()) + self.contarDescendientes(nodo.getDer())
    
    def contarDescendientes2(self, valor):
        # Primero encontramos el nodo con el valor dado
        nodoInicial = self.__buscar(self.__raiz, valor)
        if nodoInicial is None:
            return f"Error: El valor {valor} no existe en el árbol"
        
        # Llamamos a la función auxiliar que cuenta los descendientes
        return self.__contarDescendientes(nodoInicial) - 1  # Restamos 1 para no contar el nodo inicial

    def __contarDescendientes(self, nodo):
        # Caso base: si el nodo es None
        if nodo is None:
            return 0
        
        # Contamos el nodo actual (1) más todos sus descendientes
        return 1 + self.__contarDescendientes(nodo.getIzq()) + self.__contarDescendientes(nodo.getDer())

    def __buscar(self, nodo, valor):
        if nodo is None or nodo.getValor() == valor:
            return nodo
        
        if valor < nodo.getValor():
            return self.__buscar(nodo.getIzq(), valor)
        else:
            return self.__buscar(nodo.getDer(), valor)
    
    def muestraFrontera(self,nodo):
        if nodo is not None:
            self.muestraFrontera(nodo.getIzq())
            if nodo.getDer() is None and nodo.getIzq() is None:
                print(nodo.getValor(), end=" ")
            self.muestraFrontera(nodo.getDer())
    
    def grado(self,nodo,valor,grado=0):
        if nodo is not None:
            if valor == nodo.getValor():
                if nodo.getDer() is None and nodo.getIzq() is None:
                    grado = 0
                elif nodo.getDer() is not None and nodo.getIzq() is not None:
                    grado = 2
                else: grado = 1
                return grado
            if valor < nodo.getValor():
                return self.grado(nodo.getIzq(),valor,grado)
            else:
                return self.grado(nodo.getDer(),valor,grado)

if __name__ == "__main__":
    arbol = ABB()
    arbol.insertar(10, arbol.getRaiz())
    arbol.insertar(5, arbol.getRaiz())
    arbol.insertar(8, arbol.getRaiz())
    arbol.insertar(4, arbol.getRaiz())
    arbol.insertar(15, arbol.getRaiz())
    arbol.insertar(7, arbol.getRaiz())
    arbol.insertar(12, arbol.getRaiz())
    #arbol.insertarIterativo(6)
    arbol.inorden(arbol.getRaiz())
    print()
    arbol.preorden(arbol.getRaiz())
    print()
    arbol.postorden(arbol.getRaiz())
    if arbol.hijo(arbol.getRaiz(), 4,5):
        print("\nEl nodo 5 es padre del nodo 4")
    else:
        print("\nLos nodos ingresados no son descendientes directos")
    
    if arbol.hijo1(arbol.getRaiz(), 4,5):
        print("\nEl nodo 5 es padre del nodo 4")
    else:
        print("\nLos nodos ingresados no son descendientes directos")
     
    arbol.buscar(arbol.getRaiz(),33)
    if arbol.buscarIterativo(7):
        print("\nSe encontro el elemento",arbol.buscarIterativo(7))
    else: print("\nNo se encontro el elemento")  
    print("\nNivel iterativo:")
    print("\nEl nivel del nodo 10 es:",arbol.nivel(arbol.getRaiz(),10))
    print("\nEl nivel del nodo 5 es:",arbol.nivel(arbol.getRaiz(),5))
    print("\nEl nivel del nodo 8 es:",arbol.nivel(arbol.getRaiz(),(8)))
    print("\nEl nivel del nodo 4 es:",arbol.nivel(arbol.getRaiz(),4))
    print("\nEl nivel del nodo 15 es:",arbol.nivel(arbol.getRaiz(),15))
    print("\nEl nivel del nodo 7 es:",arbol.nivel(arbol.getRaiz(),7))
    print("\nEl nivel del nodo 12 es:",arbol.nivel(arbol.getRaiz(),12))
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
    print("\nLa altura del arbol 1 es:",arbol.altura1(arbol.getRaiz()))
    if arbol.hoja(arbol.getRaiz(),7):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja(arbol.getRaiz(),4):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja(arbol.getRaiz(),15):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    print()
    if arbol.hoja1(arbol.getRaiz(),7):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja1(arbol.getRaiz(),4):
        print("\nEs hoja")
    else: print("\nNo es hoja")
    if arbol.hoja1(arbol.getRaiz(),15):
        print("\nEs hoja")
    else: print("\nNo es hoja")

    print("Los descendientes de el nodo son:", arbol.cuentaDescendientes(arbol.getRaiz(),8))
    print("Los descendientes de el nodo son:", arbol.cuentaDescendientes(arbol.getRaiz(),5))
    print("Los descendientes de el nodo son:", arbol.cuentaDescendientes(arbol.getRaiz(),10))
    print("Los descendientes de el nodo son:", arbol.cuentaDescendientes(arbol.getRaiz(),12))
    print("Los descendientes de el nodo son:", arbol.cuentaDescendientes(arbol.getRaiz(),15))
    print()
    print("Los descendientes de el nodo son:", arbol.contarDescendientes2(8))
    print("Los descendientes de el nodo son:", arbol.contarDescendientes2(5))
    print("Los descendientes de el nodo son:", arbol.contarDescendientes2(10))
    print("Los descendientes de el nodo son:", arbol.contarDescendientes2(12))
    print("Los descendientes de el nodo son:", arbol.contarDescendientes2(15))
    print()
    arbol.muestraFrontera(arbol.getRaiz())
    print()
    print("El grado del nodo es 8:", arbol.grado(arbol.getRaiz(),8))
    print("El grado del nodo es 5:", arbol.grado(arbol.getRaiz(),5))
    print("El grado del nodo es 10:", arbol.grado(arbol.getRaiz(),10))
    print("El grado del nodo es 12:", arbol.grado(arbol.getRaiz(),12))
    print("El grado del nodo es 15:", arbol.grado(arbol.getRaiz(),15))