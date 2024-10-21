class Nodo:
    __valor:int                                 #Almacena el valor de la variable o el dato a guardar
    __izquierda: 'Nodo'                         #Referencia al arbol izquierdo
    __derecha: 'Nodo'                           #Referencia al arbol derecho
    __padre: 'Nodo'                             #Referencia al padre del nodo
    #CONSTRUCTOR
    def __init__(self, valor):
        self.__valor = valor
        self.__izquierda = None                 #Deben apuntar a None xq todavia la parte izq del arbol esta vacio
        self.__derecha = None                   #Deben apuntar a None xq todavia la parte der del arbol esta vacio
        self.__padre = None 
        
    def getValor(self):
        return self.__valor                     #Retorna el valor del dato guardado
        
    def getIzquierda(self):
        return self.__izquierda                 #Retorna la referencia al arbol izquierdo
    
    def getDerecha(self):
        return self.__derecha                   #Retorna la referencia al arbol derecho
    
    def setValor(self,valor):
        self.__valor = valor                    #Setea el valor del dato guardado
        
    def setIzquierda(self, nodo):
        self.__izquierda = nodo                 #Setea la referencia del arbol izquierdo
        
    def setDerecha(self, nodo):
        self.__derecha = nodo                   #Setea la referencia del arbol derecho
    
    def getPadre(self):
        return self.__padre                     #Retorna el padre del nodo
        
