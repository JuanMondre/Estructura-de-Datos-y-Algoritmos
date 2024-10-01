import numpy as np

class Pila:
    __elem:int
    __tope:int
    __cant:int
    
    def __init__(self,cant):
        self.__cant = cant
        self.__tope= 0
        self.__elem = np.empty(cant,dtype=int)
    
    def vacia(self):
        return self.__tope == 0
    
    def insertar(self,x):
        if self.__cant == self.__tope:
            print("La pila esta llena, no se puede insertar mas")
        else:
            self.__elem[self.__tope] = x
            self.__tope +=1
        
    def mostrar(self):
        for i in range(self.__tope-1,-1,-1):
            print(self.__elem[i])
            
    def eliminar(self):
        if self.vacia():
            print("No hay nada para eliminar")
        else:
            x = self.__elem[self.__tope-1]
            self.__tope -=1
            return x

class Nodo:
    __elem:int
    __sig:object
    def __init__(self,elem):
        self.__sig = None 
        self.__elem = elem  
    def setSig(self,sig):
        self.__sig = sig
    def setElem(self,elem):
        self.__elem = elem
    def getSig(self):
        return self.__sig
    def getElem(self):
        return self.__elem        

class pilaEnlazada:
    __tope:Nodo
    __cant:int

    def __init__(self,cant=0): #En el constructor al menos siempre debo poner la cantidad 
        self.__cant = cant
        self.__tope = None
        
    def vacia(self):
        return self.__cant == 0  
    
    def insertar(self,x):
        nodo = Nodo(x)
        nodo.setSig(self.__tope) #el nuevo nodo apunta al antiguo tope
        self.__tope = nodo #el nuevo tope ahora es el nuevo nodo
        self.__cant += 1 #incremento la cantidad de elementos en la pila
        
    def eliminar(self):
        if self.vacia():
            print("No hay nada para eliminar ")
        else:
            aux = self.__tope
            x = aux.getElem()
            self.__tope = aux.getSig()
            self.__cant -=1
            return x  
        
    def mostrar(self):
        if self.vacia():
            print("No hay nada para mostrar")
        else:
            aux = self.__tope
            while aux is not None:
                print(aux.getElem()) 
                aux = aux.getSig()
                
    def mostrarCant(self):
        return self.__cant
    
class Cola:
    __elem:np.array
    __pr:int
    __ul:int
    __max_size:int
    __cant:int
    
    def __init__(self,max_size=0):
        self.__max_size = max_size
        self.__elem = np.empty(max_size, dtype=int)
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        
    def vacia(self):
        return self.__cant == 0 
    
    def insertar(self,x):
        if self.__max_size == self.__cant:
            print("La cola esta llena")
        else:
            self.__elem[self.__ul] = x
            self.__ul +=1
            self.__cant +=1

    def eliminar(self):
        if self.vacia():
            print("Nada para eliminar")
        else:
            x = self.__elem[self.__pr]
            self.__pr +=1
            self.__cant -=1
            return x
        
    def mostrar(self):
        for i in range(self.__pr, self.__ul):
            print(self.__elem[i])
    
    def mostrarCant(self):
        return self.__cant

class ColaCircular:
    __max : int
    __pr:int
    __ul: int
    __cant:int
    __items: int
    
    
    def __init__(self, max_size=0):
        self.__max = max_size  # Tamaño máximo de la cola
        self.__pr = 0  # Índice del primer elemento en la cola
        self.__ul = 0  # Índice del último elemento en la cola
        self.__cant = 0  # Cantidad actual de elementos en la cola
        self.__items = np.empty(max_size, dtype=int)  # Arreglo de NumPy para almacenar los elementos de la cola
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ul] = x  # Inserta el elemento en la posición 'ul'
            self.__ul = (self.__ul + 1) % self.__max  # Actualiza el índice del último elemento (operación circular)
            self.__cant += 1  # Incrementa la cantidad de elementos en la cola
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacía")  # Imprime un mensaje si la cola está vacía
        else:
            x = self.__items[self.__pr]  # Guarda el elemento que se va a eliminar
            self.__pr = (self.__pr + 1) % self.__max  # Actualiza el índice del primer elemento (operación circular)
            self.__cant -= 1  # Decrementa la cantidad de elementos en la cola
            return x  # Retorna el elemento eliminado
    
    def recorrer(self):
        if not self.vacia():
            i = self.__pr  # Comienza en el índice del primer elemento
            j = 0  # Contador de elementos mostrados
            while j < self.__cant:  # Recorre mientras haya elementos en la cola
                print(self.__items[i])  # Imprime el elemento en la posición actual
                i = (i + 1) % self.__max  # Avanza al siguiente índice (operación circular)
                j += 1  # Incrementa el contador de elementos mostrados


