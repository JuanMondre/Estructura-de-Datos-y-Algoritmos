class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None

    def obtener_valor(self):
        return self.__valor

    def obtener_siguiente(self):
        return self.__siguiente

    def cargar_siguiente(self, nodo):
        self.__siguiente = nodo

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.__cabeza is None or self.__cabeza.obtener_valor() >= valor:
            nuevo_nodo.cargar_siguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            actual = self.__cabeza
            while actual.obtener_siguiente() and actual.obtener_siguiente().obtener_valor() < valor:
                actual = actual.obtener_siguiente()
            nuevo_nodo.cargar_siguiente(actual.obtener_siguiente())
            actual.cargar_siguiente(nuevo_nodo)
        
        self.__tamaño += 1

    def suprimir(self, valor):
        if self.__cabeza is None:
            raise Exception("La lista está vacía")
        
        if self.__cabeza.obtener_valor() == valor:
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            actual = self.__cabeza
            while actual.obtener_siguiente() and actual.obtener_siguiente().obtener_valor() != valor:
                actual = actual.obtener_siguiente()
            
            if actual.obtener_siguiente() is None:
                raise Exception("Elemento no encontrado")
            
            actual.cargar_siguiente(actual.obtener_siguiente().obtener_siguiente())
        
        self.__tamaño -= 1

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        
        actual = self.__cabeza
        for i in range(pos):
            actual = actual.obtener_siguiente()
        
        return actual.obtener_valor()

    def buscar(self, valor):
        actual = self.__cabeza
        pos = 0
        while actual is not None:
            if actual.obtener_valor() == valor:
                return pos
            actual = actual.obtener_siguiente()
            pos += 1
        return -1

    def primer_elemento(self):
        if self.__cabeza is None:
            raise Exception("La lista está vacía")
        return self.__cabeza.obtener_valor()

    def ultimo_elemento(self):
        if self.__cabeza is None:
            raise Exception("La lista está vacía")
        
        actual = self.__cabeza
        while actual.obtener_siguiente() is not None:
            actual = actual.obtener_siguiente()
        
        return actual.obtener_valor()

    def siguiente(self, pos):
        if pos < 0 or pos >= self.__tamaño - 1:
            raise IndexError("No hay siguiente")
        return self.recuperar(pos + 1)

    def anterior(self, pos):
        if pos <= 0 or pos >= self.__tamaño:
            raise IndexError("No hay anterior")
        return self.recuperar(pos - 1)

    def recorrer(self):
        actual = self.__cabeza
        while actual:
            print(actual.obtener_valor(), end=" -> ")
            actual = actual.obtener_siguiente()
        print("None")

    def crear(self):
        self.__cabeza = None
        self.__tamaño = 0
        print("Lista creada vacía")

    def vaciar(self):
        self.__cabeza = None
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
    print("\n--- Lista Enlazada Ordenada ---")
    lista = ListaEnlazadaOrdenada()

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