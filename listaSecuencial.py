import numpy as np

class ListaSecuencial:
    
    __capacidad = int
    __elementos = list
    __tamano = int
    
    
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__elementos = np.empty(capacidad, dtype=int)
        self.__tamano = 0  # número de elementos actuales

    def insertar(self, elemento, posicion):
        if self.__tamano >= self.__capacidad:
            raise Exception("Lista llena")
        if posicion < 0 or posicion > self.__tamano:
            raise IndexError("Posición fuera de rango")
        for i in range(self.__tamano, posicion, -1):
            self.__elementos[i] = self.__elementos[i-1]
        self.__elementos[posicion] = elemento
        self.__tamano += 1

    def suprimir(self, posicion):
        if posicion < 0 or posicion >= self.__tamano:
            raise IndexError("Posición fuera de rango")
        for i in range(posicion, self.__tamano - 1):
            self.__elementos[i] = self.__elementos[i+1]
        self.__tamano -= 1

    def recuperar(self, posicion):
        if posicion < 0 or posicion >= self.__tamano:
            raise IndexError("Posición fuera de rango")
        return self.__elementos[posicion]

    def buscar(self, elemento):
        i=0 
        while i<self.__tamano:
            if self.__elementos[i]==elemento:
                return i
            else:
                i+=1
        return -1
    def primer_elemento(self):
        if self.__tamano == 0:
            raise Exception("Lista vacía")
        return self.__elementos[0]

    def ultimo_elemento(self):
        if self.__tamano == 0:
            raise Exception("Lista vacía")
        return self.__elementos[self.__tamano - 1]

    def siguiente(self, posicion):
        if posicion < 0 or posicion >= self.__tamano - 1:
            raise IndexError("No hay elemento siguiente")
        return self.__elementos[posicion + 1]

    def anterior(self, posicion):
        if posicion <= 0 or posicion >= self.__tamano:
            raise IndexError("No hay elemento anterior")
        return self.__elementos[posicion - 1]

    def recorrer(self):
        for i in range(self.__tamano):
            print(self.__elementos[i], end=" ")
        print()

    def vaciar(self):
        self.__tamano = 0
        
        
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