class ArbolBinarioBusqueda:
    __raiz : Nodo
    
    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz                      #Retorna la raiz actual
    
    def setRaiz(self,raiz):
        self.__raiz = raiz                      #Setea la raiz a la raiz actual
        
    def vacio(self):                            #Retorna verdadero si la raiz del arbol es igual a None, que significa que el arbol esta vacio
        return self.__raiz == None

    def insertarRecursivo(self,valor, nodo):
        """  
         Paso 1: 
         Verificamos si el arbol esta vacio, si eso es verdadero entonces instanciamos un nodo(que sera la raiz del arbol)
         
         Paso 2: 
         Se compara el valor a insertar con el valor del nodo actual.
         Si es menor, se mueve al subárbol izquierdo.
         Si es mayor o igual, se mueve al subárbol derecho.
         Se repite este proceso hasta encontrar una posición vacía (None).
         Cuando se encuentra una posición vacía, se crea un nuevo nodo y se inserta en esa posición.
         
        """
        if self.vacio():
            self.__raiz = Nodo(valor)           
            
        elif valor < nodo.getValor():                        
            if nodo.getIzquierda() is None:                  
                nodo.setIzquierda((Nodo(valor)))
            else:
                self.insertarRecursivo(valor, nodo.getIzquierda())
    
        elif valor > nodo.getValor(): 
            if nodo.getDerecha() is None:
                nodo.setDerecha((Nodo (valor)))
            else:
                self.insertarRecursivo(valor, nodo.getDerecha())
        else:
            print("Erorr el Valor ya se encuentra en el arbol")
            
    def insertar(self,valor):
        """
        Creamos un nuevo nodo con el valor a insertar.
        Verificamos si el árbol está vacío (si la raíz es None). Si lo está, el nuevo nodo se convierte en la raíz y terminamos.
        Si el árbol no está vacío, iniciamos un bucle while que continuará hasta que encontremos la posición correcta para insertar el nuevo nodo.
        En cada iteración del bucle:

            Comparamos el valor a insertar con el valor del nodo actual.
            Si el valor es menor que el del nodo actual:

                Verificamos si el hijo izquierdo es None.
                Si lo es, insertamos el nuevo nodo como hijo izquierdo y terminamos.
                Si no, movemos el nodo actual al hijo izquierdo y continuamos el bucle.

            Si el valor es mayor o igual que el del nodo actual:

                Verificamos si el hijo derecho es None.
                Si lo es, insertamos el nuevo nodo como hijo derecho y terminamos.
                Si no, movemos el nodo actual al hijo derecho y continuamos el bucle.
                
        def insertar(self,dato):
            nuevoNodo = Nodo(valor)
            if self.__raiz == None:
                self.__raiz = nuevoNodo
                return
            nodo = self.__raiz
            while True:
                if valor < nodo.getValor():
                    if nodo.getIzquierda() is None:
                        nodo.setIzquierda(nuevoNodo)
                        return
                    nodo = nodo.getIzquierda()
                else:
                    if nodo.getDerecha() is None:
                        nodo.setDerecha(nuevoNodo)
                        return
                    nodo = nodo.getDerecha()
            
        """
    
    def getMinimoIterativo(self, nodo):                                                      #Metodo que busca el valor minimo del ABB (nodo mas a la izquierda)
        while nodo.getIzquierda() is not None:                                               #El metodo es sencillo, mientras haya nodo o hijo hizquierdo avanza hacia el
            nodo = nodo.getIzquierda()                                                       #Cuando no puede avanzar mas ese nodo es el minimo 
        return nodo                                                                          #Retornar el nodo en lugar del valor
    
    def getMinimo(self,nodo):                                                                #Realiza lo mismo que el metodo anterior
        if self.__raiz is None:                                                              #Si la raiz no existe entonces retorna null
            return None                                                                            
        elif nodo.getIzquierda() is None:
            return nodo
        else:
            return self.getMinimo(nodo.getIzquierda())
    
    def getMaximo(slef,nodo):
        while nodo.getDerecha()is not None:
            nodo = nodo.getDerecha()
        return nodo
    
    def getMaximo(self, nodo):
        if self.__raiz is None:
            return None
        elif nodo.getDerecha() is None:
            return nodo
        else:
            return self.getMaximo(nodo.getDerecha())
    
    def eliminar(self, nodo, valor):
        """
            Verificación del árbol vacío:
                Primero, el método verifica si el árbol está vacío mediante self.vacio(). Si el árbol está vacío, imprime un mensaje y no realiza ninguna operación adicional.

            Recursión hacia el subárbol izquierdo o derecho:
                Aquí el método compara el valor que se desea eliminar con el valor del nodo actual:
                    Si valor es menor que el valor del nodo actual, el método recurre hacia el subárbol izquierdo (nodo.getIzquierda()), buscando el valor en ese subárbol.
                    Si valor es mayor, recurre al subárbol derecho (nodo.getDerecha()) en busca del valor en el lado derecho.
                    Esta recursión continúa hasta encontrar el nodo que contiene el valor que queremos eliminar.

            Nodo encontrado (valor coincidente):
            Caso 1: El nodo es una hoja (no tiene hijos):
                Si el nodo no tiene hijos (ambos subárboles izquierdo y derecho son None), simplemente se devuelve None, lo que efectivamente elimina el nodo de su posición en el árbol.

            Caso 2: El nodo tiene un solo hijo:
                Si el nodo solo tiene un hijo (izquierdo o derecho), el método devuelve ese hijo, reemplazando el nodo actual en su posición en el árbol.

            Caso 3: El nodo tiene dos hijos:
                En este caso, se necesita reemplazar el nodo con su sucesor en orden (el menor valor del subárbol derecho). Esto se hace en tres pasos:
                    Se encuentra el sucesor llamando a self.getMinimo(nodo.getDerecha()), que devuelve el nodo con el menor valor en el subárbol derecho.
                    Se actualiza el valor del nodo actual con el valor del sucesor (nodo.setValor(sucesor.getValor())).
                    Finalmente, se elimina el sucesor del subárbol derecho mediante una llamada recursiva a self.eliminar para evitar duplicados.
            
            Devolución del nodo actualizado:
                Después de actualizar el nodo (o eliminarlo si es un nodo hoja), el método devuelve el nodo actualizado para que la estructura del árbol permanezca consistente. Esto permite que el árbol se actualice correctamente en todos los niveles de recursión.

            Este método garantiza que el árbol permanezca ordenado tras la eliminación del nodo y que el BST conserve sus propiedades tras la operación.
        """
        
        if self.vacio():
            print("El arbol esta vacio")                                                                    
        
        if valor < nodo.getValor():                                                           #Si el valor a eliminar es menor que el valor del nodo actual(valor de la raiz),
            nodo.setIzquierda(self.eliminar(nodo.getIzquierda(),valor))                       #Buscar en el subárbol izquierdo
                
        elif valor > nodo.getValor():                                                         #Si el valor a eliminar es mayor que el valor del nodo actual,
            nodo.setDerecha(self.eliminar(nodo.getDerecha(),valor))                           #Buscar en el subárbol derecho
                                                                                                    
        else:                                                                                 #Si el valor es igual al valor del nodo actual, este es el nodo a eliminar
            
            if nodo.getIzquierda() is None and nodo.getDerecha() is None:                     #Caso 1: Nodo hoja, no tiene hijos.
                return None
            
            if nodo.getIzquierda() is None:                                                   #Caso 2: Nodo con 1 hijo
                return nodo.getDerecha()
            if nodo.getDerecha() is None:
                return nodo.getIzquierda()
                                                                                              #Caso 3: Nodo con 2 hijos
            sucesor = self.getMinimo(nodo.getDerecha())                                       #Encontrar el sucesor (el menor valor en el subárbol derecho)
            nodo.setValor(sucesor.getValor())                                                 #Copiar el valor del sucesor al nodo actual
            nodo.setDerecha(self.eliminar(nodo.getDerecha(), sucesor.getValor()))             #Eliminar el sucesor del subárbol derecho
    
        return nodo
        
    def eliminar_valor(self, valor):                                                          #Método auxiliar para iniciar la eliminación desde la raíz
        self.__raiz = self.eliminar(self.__raiz, valor)
                
    
    def buscarIterativo(self,valor):
        actual = self.__raiz
        while actual is not None:
            if actual.getValor() == valor:
                print("Se encontro el elemento")
                return True  #Es legal?
            elif actual.getValor() > valor:
                actual = actual.getIzquierda()
            else:
                actual = actual.getDerecha()
        return False
    
    def buscarRecursivo(self,nodo,valor):                                                     
        if nodo is None:
            print("No se encontro el elemento")
            return False
        if valor == nodo.getValor():
            print("Se encontro el elemento")
            return nodo.getValor()
        elif valor < nodo.getValor():                                                         #Si el valor es mas chico que la raiz
            return self.buscarRecursivo(nodo.getIzquierda(),valor)                            #Busco por la izquierda
        else:
            return self.buscarRecursivo(nodo.getDerecha(),valor)                              #Si el valor es mas grandwe que la raiz busco por la derecha
        
       
    def nivel(self,nodo, valor, nivel=0):
        if self.vacio():
            print("El arbol esta vacio")
        elif nodo is None:
            print("No se encuentra el elemento")
        elif nodo.getValor() == valor:
            print(F"Nivel de {valor} es: {nivel}")
        elif nodo.getValor()> valor:
            self.nivel(nodo.getIzquierda(),valor,nivel+1)
        else:
            self.nivel(nodo.getDerecha(),valor,nivel+1)
    
    """
    def nivel(self,nodo, valor, nivel=0):
        if self.vacio():
            print("El arbol esta vacio")
            return false
        elif nodo is None:
            print("No se encuentra el elemento")
            return false
        elif nodo.getValor() == valor:
            print(F"Nivel de {valor} es: {nivel}")
        elif nodo.getValor()> valor:
             return self.nivel(nodo.getIzquierda(),valor,nivel+1)
        else:
            return self.nivel(nodo.getDerecha(),valor,nivel+1)
    """
    
    def hoja(self,nodo,valor):
        if self.vacio():
            print("El arbol esta vacio")
            return False
        elif nodo is None:
            print("No se encuentra el elemento")
            return False
        elif nodo.getValor() == valor:
            return nodo.getIzquierda() is None and nodo.getDerecha() is None
        elif valor < nodo.getValor() :
            return self.hoja(nodo.getIzquierda(),valor)
        else:
            return self.hoja(nodo.getDerecha(),valor)
            
    def hijo(self, nodo, hijo, padre):
        if self.vacio():
            return False
        elif nodo is None:
            return False
        elif nodo.getValor() == padre:
            return nodo.getIzquierda().getValor() == hijo or nodo.getDerecha().getValor() == hijo
        elif nodo.getValor() > padre:
            return self.hijo(nodo.getIzquierda(),hijo,padre)
        else:
            return self.hijo(nodo.getDerecha(),hijo,padre)
        
    def altura(self,nodo):
        if nodo is None:
            return 0
        else: 
            return 1 + max(self.altura(nodo.getDerecha()), self.altura(nodo.getIzquierda()))

    def inorden(self, nodo):                                                    #Muestra los nodos en orden ascendente(del nodo mas chico al nodo mas grande)
        if  nodo is not None:
            self.inorden(nodo.getIzquierda())                                   #Recorre recurtsivamente el arbol izquierdo
            print(nodo.getValor(),end=" ")                                      #Imprime el nodo
            self.inorden(nodo.getDerecha())                                     #Recorre recursivamente el arbol derecho
            
    def preorden(self, nodo):                                                   #muestra primero la raiz del arbon, luego el hijo izquierdo y por ultimo el derecho
        if nodo is not None:
            print(nodo.getValor(), end=" ")                                     #Imprime el nodo
            self.preorden(nodo.getIzquierda())                                  #Recorre recurtsivamente el arbol izquierdo
            self.preorden(nodo.getDerecha())                                    #Recorre recursivamente el arbol derecho
        
    def postorden(self, nodo):                                                  #muestra primero los hijos izquierdo, derecho y luego la raiz
        if nodo is not None:
            self.postorden(nodo.getIzquierda())                                 #Recorre recurtsivamente el arbol izquierdo
            self.postorden(nodo.getDerecha())                                   #Recorre recursivamente el arbol derecho
            print(nodo.getValor(), end=" ")                                     #Imprime el nodo
            
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    """
    valores_a_insertar = [15, 10, 20, 8, 12, 17, 25]
    print("Insertando valores en el árbol:", valores_a_insertar)
    for valor in valores_a_insertar:
        print(f"Insertando valor {valor}")
        arbol.insertar(valor)
    """    
    arbol.insertarRecursivo(15,arbol.getRaiz())
    arbol.insertarRecursivo(10,arbol.getRaiz())
    arbol.insertarRecursivo(20,arbol.getRaiz())
    arbol.insertarRecursivo(8,arbol.getRaiz())
    arbol.insertarRecursivo(12,arbol.getRaiz())
    arbol.insertarRecursivo(17,arbol.getRaiz())
    arbol.insertarRecursivo(25,arbol.getRaiz())

    # Recorridos del árbol
    print("\nRecorrido Inorden (debe mostrar valores en orden ascendente):")
    arbol.inorden(arbol.getRaiz())
    print("\nRecorrido Preorden (raíz, izquierda, derecha):")
    arbol.preorden(arbol.getRaiz())
    print("\nRecorrido Postorden (izquierda, derecha, raíz):")
    arbol.postorden(arbol.getRaiz())
    print("\n")
    
    # Búsquedas
    #arbol.buscarIterativo(25)
    print(arbol.buscarRecursivo(arbol.getRaiz(),25))
    print("\n")
    
    # Prueba de obtener mínimo y máximo
    print("Valor mínimo en el árbol:", arbol.getMinimo(arbol.getRaiz()).getValor())
    print("Valor mínimo en el árbol:", arbol.getMaximo(arbol.getRaiz()).getValor())

    
    # Verificar la altura del árbol
    print("\nAltura del árbol:", arbol.altura(arbol.getRaiz()))
    
    # Verificar si un nodo es hijo
    if (arbol.hijo(arbol.getRaiz(),25,20)):
        print("\nLos valores ingresados son hijos")
    else: 
        print("\nLos valores ingresados no son hijos")
        
    # Verificar si un nodo es hoja
    if arbol.hoja(arbol.getRaiz(),25):
        print("\nEl nodo ingresado es hoja")
    else:
        print("\nEl nodo ingresado no es hoja")
    
    print("\n")
    # Prueba del nivel de un nodo
    arbol.nivel(arbol.getRaiz(),15,0)
    arbol.nivel(arbol.getRaiz(),10,0)
    arbol.nivel(arbol.getRaiz(),20,0)
    arbol.nivel(arbol.getRaiz(),8,0)
    arbol.nivel(arbol.getRaiz(),12,0)
    arbol.nivel(arbol.getRaiz(),17,0)
    arbol.nivel(arbol.getRaiz(),25,0)
    
    # Prueba de eliminar un valor 
    print("\nEliminando el valor 10 del árbol")
    arbol.eliminar_valor(10)
    
    # Recorrido Inorden después de eliminar
    print("\nRecorrido Inorden después de eliminar 10:")
    arbol.inorden(arbol.getRaiz())
    print("\nRecorrido Preorden después de eliminar 10:")
    arbol.preorden(arbol.getRaiz())
    print("\nRecorrido Postorden después de eliminar 10:")
    arbol.postorden(arbol.getRaiz())
    