class Nodo:
    __elem:int
    __sig:object
    def __init__(self,elem):
        self.__sig = None 
        self.__elem = elem  
    def setSig(self,sig):
        self.__sig = sig
    def setElem(self,elem):
        self.__elem = elem
    def getSig(self):
        return self.__sig
    def getElem(self):
        return self.__elem  
    
class colaEnlazada:
    __pr: Nodo
    __ul: Nodo
    __cant:int
    
    def __init__(self,cant=0):
        self.__ul = None
        self.__pr = None
        self.__cant = cant
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nodo = Nodo (x)
        if self.vacia(): 
            self.__pr = nodo #si la cola esta vacia entonces el nodo creado es el prmer elemenro
            self.__ul = nodo
        else:
            self.__ul.setSig(nodo) #si no esta vacia entonces el siguiente del ultimo apunta al nuevo nodo y el ultimo ahora es el nuevo nodo
            self.__ul = nodo
        self.__cant+=1
    
    def eliminar(self):
        if self.vacia():
            print("No hay nada para eliminar")
        else:   
            aux = self.__pr
            x = aux.getElem()
            self.__pr = aux.getSig()
            self.__cant -=1
        return x
    
    def mostrar(self):
        if self.vacia():
            print("No hay nada para mostrar")
        else:
            aux = self.__pr
            while aux is not None:
                print(aux.getElem())
                aux = aux.getSig()
                
    def mostrarCant(self):
        return self.__cant
    
def factorial(n,pila):
    if n == 0:
        return 1
    else:
        pila.insertar(n)
        print("Muestro la pila:")
        pila.mostrar()
        resultado = n * factorial(n-1,pila)
        pila.eliminar()
        print("Muestro la pila de nuevo:")
        pila.mostrar()
        return resultado
    
class listaSecuencial:
    __cap:int
    __elem:np.array
    __cant:int
    
    def __init__(self,cap):
        self.__cant = 0
        self.__elem = np.empty(cap,dtype=int)
        self.__cap = cap    
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x,pos):
        if self.__cant > self.__cap:
            print("La lista esta llena")
        if pos < 0 or pos >= self.__cap:
            print("Pos fuera de rango")
        for i in range(self.__cant, self.__cap, -1):
            self.__elem[i] = self.__elem[i-1]
        self.__elem[pos] = x
        self.__cant +=1
        
    def eliminar(self,pos):
        if self.vacia():
            print("No hay nada para eliminar")
        if pos < 0 or pos >= self.__cap:
            print("Pos fuera de rango")
        else:
            for i in range(pos, self.__cant):
                self.__elem[i] = self.__elem[i+1]
        x = self.__elem[pos]
        self.__cant-=1
        return x
    
    def mostrar(self):
        for i in range(self.__cant):
            print(self.__elem[i])
    
    def recuperar(self,pos):
        if self.vacia():
            print("No hay nada para recuperar")
        if pos < 0 or pos >= self.__cap:
            print("Pos fuera de rango")
        else:
            return self.__elem[pos]
        
    def buscar(self,x):
        i=0
        try:
            while not self.vacia():
                if self.__elem[i]==x:
                    return i
                else:
                    i+=1
        except IndexError:
            print("No se encontro")
            
    def primero(self):
        return self.__elem[0]
    def ultimo(self):
        return self.__elem[self.__cant-1]
    def anterior(self,pos):
        return self.__elem[pos-1]
    def posterior(self,pos):
        return self.__elem[pos+1]

class Nodo():
    __elem:int
    __sig:object
    def __init__(self,elem):
        self.__sig = None 
        self.__elem = elem  
    def setSig(self,sig):
        self.__sig = sig
    def setElem(self,elem):
        self.__elem = elem
    def getSig(self):
        return self.__sig
    def getElem(self):
        return self.__elem 
    
