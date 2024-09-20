import numpy as np  # Importa la librería numpy, que será usada para manejar arrays de forma eficiente

class ListaSecuencial:
    
    __capacidad = int  # La capacidad máxima de la lista
    __elementos = list  # El array que contendrá los elementos de la lista
    __tamano = int  # El número actual de elementos en la lista

    def __init__(self, capacidad):
        # Constructor que inicializa la capacidad y crea un array vacío de esa capacidad
        self.__capacidad = capacidad  # Almacena la capacidad máxima de la lista
        self.__elementos = np.empty(capacidad, dtype=int)  # Crea un array de tamaño fijo con capacidad definida
        self.__tamano = 0  # Inicializa el tamaño actual de la lista en 0 (lista vacía)

    def insertar(self, elemento, posicion):
        # Método para insertar un elemento en una posición específica
        if self.__tamano >= self.__capacidad:
            raise Exception("Lista llena")  # Si la lista está llena, lanza una excepción
        if posicion < 0 or posicion > self.__tamano:
            raise IndexError("Posición fuera de rango")  # Si la posición no es válida, lanza una excepción
        for i in range(self.__tamano, posicion, -1):
            # Desplaza los elementos hacia la derecha para hacer espacio en la posición
            self.__elementos[i] = self.__elementos[i-1]
        self.__elementos[posicion] = elemento  # Inserta el nuevo elemento en la posición especificada
        self.__tamano += 1  # Incrementa el tamaño de la lista

    def suprimir(self, posicion):
        # Método para eliminar un elemento de una posición específica
        if posicion < 0 or posicion >= self.__tamano:
            raise IndexError("Posición fuera de rango")  # Si la posición no es válida, lanza una excepción
        for i in range(posicion, self.__tamano - 1):
            # Desplaza los elementos hacia la izquierda para llenar el hueco del elemento suprimido
            self.__elementos[i] = self.__elementos[i+1]
        self.__tamano -= 1  # Decrementa el tamaño de la lista

    def recuperar(self, posicion):
        # Método para recuperar el valor de un elemento en una posición específica
        if posicion < 0 or posicion >= self.__tamano:
            raise IndexError("Posición fuera de rango")  # Si la posición no es válida, lanza una excepción
        return self.__elementos[posicion]  # Devuelve el valor del elemento en la posición dada

    def buscar(self, elemento):
        # Método para buscar un elemento en la lista y devolver su índice
        i = 0
        while i < self.__tamano:
            # Recorre la lista desde el principio hasta encontrar el elemento
            if self.__elementos[i] == elemento:
                return i  # Si encuentra el elemento, devuelve su índice
            else:
                i += 1  # Si no, continúa buscando
        return -1  # Si el elemento no se encuentra, devuelve -1

    def primer_elemento(self):
        # Método para obtener el primer elemento de la lista
        if self.__tamano == 0:
            raise Exception("Lista vacía")  # Si la lista está vacía, lanza una excepción
        return self.__elementos[0]  # Devuelve el primer elemento

    def ultimo_elemento(self):
        # Método para obtener el último elemento de la lista
        if self.__tamano == 0:
            raise Exception("Lista vacía")  # Si la lista está vacía, lanza una excepción
        return self.__elementos[self.__tamano - 1]  # Devuelve el último elemento

    def siguiente(self, posicion):
        # Método para obtener el elemento siguiente al de una posición dada
        if posicion < 0 or posicion >= self.__tamano - 1:
            raise IndexError("No hay elemento siguiente")  # Si no hay siguiente, lanza una excepción
        return self.__elementos[posicion + 1]  # Devuelve el elemento siguiente

    def anterior(self, posicion):
        # Método para obtener el elemento anterior al de una posición dada
        if posicion <= 0 or posicion >= self.__tamano:
            raise IndexError("No hay elemento anterior")  # Si no hay anterior, lanza una excepción
        return self.__elementos[posicion - 1]  # Devuelve el elemento anterior

    def recorrer(self):
        # Método para recorrer y mostrar todos los elementos de la lista
        for i in range(self.__tamano):  # Recorre desde el primer elemento hasta el último
            print(self.__elementos[i], end=" ")  # Imprime cada elemento con un espacio
        print()  # Nueva línea al final

    def vaciar(self):
        # Método para vaciar la lista
        self.__tamano = 0  # Resetea el tamaño de la lista a 0, esencialmente "vacía" la lista

        
        
if __name__ == "__main__":
    capacidad = int(input("Ingrese la capacidad de la lista\n"))
    lista = ListaSecuencial(capacidad)
    def mostrar_menu():
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Insertar elemento")
        print("2. Mostrar lista")
        print("3. Suprimir elemento de la lista")
        print("4. Recuperar elemento")
        print("5. Buscar elemento")
        print("6. Muestrar el ultimo elemento")
        print("7. Muestrar el primer elemento")
        print("8. Mostrar los elementos adyacentes de la lista")
        print("9. Vaciar Lista ")
        print("0. Para finaliazar ")
        print("------------------------") 
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
                posicion = int(input("\nIngrese una posicion: "))
                lista.insertar(numero,posicion)
                print(f"Número {numero} agregado a la lista en la posicion {posicion}.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        elif op == 2:
            print("\n--- Mostrando Lista ---")
            lista.recorrer()
        elif op == 3:
            posicion = int(input("ingrese la posicion a suprimir: "))
            suprimido = lista.suprimir(posicion)
            if suprimido != 0:
                print(f"Elemento {suprimido} eliminado de la lista.\n")
        elif op == 4:
            try:
                posicion = int(input("\nIngrese una posicion para obtener el elemento: "))
                print(f"Elemento {lista.recuperar(posicion)} Recuperado de la poscion {posicion}.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
                
        elif op==5:
            elemento = int (input("Ingrese un elemento a buscar: \n"))
            if lista.buscar(elemento)!=-1:
                print(f"Elemento {lista.buscar(elemento)} encontrado")
            else: print("El elemento no ha sido encontrado")
            
        elif op==6:
            print (F"El ultimo elemento de la lista es: {lista.ultimo_elemento()}.\n")
        elif op==7:
            print (F"El primer elemento de la lista es: {lista.primer_elemento()}.\n")
        elif op==8:
            posicion = int(input("Ingrese una posicion para mostrar el elemento anterior y el siguiente: \n"))
            print(lista.anterior(posicion))
            print(lista.siguiente(posicion))
        
        elif op==9:
            lista.vaciar()
        
        elif op == 0:
            print("Finalizando el programa...\n")
        else:
            print("Opción no válida. Intente nuevamente.\n")
