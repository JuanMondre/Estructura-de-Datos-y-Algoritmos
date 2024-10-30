import numpy as np
import random

class Nodo:
    __sig: object
    __clave: object

    def __init__(self, clave):
        self.__sig = None
        self.__clave = clave

    def getSig(self):
        return self.__sig

    def getClave(self):
        return self.__clave

    def setSig(self, sig):
        self.__sig = sig


class TablaHashEncadenada:
    # En lugar de almacenar un solo elemento en cada índice de la tabla, se utiliza una lista enlazada para almacenar múltiples elementos que comparten la misma dirección (índice de la tabla hash).
    __lista: np.ndarray  # Lista que lleva un registro del número de colisiones en cada posición de la tabla.
    __tamaño: int        # El tamaño de la tabla hash, determinado por la fórmula N/M, donde N: número aproximado de elementos a almacenar, M: factor de carga.
    __colisiones: list   # Almacena los nodos en cada posición de la tabla hash.

    def __init__(self, N=100, M=5):
        self.__tamaño = int(N / M)
        self.__colisiones = np.zeros(self.__tamaño, dtype=int)
        self.__lista = np.ndarray(self.__tamaño, dtype=object)

    def plegado(self, clave):
        """
        Esta función de transformación utiliza el método de plegado: divide la clave en grupos de dos dígitos, los suma, y luego calcula el módulo (%) con el tamaño de la tabla hash para obtener la dirección donde se almacenará la clave.
        """
        clave_str = str(clave)
        suma = 0
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        return suma % self.__tamaño
    

    def insertar(self, clave):
        """
        Se obtiene la dirección de la clave mediante la función plegado.
        Si la posición en __lista[direccion] está vacía, la clave se inserta directamente.
        Si no está vacía (hay colisión), se recorre la lista enlazada hasta el final:
        Si no se encuentra la clave, se añade al final de la lista y se incrementa el contador de colisiones.
        Si la clave ya está en la lista, se indica que ya fue ingresada.
        """
        direccion = self.plegado(clave)
        nodo = Nodo(clave)
        if self.__lista[direccion] is None:
            nodo.setSig(None)
            self.__lista[direccion] = nodo
            print(f"Se inserto la clave '{clave}'.")
        else:
            aux = self.__lista[direccion]
            while aux.getSig() is not None and aux.getClave() != clave:
                aux = aux.getSig()
            if aux.getSig() is None:
                self.__colisiones[direccion] += 1
                aux.setSig(nodo)
                print(f"Se inserto la clave '{clave}', hay {self.__colisiones[direccion]} claves colisionadas.")
            else:
                print("Clave ya ingresada.")

    def buscar(self, clave):
        """
        Primero, se obtiene la dirección de la clave.
        Si en esa dirección no hay nodos, se indica un error.
        Si hay nodos, se recorre la lista enlazada buscando la clave. Si se encuentra, se indica cuántos intentos tomó.
        """
        direccion = self.plegado(clave)
        cont = 1
        if self.__lista[direccion] is not None:
            aux = self.__lista[direccion]
            while aux.getSig() is not None and aux.getClave() != clave:
                aux = aux.getSig()
                cont += 1
            if aux.getClave() == clave:
                print(f"Se ha encontrado la clave '{aux.getClave()}', en {cont} intentos.")
            else:
                print("Elemento no encontrado.")
        else:
            print("Error.")

    def promColisiones(self):
        suma = 0
        for i in range(len(self.__colisiones)):
            suma += self.__colisiones[i]
        promedio = suma / self.__tamaño
        return promedio


if __name__ == '__main__':
    tabla = TablaHashEncadenada()
    tabla.insertar('45635882')
    tabla.insertar('45635883')

    claves = []
    for _ in range(100):
        claves.append(random.randint(45000000, 45999999))

    cont = 0
    for clave in claves:
        tabla.insertar(clave)
        cont += 1
    print(f"\nSe ingresaron {cont} claves")

    tabla.insertar('45635882')
    tabla.buscar('45635882')
    print(f"Promedio: {tabla.promColisiones()}")