class listaEnlazada():
    __cabeza:Nodo
    __cant:int
    
    def __init__(self,cabeza=None,cant=0):
        self.__cabeza = cabeza
        self.__cant = cant
    
    def vacia(self):
        return self.__cant == 0        

    def insertar(self,x,pos):
        if pos < 0 or pos > self.__cant: 
            raise IndexError("Pos fuera de rango")
        nuevoNodo = Nodo(x)    
        if pos ==0:
            nuevoNodo.setSig(self.__cabeza)
            self.__cabeza = nuevoNodo
        else:
            aux = self.__cabeza
            for _ in range(pos -1):
                aux = aux.getSig()
            nuevoNodo.setSig(aux.getSig())
            aux.setSig(nuevoNodo)
        self.__cant +=1
        
    def eliminar(self,pos):
        if pos< 0 or pos>=self.__cant:
            print("Pos fuera de rango")  
        if self.vacia():
            print("no hay nada para eliminar")
        else:
            if pos == 0:
                aux = self.__cabeza
                self.__cabeza = aux.getSig()
                return aux
            else:
                aux = self.__cabeza
                for _ in range(pos -1):
                    aux = aux.getSig()
                x = aux.getElem()
                aux.setSig(aux.getSig().getSig())
        self.__cant-=1
        return x
    
    def recuperar(self,pos):
        if pos< 0 or pos>=self.__cant:
            print("Pos fuera de rango")  
        if self.vacia():
            print("no hay nada para recuperar")
        else:
            aux = self.__cabeza
            for _ in range(pos):
                aux = aux.getSig()
        return aux.getElem()
    
    def buscar(self,x):
        pos = 0
        if self.vacia():
            print("no hay nada para buscar")
        else:
            aux = self.__cabeza
            try:
                while aux is not None:
                    if aux.getElem() == x:
                        return pos
                    else:
                        aux = aux.getSig()
                        pos+=1
            except IndexError:
                print("No se encontro")
            
    def primero(self):
        if self.vacia():
            print("La lista esta vacia")
        else:
            return self.__cabeza.getElem()
    
    def ultimo(self):
        if self.vacia():
            print("no hay nada para recuperar")
        else:
            aux = self.__cabeza
            while aux.getSig() is not None:
                aux = aux.getSig()
            return aux.getElem()
    
    def anterior(self,pos):
        if pos< 0 or pos>=self.__cant:
            print("Pos fuera de rango")  
        if self.vacia():
            print("no hay nada para recuperar")
        aux = self.__cabeza
        for _ in range(pos -1):
            aux = aux.getSig()
        return aux.getElem()
    
    def siguiente(self,pos):
        if pos< 0 or pos>=self.__cant:
            print("Pos fuera de rango")  
        if self.vacia():
            print("no hay nada para recuperar")
        aux = self.__cabeza
        for _ in range (pos):
            aux = aux.getSig()
        return aux.getSig().getElem()
    
    def mostrar(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.getElem())
            aux=aux.getSig()
            
class listaSecuencialOrdenada:
    __elem:np.array
    __tamaño:int
    __cap:int
    
    def __init__(self,cap=0):
        self.__cap = cap
        self.__tamaño = 0
        self.__elem = np.empty(cap,dtype=int)
    
    def vacia(self):
        return self.__tamaño == 0    
    
    def insertar(self,x):
        if self.__tamaño == self.__cap:
            print("La lista esta llena")
        pos = 0
        while pos < self.__tamaño and self.__elem[pos] < x:
            pos+=1
        for i in range(self.__tamaño,pos,-1):
            self.__elem[i] = self.__elem[i-1]
        
        self.__elem[pos] = x
        self.__tamaño += 1
    
    def eliminar(self,pos):
        if  self.vacia():
            print("No hay nada para eliminar")
        if 0 <= pos < self.__tamaño:
            for i in range(pos,self.__tamaño -1):
                self.__elem[i]= self.__elem[i+1]
            x = self.__elem[pos]
            self.__tamaño-=1
        return x
    
    def recuperar(self,pos):
        if self.vacia():
            print("No hay nada por recuperar:")
        if pos < 0 or pos > self.__tamaño:
            print("pos fuera de rango")
        else:
            return self.__elem[pos]
    
    def buscar(self,x):
        i=0
        if not self.vacia():    
            while i< self.__tamaño:
                if self.__elem[i]== x:
                    return self.__elem[i]
                else:
                    i+=1 
        else:
            print("No hay nada por buscar")

    def primer(self):
        if not self.vacia():
            return self.__elem[0]
        else:
            print("La lista esta vacia")
    def ultimo(self):
        if not self.vacia():
            return self.__elem[self.__tamaño-1]
        
    def anterior(self,pos):
        if pos < 0 or pos > self.__tamaño:
            print("pos fuera de rango")
        if self.vacia():
            print("Lista vacia") 
        return self.__elem[pos-1]
    
    def siguiente(self,pos):
        if pos < 0 or pos > self.__tamaño:
            print("pos fuera de rango")
        if self.vacia():
            print("Lista vacia") 
        return self.__elem[pos+1]
        
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tamaño):
                print(self.__elem[i])

