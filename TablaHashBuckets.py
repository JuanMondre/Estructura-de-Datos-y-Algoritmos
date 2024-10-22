import numpy as np
import random
"""
Este código implementa una tabla hash que utiliza la técnica de buckets para el manejo de colisiones. 
Cada bucket tiene una capacidad limitada, y cuando se llena, los elementos desbordados se almacenan en una región separada (área de overflow).
"""
class tablaHashBuckets:
    __lista: np.ndarray                     #Arreglo bidimensional que actúa como tabla hash. Cada fila representa un bucket, y cada columna representa un espacio dentro de ese bucket.
    __capBuckets:int                        #Define la capacidad máxima de cada bucket, es decir, cuántas claves puede almacenar un bucket antes de que ocurra un desbordamiento
    __tamaño: int                           #Tamaño total de la tabla hash, que se calcula en función de la cantidad de claves y la capacidad de los buckets.
    __contadores: list                      #Arreglo que mantiene el número de claves almacenadas en cada bucket (nos ayuda a saber cuántas posiciones en cada bucket están ocupadas.)
    
    def __init__(self ,claves = 1000, capBuckets=4):
        self.__capBuckets = capBuckets
        self.__tamaño = int(claves/capBuckets + (claves / capBuckets )* 0.2)
        self.__lista = np.zeros((300,4))
        self.__contadores = np.zeros(self.__tamaño,dtype=int)
        self.__dirOverflow = int(claves/capBuckets)              #Índice que marca el inicio de la región de overflow, es decir, la parte de la tabla donde se almacenan los elementos que no caben en sus buckets originales.
        
    def extraccion(self,clave):                                  #Retorna los últimos dos dígitos de la clave para determinar la dirección en la tabla hash (bucket) donde se insertará.
        return int(clave[-2:])

    def insertar(self,clave):
        """
        Paso 1: Se calcula la dirección (bucket) utilizando el método extraccion.
        Paso 2: Si el bucket en la posición direccion no está lleno (es decir, si __contadores[direccion] es menor que la capacidad del bucket), la clave se inserta en la posición correspondiente dentro del bucket.
        Paso 3: Si el bucket está lleno, la clave se inserta en la región de overflow, que empieza en __dirOverflow. Se busca un bucket en overflow con espacio disponible, y se inserta la clave en esa posición.
        """
        direccion = self.extraccion(clave)
        if self.__contadores[direccion] < self.__capBuckets:
            self.__lista[direccion][self.__contadores[direccion]]= clave
            print(self.__lista[direccion][self.__contadores[direccion]])

            self.__contadores[direccion] += 1
            print(f"Insertó en la direccion {direccion} la clave {clave}")
            self.buscar(clave)                                   #Se llama al método buscar para verificar que la clave ha sido insertada correctamente.
        else:
            aux = self.__dirOverflow
            while self.__contadores[aux] >= self.__capBuckets and aux < self.__tamaño-1:
                aux+=1
            if aux < self.__tamaño-1:
                self.__lista[aux][self.__contadores[aux]] = clave
                self.__contadores[aux] += 1
                print(f"Insertó en la direccion {aux} la clave {clave} en overflow")
                
    def buscar(self,clave):
        cont = 0
        direccion = self.extraccion(clave)
        i = 0
        while i < self.__capBuckets:
            if self.__lista[direccion][i]== float(clave):
                print(f"Se encontró  {clave} en {cont} comparaciones\n")
                i = 4 #es una manera de romper el bucle.
            else:
                cont+=1
                i+=1
            
    def contDesbordados(self):
        cont = 0
        i = 0
        while i < self.__tamaño:
            if self.__contadores[i] == self.__capBuckets:
                cont+=1
            i+=1
        print(f"Cantidad de buckets desbordados de los 300: {cont}\n")
        
    def contSubocupados(self):
        cont = 0
        i = 0
        while i < self.__tamaño:
            if self.__contadores[i] <  int(self.__capBuckets/3):
                cont+=1
            i+=1
        print(f"Cantidad de buckets subocupados de los 300: {cont}\n")
                
    def contOverflows(self):
        cont = 0
        aux = self.__dirOverflow
        while aux < self.__tamaño:
            if self.__contadores[aux] == self.__capBuckets:
                cont+=1
            aux+=1
        print(f"cantidad de claves en overflow:{cont}\n")
        
    def contOtros(self):
        cont = 0
        for bucket in self.__lista:
            if np.count_nonzero(bucket) >int(self.__capBuckets/3) and np.count_nonzero(bucket) != self.__capBuckets:
                cont+=1
        print(f"Cantidad de buckets que no entran en los subocupados o desbordados: {cont}\n")
        
if __name__ == '__main__':
    tabla = tablaHashBuckets()
    for _ in range(0,1000):
        clave = str(random.randint(46000000,46999999))
        aux = clave
        tabla.insertar(clave)    
    tabla.contDesbordados()
    tabla.contSubocupados()
    tabla.contOverflows()
    tabla.contOtros()