import numpy as np

class ListaSecuencialOrdenada:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__lista = np.empty(self.__capacidad, dtype=int)
        self.__tamaño = 0

    def insertar(self, valor):
        if self.__tamaño >= self.__capacidad:
            raise Exception("La lista está llena")
        
        pos = 0
        while pos < self.__tamaño and self.__lista[pos] < valor:
            pos += 1
        
        for i in range(self.__tamaño, pos, -1):
            self.__lista[i] = self.__lista[i-1]
        
        self.__lista[pos] = valor
        self.__tamaño += 1

    def suprimir(self, valor):
        pos = self.buscar(valor)
        if pos == -1:
            raise Exception("Elemento no encontrado")
        
        for i in range(pos, self.__tamaño - 1):
            self.__lista[i] = self.__lista[i + 1]
        
        self.__tamaño -= 1

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        return self.__lista[pos]

    def buscar(self, valor):
        pos = 0
        while pos < self.__tamaño:
            if self.__lista[pos] == valor:
                return pos
            pos += 1
        return -1

    def primer_elemento(self):
        if self.__tamaño == 0:
            raise Exception("La lista está vacía")
        return self.__lista[0]

    def ultimo_elemento(self):
        if self.__tamaño == 0:
            raise Exception("La lista está vacía")
        return self.__lista[self.__tamaño - 1]

    def siguiente(self, pos):
        if pos < 0 or pos >= self.__tamaño - 1:
            raise IndexError("No hay siguiente")
        return self.__lista[pos + 1]

    def anterior(self, pos):
        if pos <= 0 or pos >= self.__tamaño:
            raise IndexError("No hay anterior")
        return self.__lista[pos - 1]

    def recorrer(self):
        for i in range(self.__tamaño):
            print(self.__lista[i], end=" ")
        print()

    def crear(self):
        self.__tamaño = 0
        print("Lista creada vacía")

    def vaciar(self):
        self.__tamaño = 0
        print("Lista vaciada")

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Insertar elemento")
    print("2. Suprimir elemento")
    print("3. Recuperar elemento")
    print("4. Buscar elemento")
    print("5. Mostrar primer elemento")
    print("6. Mostrar último elemento")
    print("7. Siguiente elemento")
    print("8. Elemento anterior")
    print("9. Recorrer lista")
    print("10. Vaciar lista")
    print("0. Salir")
    print("------------------------")

if __name__ == "__main__":
    print("\n--- Lista Secuencial Ordenada ---")
    capacidad = int(input("Ingrese la capacidad máxima de la lista: "))
    lista = ListaSecuencialOrdenada(capacidad)

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == '1':
            elemento = int(input("Ingrese el elemento a insertar: "))
            lista.insertar(elemento)
        elif opcion == '2':
            posicion = int(input("Ingrese la posición del elemento a suprimir: "))
            lista.suprimir(posicion)
        elif opcion == '3':
            posicion = int(input("Ingrese la posición del elemento a recuperar: "))
            print(f"Elemento recuperado: {lista.recuperar(posicion)}")
        elif opcion == '4':
            elemento = int(input("Ingrese el elemento a buscar: "))
            resultado = lista.buscar(elemento)
            if resultado != -1:
                print(f"Elemento encontrado en la posición: {resultado}")
            else:
                print("Elemento no encontrado")
        elif opcion == '5':
            print(f"Primer elemento: {lista.primer_elemento()}")
        elif opcion == '6':
            print(f"Último elemento: {lista.ultimo_elemento()}")
        elif opcion == '7':
            posicion = int(input("Ingrese la posición del elemento actual: "))
            print(f"Siguiente elemento: {lista.siguiente(posicion)}")
        elif opcion == '8':
            posicion = int(input("Ingrese la posición del elemento actual: "))
            print(f"Elemento anterior: {lista.anterior(posicion)}")
        elif opcion == '9':
            lista.recorrer()
        elif opcion == '10':
            lista.vaciar()
            print("Lista vaciada.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