class Nodo:
    __elem:int
    __sig:object
    def __init__(self,elem):
        self.__elem = elem
        self.__sig = None     
    def getElem(self):
        return self.__elem
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
           
class listaEnlazadaOrdenada:
    __cabeza:Nodo
    __cant:int
    
    def __init__(self,cant=0):
        self.__cabeza = None 
        self.__cant = cant

    def vacia(self):
        return self.__cant == 0
        
    def insertar(self,x):
        nuevoNodo = Nodo(x)
        if self.__cabeza is None or self.__cabeza.getElem()>= x:
            nuevoNodo.setSig(self.__cabeza)
            self.__cabeza=nuevoNodo
        else:
            aux=self.__cabeza
            while aux.getSig() and aux.getSig().getElem()<x:
                aux = aux.getSig()
            
            nuevoNodo.setSig(aux.getSig())
            aux.setSig(nuevoNodo)
        self.__cant+=1
        
    def eliminar(self, x):
        if self.vacia():
            print("Nada para eliminar")
            return None  # Retornamos None si la lista está vacía

        # Caso en que el elemento a eliminar está en la cabeza
        if self.__cabeza.getElem() == x:
            nodoEliminado = self.__cabeza
            self.__cabeza = self.__cabeza.getSig()
            self.__cant -= 1
            return nodoEliminado.getElem()

        # Buscar el nodo anterior al que queremos eliminar
        aux = self.__cabeza
        while aux.getSig() and aux.getSig().getElem() != x:
            aux = aux.getSig()

        # Verificar si el elemento fue encontrado
        if aux.getSig() is None:
            print(f"Error: El elemento {x} no se encontró en la lista.")
            return None  # Retornamos None si el elemento no se encuentra

        # Eliminar el nodo
        nodoEliminado = aux.getSig()
        aux.setSig(nodoEliminado.getSig())
        self.__cant -= 1
        return nodoEliminado.getElem()
    
    def recuperar(self,pos):
        if self.vacia():
            print("No hay nada por recuperar")
        aux = self.__cabeza
        for i in range(pos):
            aux = aux.getSig()    
        return aux.getElem()
    
    def buscar(self,x):
        if self.vacia():
            print("no hay nada por buscar")
        else:
            i=0
            aux = self.__cabeza
            while aux is not None:
                if aux.getElem()!= x:
                    aux = aux.getSig()
                    i+=1
                else:
                    return aux.getElem()    

    def anterior(self,pos):
        if pos>0 and pos<self.__cant:
            return pos-1
        else:
            print("pos fuera de rango")
    
    def siguiente(self,pos):
        if pos>0 and pos<self.__cant:
            return pos+1
        else:
            print("pos fuera de rango")
    
    def primero(self):
        if self.vacia():
            print("No hay primero")
        else:
            return self.__cabeza.getElem()
    
    def ultimo(self):
        if self.vacia():
            print("no hay ultimo")
        else:
            aux = self.__cabeza
            while aux.getSig() is not None:
                aux = aux.getSig()
            
            return aux.getElem()
    
    def mostrar(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.getElem())
            aux=aux.getSig()

