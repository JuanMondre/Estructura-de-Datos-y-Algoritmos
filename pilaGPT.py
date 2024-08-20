import numpy as np

class Pila:
    def __init__(self, __cant=0):
        """
        Constructor de la clase Pila.
        Inicializa la capacidad de la pila, el índice del tope, y un arreglo de numpy para almacenar los elementos.
        """
        self.__cant = __cant
        self.__tope = -1  # El __tope empieza en -1, lo que significa que la pila está vacía.
        self.__items = np.empty(0, dtype=int)  # Inicializa un arreglo vacío de numpy.

    def vacia(self):
        """
        Verifica si la pila está vacía.
        Retorna True si la pila está vacía (cuando __tope es -1), de lo contrario, False.
        """
        return self.__tope == -1

    def insertar(self, x):
        """
        Inserta un elemento en la pila.
        Incrementa el índice del __tope y agrega el valor x en el arreglo.
        Retorna el valor insertado.
        """
        if self.__tope < self.__cant - 1:  # Verifica si hay espacio en la pila.
            self.__tope += 1  # Incrementa el índice del __tope.
            if self.__tope >= len(self.__items):  # Si el __tope es mayor o igual que el tamaño actual del arreglo:
                self.__items = np.append(self.__items, x)  # Agrega el nuevo elemento al final del arreglo.
            else:
                self.__items[self.__tope] = x  # Si el espacio existe, simplemente asigna el valor.
            return x
        else:
            return 0  # Retorna 0 si la pila está llena.

    def suprimir(self):
        """
        Elimina el elemento en el __tope de la pila y lo retorna.
        Si la pila está vacía, imprime un mensaje y retorna 0.
        """
        if self.vacia():  # Verifica si la pila está vacía.
            print("Pila vacía")
            return 0
        else:
            x = self.__items[self.__tope]  # Guarda el valor en el __tope.
            self.__tope -= 1  # Decrementa el índice del __tope.
            return x  # Retorna el valor suprimido.

    def mostrar(self):
        """
        Muestra todos los elementos en la pila desde el __tope hasta la base.
        Si la pila no está vacía, imprime cada elemento.
        """
        if not self.vacia():  # Verifica si la pila no está vacía.
            for i in range(self.__tope, -1, -1):  # Recorre el arreglo desde el __tope hasta la base.
                print(self.__items[i])  # Imprime cada elemento.


# Ejemplo de uso de la clase Pila con numpy
mi_pila = Pila(5)  # Crea una pila con capacidad para 5 elementos
mi_pila.insertar(10)
mi_pila.insertar(20)
mi_pila.mostrar()  # Debería mostrar 20 y 10
print(mi_pila.suprimir())  # Debería devolver 20
mi_pila.mostrar()  # Debería mostrar solo 10