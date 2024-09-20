import numpy as np

class ColaSecuencial: 
    __max_size : int
    __pr:int
    __ul: int
    __cant:int
    __elementos: int
    def __init__(self, max_size=0):
        # Inicializa la cola con los atributos privados
        self.__max_size = max_size  # Capacidad máxima de la cola
        self.__elementos = np.zeros(max_size, dtype=int)  # Arreglo que almacena los elementos de la cola
        self.__pr = 0  # Puntero al primer elemento de la cola (frente de la cola)
        self.__ul = 0  # Puntero al último elemento de la cola
        self.__cant = 0  # Cantidad actual de elementos en la cola

    def vacia(self):
        # Verifica si la cola está vacía
        return self.__cant == 0

    def insertar(self, x):
        # Inserta un nuevo elemento en la cola
        if self.__cant < self.__max_size:
            self.__elementos[self.__ul] = x  # Coloca el nuevo elemento en la posición indicada por ul
            self.__ul += 1  # Incrementa ul para que apunte al siguiente espacio vacío
            self.__cant += 1  # Incrementa la cantidad de elementos en la cola
            return x  # Devuelve el elemento insertado
        else:
            return 0  # Retorna 0 si la cola está llena

    def suprimir(self):
        # Elimina y retorna el elemento al frente de la cola
        if self.vacia():
            print("Cola vacía")
            return 0  # Retorna 0 si la cola está vacía
        else:
            x = self.__elementos[self.__pr]  # Toma el elemento al frente de la cola
            self.__pr += 1  # Incrementa pr para que apunte al siguiente elemento
            self.__cant -= 1  # Decrementa la cantidad de elementos en la cola
            return x  # Devuelve el elemento eliminado

    def recorrer(self):
        # Recorre y muestra los elementos de la cola
        if not self.vacia():
            for i in range(self.__pr, self.__pr + self.__cant):
                print(self.__elementos[i])

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Cargar Cola")
    print("2. Mostrar Cola")
    print("3. Suprimir elemento de la Cola")
    print("0. Finalizar")
    print("------------------------")
    
# Ejemplo de uso
if __name__ == "__main__":
    cant = int (input("Ingrese la cantidad de elementos de la cola: "))
    cola = ColaSecuencial(cant)
    op = -1
    while op != 0:
        mostrar_menu()
        try:
            op = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if op == 1:
            try:
                numero = int(input("\nIngrese un número: "))
                cola.insertar(numero)
                print(f"Número {numero} agregado a la Cola.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        elif op == 2:
            print("\n--- Mostrando Cola ---")
            cola.recorrer()
        elif op == 3:
            suprimido = cola.suprimir()
            if suprimido != 0:
                print(f"Elemento {suprimido} eliminado de la Cola.\n")
        else:
            print("Opción no válida. Intente nuevamente.\n")


"""
    Explicación del Código
    Inicialización (__init__):

    Se inicializan los atributos privados de la clase. __max_size es la capacidad máxima de la cola.
    __elementos es un arreglo de NumPy que almacena los elementos en la cola.
    __pr y __ul son punteros que mantienen el índice del primer y último elemento respectivamente.
    __cant lleva la cuenta del número de elementos en la cola.
    Método vacia:

    Devuelve True si la cola está vacía (cuando __cant es 0) y False en caso contrario.
    Método insertar:

    Si hay espacio en la cola, el método agrega el nuevo elemento en la posición indicada por __ul y ajusta los punteros. Si la cola está llena, devuelve 0.
    Método suprimir:

    Elimina y devuelve el primer elemento de la cola (el que está en la posición __pr). Si la cola está vacía, muestra un mensaje y devuelve 0.
    Método recorrer:

    Recorre los elementos en la cola desde __pr hasta __pr + __cant y los imprime.
    Este diseño evita la implementación circular y mantiene la simplicidad en la gestión de los punteros __pr y __ul. Sin embargo, es importante notar que una vez que __ul llega a __max_size, no podrá insertar más elementos a menos que se eliminen elementos desde el frente de la cola.
"""