if __name__ == "__main__":
    
    #PILA SECUENCIAL
    """    
    pila = Pila(4)
    print(pila.vacia())
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.mostrar()
    print("Elimino 2 veces")
    pila.eliminar()
    pila.eliminar()
    pila.mostrar()
    """
    #PILA ENLAZADA
    """ 
    pila = pilaEnlazada()
    print(pila.vacia())
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.mostrar()
    print("Cantidad:")
    print(pila.mostrarCant())
    print("Elimino 2 veces")
    pila.eliminar()
    pila.eliminar()
    pila.mostrar()
    print("Cantidad:")
    print(pila.mostrarCant())
    """
    #COLA SECUENCIAL
    """
    cola = Cola(4)
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.mostrar()
    print("Cantidad:")
    print(cola.mostrarCant())
    print("Elimino 2 veces")
    cola.eliminar()
    cola.eliminar()
    cola.mostrar()
    print("Cantidad:")
    print(cola.mostrarCant())
    """
    #COLA CIRCULAR
    """
    cola = ColaCircular(5)  # Crea una cola con capacidad para 5 elementos
    cola.insertar(10)  # Inserta el elemento 10 en la cola
    cola.insertar(20)  # Inserta el elemento 20 en la cola
    cola.insertar(30)  # Inserta el elemento 30 en la cola
    cola.recorrer()  # Muestra todos los elementos en la cola
    print("Elemento suprimido:", cola.suprimir())  # Elimina y muestra el primer elemento de la cola
    cola.recorrer()  # Muestra el estado actual de la cola  
    """
    #COLA ENLAZADA
    """
    cola = colaEnlazada()
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.mostrar()
    print("Cantidad:")
    print(cola.mostrarCant())
    print("Elimino 2 veces")
    cola.eliminar()
    cola.eliminar()
    cola.mostrar()
    print("Cantidad:")
    print(cola.mostrarCant())
    """
    #BINARIO
    """    
    pila = Pila(4)
    n = 14
    while n > 2 :
        resto = n % 2
        pila.insertar(resto)
        n = n/2
        if n<2:
            pila.insertar(n)
    pila.mostrar()
    """
    #FACTORIAL   
    """    
    pila = Pila(100)
    n = 3
    resultado = factorial(n,pila)
    print(f"El factorial de {n}! = {resultado}")
    """
    #LISTA SECUENCIAL  
    """
    lista = listaSecuencial(100)
    lista.insertar(1,0)
    lista.insertar(2,1)
    lista.insertar(3,2)
    lista.insertar(4,3)
    lista.insertar(5,4)
    lista.mostrar()
    print("Elimino 2")
    #lista.eliminar(0)
    #lista.eliminar(1)
    #lista.mostrar()
    pos=2
    print(f"El elemento {lista.recuperar(pos)} se recupero de la pos {pos}")
    num=7
    print(F"Se encontro el numero {num} en la posicion {lista.buscar(num)}")
    print(lista.primero())
    print(lista.ultimo())
    print(lista.anterior(1))
    print(lista.posterior(1))
    """
    #LISTA ENLAZADA
    """ 
    lista = listaEnlazada()
    lista.insertar(1,0)
    lista.insertar(2,1)
    lista.insertar(3,2)
    lista.insertar(4,3)
    lista.insertar(5,4)
    lista.mostrar()
    #print("Elimino 2")
    #lista.eliminar(0)
    #lista.eliminar(1)
    #lista.mostrar()
    pos=2
    print(f"El elemento {lista.recuperar(pos)} se recupero de la pos {pos}")
    num=5
    if lista.buscar(num)==None:
        print("El elemento no esta")
    else:
        print(f"El elemento {num} se encontro de la pos {lista.buscar(num)}")
    print(lista.primero())
    print(lista.ultimo())
    print(lista.anterior(1))
    print(lista.siguiente(1))
    """
    #LISTA SECUENCIAL ORDENADA
    """
    lista = listaSecuencialOrdenada(100)
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(4)
    lista.insertar(5)
    lista.mostrar()
    #print("Elimino 2")
    #lista.eliminar(0)
    #lista.eliminar(1)
    #lista.mostrar()
    pos=2
    print(f"El elemento {lista.recuperar(pos)} se recupero de la pos {pos}")
    num=3
    if lista.buscar(num) == None:
        print("No se encontro")
    else:
        print(F"Se encontro el numero {num} en la posicion {lista.buscar(num-1)}")
    print(lista.primer())
    print(lista.ultimo())
    print(lista.anterior(1))
    print(lista.siguiente(1))
    """
    #LISTA ENLAZADA ORDENADA
    lista = listaEnlazadaOrdenada()
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(4)
    lista.insertar(5)
    lista.mostrar()
    #print("Elimino 2")
    #lista.eliminar(3)
    #lista.eliminar(5)
    #lista.mostrar()
    pos=2
    print(f"El elemento {lista.recuperar(pos)} se recupero de la pos {pos}")
    num=5
    if lista.buscar(num) == None:
        print("El elemento no esta")
    else:
        print(f"El elemento {num} se encontro de la pos {lista.buscar(num)-1 }")
    print(lista.primero())
    print(lista.ultimo())
    print(lista.anterior(1))
    print(lista.siguiente(1))