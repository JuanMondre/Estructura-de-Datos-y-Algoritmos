class Nodo:
    def __init__(self, elem):
        self.__elem = elem  # elem del nodo
        self.__siguiente = None  # Referencia al siguiente nodo

    def obtener_elem(self):
        return self.__elem

    def establecer_elem(self, elem):
        self.__elem = elem

    def obtener_siguiente(self):
        return self.__siguiente

    def establecer_siguiente(self, siguiente):
        self.__siguiente = siguiente


class ListaEncadenada:
    __cabeza : Nodo
    __tamaño : int
    
    def __init__(self, cabeza=None, tamaño= 0):
        self.__cabeza = cabeza  # Primer nodo de la lista
        self.__tamaño = tamaño  # Número de elementos en la lista

    def vacia(self):
        """Verifica si la lista está vacía."""
        return self.__cabeza is None

    def tamaño(self):
        """Devuelve el tamaño de la lista."""
        return self.__tamaño

    def insertar(self, elem, posicion):
        """Inserta un elem en una posición específica."""
        if posicion < 0 or posicion > self.__tamaño:
            raise IndexError("Posición fuera de rango")

        nuevo_nodo = Nodo(elem)

        if posicion == 0:
            nuevo_nodo.establecer_siguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            nodo_actual = self.__cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.obtener_siguiente()

            nuevo_nodo.establecer_siguiente(nodo_actual.obtener_siguiente())
            nodo_actual.establecer_siguiente(nuevo_nodo)

        self.__tamaño += 1

    def suprimir(self, posicion):
        """Suprime el nodo en la posición indicada y devuelve su elem."""
        if posicion < 0 or posicion >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            elem = self.__cabeza.obtener_elem()
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            nodo_actual = self.__cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.obtener_siguiente()

            nodo_a_suprimir = nodo_actual.obtener_siguiente()
            elem = nodo_a_suprimir.obtener_elem()
            nodo_actual.establecer_siguiente(nodo_a_suprimir.obtener_siguiente())

        self.__tamaño -= 1
        return elem

    def buscar(self, elem):
        """Busca un elem en la lista y devuelve la posición donde se encuentra, o -1 si no se encuentra."""
        nodo_actual = self.__cabeza
        posicion = 0
        while nodo_actual is not None:
            if nodo_actual.obtener_elem() == elem:
                return posicion
            nodo_actual = nodo_actual.obtener_siguiente()
            posicion += 1
        return -1

    def recuperar(self, posicion):
        """Devuelve el elem en la posición indicada."""
        if posicion < 0 or posicion >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        
        nodo_actual = self.__cabeza
        for _ in range(posicion):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_elem()

    def primer_elemento(self):
        """Devuelve el elem del primer nodo."""
        if self.vacia():
            return None
        return self.__cabeza.obtener_elem()

    def ultimo_elemento(self):
        """Devuelve el elem del último nodo."""
        if self.vacia():
            return None

        nodo_actual = self.__cabeza
        while nodo_actual.obtener_siguiente() is not None:
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_elem()

    def siguiente(self, posicion):
        """Devuelve el elem del nodo siguiente a la posición indicada."""
        if posicion < 0 or posicion >= self.__tamaño - 1:
            raise IndexError("No hay un nodo siguiente a esta posición")
        
        nodo_actual = self.__cabeza
        for _ in range(posicion):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_siguiente().obtener_elem()

    def anterior(self, posicion):
        """Devuelve el elem del nodo anterior a la posición indicada."""
        if posicion <= 0 or posicion >= self.__tamaño:
            raise IndexError("No hay un nodo anterior a esta posición")

        nodo_actual = self.__cabeza
        for _ in range(posicion - 1):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_elem()

    def recorrer(self):
        """Recorre e imprime todos los elemes de la lista."""
        nodo_actual = self.__cabeza
        while nodo_actual is not None:
            print(nodo_actual.obtener_elem())
            nodo_actual = nodo_actual.obtener_siguiente()

    def crear(self):
        """Inicializa la lista vacía."""
        self.__cabeza = None
        self.__tamaño = 0

    def vaciar(self):
        """Vacía la lista eliminando todos los nodos."""
        self.__cabeza = None
        self.__tamaño = 0

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Insertar elemento")
    print("2. Mostrar lista")
    print("3. Suprimir elemento de la lista")
    print("4. Recuperar elemento")
    print("5. Buscar elemento")
    print("6. Mostrar el último elemento")
    print("7. Mostrar el primer elemento")
    print("8. Mostrar elementos adyacentes de la lista")
    print("9. Vaciar lista")
    print("0. Finalizar")
    print("------------------------")


if __name__ == "__main__":
    lista = ListaEncadenada()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                elem = int(input("Ingrese el elem a insertar: "))
                posicion = int(input("Ingrese la posición donde insertar el elem: "))
                lista.insertar(elem, posicion)
                print(f"Elemento {elem} insertado en la posición {posicion}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print("Lista actual:")
            lista.recorrer()

        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posición del elemento a suprimir: "))
                elem = lista.suprimir(posicion)
                print(f"Elemento {elem} en la posición {posicion} ha sido eliminado")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición del elemento a recuperar: "))
                elem = lista.recuperar(posicion)
                print(f"Elemento en la posición {posicion}: {elem}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            elem = int(input("Ingrese el elem a buscar: "))
            posicion = lista.buscar(elem)
            if posicion != -1:
                print(f"El elem {elem} se encuentra en la posición {posicion}")
            else:
                print("El elem no se encuentra en la lista")

        elif opcion == "6":
            elem = lista.ultimo_elemento()
            if elem is not None:
                print(f"Último elemento de la lista: {elem}")
            else:
                print("La lista está vacía")

        elif opcion == "7":
            elem = lista.primer_elemento()
            if elem is not None:
                print(f"Primer elemento de la lista: {elem}")
            else:
                print("La lista está vacía")

        elif opcion == "8":
            try:
                posicion = int(input("Ingrese la posición del elemento: "))
                anterior = lista.anterior(posicion)
                siguiente = lista.siguiente(posicion)
                print(f"Elemento anterior: {anterior}, Elemento siguiente: {siguiente}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "9":
            lista.vaciar()
            print("La lista ha sido vaciada")

        elif opcion == "0":
            print("Finalizando el programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")




