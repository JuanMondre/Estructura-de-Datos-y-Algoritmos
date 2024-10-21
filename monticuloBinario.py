import numpy as np

class MonticuloBinario:
    __elem : np.array
    __cantidad :int
    __cap:int
    
    def __init__(self,cap):
        self.__elem = np.zeros(cap, dtype=int)                                  #Arreglo con la cantidad de elementos del monticulo
        self.__cantidad = 0                                                     #Cantidad del monticulo, siempre en 0 xq se modifica cada vez que inserto
        self.__cap = cap                                                        #Capacidad del monticulo, lo configuro desde la llamada a la instancia
    
    def getPadre(self,i):
        return(i-1)//2                                                          #Retorna el padre de un nodo 
    
    def getHijoIzq(self,i):
        return 2*i+1                                                            #Retorna el hijo izquierdo de un nodo 
    
    def getHijoDer(self,i):
        return 2*i+2                                                            #Retorna el hijo derecho de un nodo 
    
    def intercambiar(self,pos1,pos2):                                           #Funcion que me permite intercambiar las posiciones del arreglo en caso que lo necesite
        aux = self.__elem[pos1]
        self.__elem[pos1] = self.__elem[pos2]
        self.__elem[pos2] = aux
    
    def vacio(self):
        return self.__cantidad == 0
        
    def insertar(self, x):
        if self.__cantidad >= self.__cap:                                       #Si la cantidad de nodos es menor que la capacidad del monticulo(arreglo) entonces puedo insertar
            print("\nError monticulo lleno")
        else:
            self.__elem[self.__cantidad] = x                                    #Guardo el nodo x en la ultima posicion del monticulo(arreglo)
            self.__cantidad+=1                                                  #Incremento el contador de la cantidad de nodos
            flag = True                                                         #Declaro la bandera que me va a ir controlando el bucle
            i = self.__cantidad-1                                               #Creo un indice acutal y lo obtengo guardando la cantidad de nodos en el monticulo menos uno
            #REORDENAMINETO DEL MONTICULO
            while i > 0 and flag:                                               #Si mi indice es mas grande que cero y la vandera es true entonces obtengo el padre
                indicePadre = self.getPadre(i)
                if self.__elem[i] < self.__elem[indicePadre]:                   #Si el valor del nodo padre es mas grande que del nodo hijo entonces intercambio valores
                    self.intercambiar(i,indicePadre)
                    i = indicePadre                                             #Actualizo el indice para iterar en el bucle y seguir intercambiando valores en caso de ser necesario
                else:
                    flag=False
    
    def eliminarMinimo(self):
        if self.vacio():                                                        #Si el monticulo esta vacio no puedo eliminar nada
            print("\nNo hay nada por eliminar:")
        else:
            minimo = self.__elem[0]                                             #Guardo en una variable el primer elemento del arreglo, que es la raiz(es el nodo con la menor clave, es decir mayor prioridad)
            self.__elem[0] = self.__elem[self.__cantidad-1]                     #Remplazo la raiz del arbol, por la ultima clave ingresada en el arbol
            self.__cantidad -=1                                                 #Decremento la cantidad
            i = 0                                                               #Declaro un indice
            flag = True
            #REORDENAMIENTO DEL MONTICULO
            while flag: 
                hijoIzq = self.getHijoIzq(i)                                    #Obtengo el hijo izq del nodo que se encuentra en mi indice i 
                hijoDer = self.getHijoDer(i)                                    #Obtengo el hijo der del nodo que se encuentra en mi indice i 
                indiceMenor= i                                                  #Declaro unav ariable que se llama indice menor y la igualo a mi indice
                if hijoIzq < self.__cantidad and self.__elem[hijoIzq] < self.__elem[indiceMenor]:
                    indiceMenor = hijoIzq                                       #Si el hijo izquierdo existe y es menor que el elemento actual, se actualiza
                if hijoDer < self.__cantidad and self.__elem[hijoDer] < self.__elem[indiceMenor]:
                    indiceMenor = hijoDer                                       #Si el hijo derecho existe y es menor que el elemento más pequeño encontrado hasta ahora, se actualiza indiceMenor
                    
                if indiceMenor != i:                                            #Si indiceMenor ha cambiado, significa que se encontró un hijo menor.
                    self.intercambiar(i,indiceMenor)                            #Se intercambia el elemento actual con el hijo menor.
                    i = indiceMenor                                             #Se actualiza i para continuar el proceso de hundimiento.
                else: 
                    flag = False                                                #Si no hubo cambio, el elemento está en su posición correcta y se termina el bucle.
            return minimo
    
    def imprimir(self):
        print(self.__elem[:self.__cantidad])
        
    def obtenerMinimo(self):
        if self.vacio():
            print("Error: El montículo está vacío")
            return None
        return self.__elem[0]
    
if __name__ == "__main__":
    
    monticulo = MonticuloBinario(10)

    print("Insertar elementos")
    elementos = [5, 3, 7, 1, 4, 6, 2, 9]
    for elemento in elementos:
        monticulo.insertar(elemento)
        print(f"Insertado {elemento}. Montículo actual:", end=" ")
        monticulo.imprimir()

    print("\nObtener mínimo")
    print("Mínimo actual:", monticulo.obtenerMinimo())

    print("\nEliminar mínimo")
    for _ in range(len(elementos)):
        minimo = monticulo.eliminarMinimo()
        print(f"Eliminado {minimo}. Montículo actual:", end=" ")
        monticulo.imprimir()

    print("\nIntentar eliminar de un montículo vacío")
    monticulo.eliminarMinimo()

    print("\nInsertar más elementos que la capacidad")
    for i in range(12):
        monticulo.insertar(i)