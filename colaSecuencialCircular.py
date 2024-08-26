import numpy as np

class Cola:
    __max : int
    __pr:int
    __ul: int
    __cant:int
    __items: int
    
    
    def __init__(self, max_size=0):
        """
        Constructor de la clase Cola. Inicializa una cola vacía con un tamaño máximo dado.
        """
        self.__max = max_size  # Tamaño máximo de la cola
        self.__pr = 0  # Índice del primer elemento en la cola
        self.__ul = 0  # Índice del último elemento en la cola
        self.__cant = 0  # Cantidad actual de elementos en la cola
        self.__items = np.empty(max_size, dtype=int)  # Arreglo de NumPy para almacenar los elementos de la cola
    
    def vacia(self):
        """
        Verifica si la cola está vacía.
        Retorna True si la cola está vacía, de lo contrario retorna False.
        """
        return self.__cant == 0
    
    def insertar(self, x):
        """
        Inserta un elemento en la cola.
        Si la cola no está llena, inserta el elemento en la posición correspondiente
        y actualiza el índice del último elemento y la cantidad de elementos.
        Retorna el valor insertado si se insertó correctamente, o 0 si la cola está llena.
        """
        if self.__cant < self.__max:
            self.__items[self.__ul] = x  # Inserta el elemento en la posición 'ul'
            self.__ul = (self.__ul + 1) % self.__max  # Actualiza el índice del último elemento (operación circular)
            self.__cant += 1  # Incrementa la cantidad de elementos en la cola
            return x
        else:
            return 0  # Retorna 0 si la cola está llena
    
    def suprimir(self):
        """
        Elimina un elemento de la cola.
        Si la cola no está vacía, elimina y retorna el primer elemento de la cola,
        actualiza el índice del primer elemento y decrementa la cantidad de elementos.
        Si la cola está vacía, imprime un mensaje y retorna 0.
        """
        if self.vacia():
            print("Cola vacía")  # Imprime un mensaje si la cola está vacía
            return 0  # Retorna 0 si no hay elementos que eliminar
        else:
            x = self.__items[self.__pr]  # Guarda el elemento que se va a eliminar
            self.__pr = (self.__pr + 1) % self.__max  # Actualiza el índice del primer elemento (operación circular)
            self.__cant -= 1  # Decrementa la cantidad de elementos en la cola
            return x  # Retorna el elemento eliminado
    
    def recorrer(self):
        """
        Recorre y muestra todos los elementos actuales en la cola en el orden de llegada.
        """
        if not self.vacia():
            i = self.__pr  # Comienza en el índice del primer elemento
            j = 0  # Contador de elementos mostrados
            while j < self.__cant:  # Recorre mientras haya elementos en la cola
                print(self.__items[i])  # Imprime el elemento en la posición actual
                i = (i + 1) % self.__max  # Avanza al siguiente índice (operación circular)
                j += 1  # Incrementa el contador de elementos mostrados

# Ejemplo de uso:
cola = Cola(5)  # Crea una cola con capacidad para 5 elementos
cola.insertar(10)  # Inserta el elemento 10 en la cola
cola.insertar(20)  # Inserta el elemento 20 en la cola
cola.insertar(30)  # Inserta el elemento 30 en la cola
cola.recorrer()  # Muestra todos los elementos en la cola
print("Elemento suprimido:", cola.suprimir())  # Elimina y muestra el primer elemento de la cola
cola.recorrer()  # Muestra el estado actual de la cola


"""
Explicación Detallada:
Importación de la Biblioteca NumPy:

python
Copiar código
import numpy as np
Importamos NumPy, que es una biblioteca de Python usada para trabajar con arreglos de manera eficiente. Aquí se utiliza para manejar la representación interna de la cola.
Definición de la Clase Cola:

La clase Cola es una implementación de una cola secuencial circular, donde los elementos se manejan mediante un arreglo de NumPy.
Atributos Privados:
__max: Capacidad máxima de la cola.
__pr: Índice del primer elemento en la cola (el que se suprimirá primero).
__ul: Índice donde se insertará el próximo elemento.
__cant: Cantidad actual de elementos en la cola.
__items: Arreglo de NumPy que almacena los elementos de la cola.
Constructor __init__:

Inicializa la cola con un tamaño máximo especificado. Todos los atributos se inicializan en su estado por defecto.
Método vacia():

Verifica si la cola está vacía comparando la cantidad de elementos actuales con 0.
Método insertar(x):

Inserta un nuevo elemento x en la cola si hay espacio disponible.
Actualiza el índice de inserción (__ul) de manera circular, es decir, vuelve a 0 cuando alcanza el final del arreglo.
Si la cola está llena, retorna 0 para indicar que no se pudo insertar el elemento.
Método suprimir():

Elimina y retorna el primer elemento de la cola.
Actualiza el índice del primer elemento (__pr) de manera circular.
Si la cola está vacía, retorna 0 y muestra un mensaje de error.
Método recorrer():

Recorre y muestra todos los elementos en la cola en orden, desde el primer elemento hasta el último, sin alterar el estado de la cola.
Ejemplo de Uso:

Se muestra un ejemplo práctico de cómo utilizar la clase Cola para insertar y suprimir elementos, así como para mostrar su contenido.
Este código implementa una cola circular, lo que permite un uso eficiente del espacio en memoria, ya que los índices se ajustan automáticamente cuando llegan al final del arreglo, volviendo al inicio del mismo. Este tipo de cola es útil para escenarios donde los recursos de memoria son limitados o donde se requiere una estructura de datos con inserciones y eliminaciones frecuentes.

"""