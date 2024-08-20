import numpy as np  # Importa el módulo numpy para manejar arrays de manera eficiente

class PilaSecuencial:
    # Atributos privados de la clase
    __items: np.array  # Array para almacenar los elementos de la pila
    __cant: int  # Capacidad máxima de la pila
    __tope: int  # Índice del tope de la pila
    
    def __init__(self, __cant=0):
        # Método constructor, se ejecuta al crear una instancia de la clase
        self.__cant = __cant  # Inicializa la capacidad máxima de la pila
        self.__tope = -1  # Inicializa el tope en -1, indicando que la pila está vacía
        self.__items = np.zeros(__cant, dtype=int)  # Crea un array de ceros con capacidad 'cant' usando numpy
    
    def vacia(self):
        # Método para verificar si la pila está vacía
        return self.__tope == -1  # Devuelve True si el tope es -1, indicando que la pila está vacía
    
    def insertar(self, x):
        # Método para insertar un elemento en la pila
        if self.__tope < self.__cant - 1:  # Verifica si hay espacio en la pila (si el tope es menor que el máximo índice)
            self.__tope += 1  # Incrementa el tope para señalar el nuevo elemento
            self.__items[self.__tope] = x  # Almacena el elemento en la posición correspondiente del array
            return x  # Retorna el valor insertado
        else:
            return 0  # Si la pila está llena, retorna 0 indicando que no se pudo insertar
    
    def suprimir(self):
        # Método para eliminar el elemento en el tope de la pila
        if self.vacia():  # Verifica si la pila está vacía
            print("Pila vacía")  # Si está vacía, imprime un mensaje de error
            return 0  # Retorna 0 para indicar que no hay elementos para suprimir
        else:
            x = self.__items[self.__tope]  # Almacena el valor del elemento en el tope
            self.__tope -= 1  # Decrementa el tope, eliminando el último elemento
            return x  # Retorna el valor eliminado
    
    def mostrar(self):
        # Método para mostrar todos los elementos en la pila
        if not self.vacia():  # Verifica si la pila no está vacía
            for i in range(self.__tope, -1, -1):  # Itera desde el tope hacia abajo
                print(self.__items[i])  # Imprime cada elemento en la pila


if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad de elementos de la pila:\n"))
    pila = PilaSecuencial(cantidad)# Crea una pila con capacidad para 5 elemento
    #MENU DE OPCIONES:
    op = int(input("Ingrese opcion:\n 1_Carga Pila\n 2_ Muestra Pila\n 3_Suprime\n 4_Agrega Elemento a la pila\n 0_Para finalizar\n"))
    while op!=0:
        if op == 1:
            for i in range(cantidad):
                numero = int(input("\n Ingrese numero:"))
                pila.insertar(numero)  # Inserta el valor 10 en la pila
        elif op == 2:
            pila.mostrar()  # Muestra los elementos de la pila
        elif op == 3:
            pila.suprimir()  # Suprime el elemento en el tope (20)
        elif op == 4:
            pass
        else: print("Numero ingresado no corresponde\n")
        op = int(input("Ingrese opcion:\n 1_Carga Pila\n 2_ Muestra Pila\n 3_Suprime\n 4_Agrega Elemento a la pila\n 0_Para finalizar\n"))
