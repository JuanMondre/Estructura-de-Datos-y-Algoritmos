class Nodo:
    def __init__(self, valor):
        self.__valor = valor  # Valor del nodo
        self.__siguiente = None  # Referencia al siguiente nodo

    def obtener_valor(self):
        return self.__valor

    def establecer_valor(self, valor):
        self.__valor = valor

    def obtener_siguiente(self):
        return self.__siguiente

    def establecer_siguiente(self, siguiente):
        self.__siguiente = siguiente


class ListaEncadenada:
    def __init__(self):
        self.__primero = None  # Primer nodo de la lista
        self.__tamaño = 0  # Número de elementos en la lista

    def vacia(self):
        """Verifica si la lista está vacía."""
        return self.__primero is None

    def tamaño(self):
        """Devuelve el tamaño de la lista."""
        return self.__tamaño

    def insertar(self, valor, posicion):
        """Inserta un valor en una posición específica."""
        if posicion < 0 or posicion > self.__tamaño:
            raise IndexError("Posición fuera de rango")

        nuevo_nodo = Nodo(valor)

        if posicion == 0:
            nuevo_nodo.establecer_siguiente(self.__primero)
            self.__primero = nuevo_nodo
        else:
            nodo_actual = self.__primero
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.obtener_siguiente()

            nuevo_nodo.establecer_siguiente(nodo_actual.obtener_siguiente())
            nodo_actual.establecer_siguiente(nuevo_nodo)

        self.__tamaño += 1

    def suprimir(self, posicion):
        """Suprime el nodo en la posición indicada y devuelve su valor."""
        if posicion < 0 or posicion >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            valor = self.__primero.obtener_valor()
            self.__primero = self.__primero.obtener_siguiente()
        else:
            nodo_actual = self.__primero
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.obtener_siguiente()

            nodo_a_suprimir = nodo_actual.obtener_siguiente()
            valor = nodo_a_suprimir.obtener_valor()
            nodo_actual.establecer_siguiente(nodo_a_suprimir.obtener_siguiente())

        self.__tamaño -= 1
        return valor

    def buscar(self, valor):
        """Busca un valor en la lista y devuelve la posición donde se encuentra, o -1 si no se encuentra."""
        nodo_actual = self.__primero
        posicion = 0
        while nodo_actual is not None:
            if nodo_actual.obtener_valor() == valor:
                return posicion
            nodo_actual = nodo_actual.obtener_siguiente()
            posicion += 1
        return -1

    def recuperar(self, posicion):
        """Devuelve el valor en la posición indicada."""
        if posicion < 0 or posicion >= self.__tamaño:
            raise IndexError("Posición fuera de rango")
        
        nodo_actual = self.__primero
        for _ in range(posicion):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_valor()

    def primer_elemento(self):
        """Devuelve el valor del primer nodo."""
        if self.vacia():
            return None
        return self.__primero.obtener_valor()

    def ultimo_elemento(self):
        """Devuelve el valor del último nodo."""
        if self.vacia():
            return None

        nodo_actual = self.__primero
        while nodo_actual.obtener_siguiente() is not None:
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_valor()

    def siguiente(self, posicion):
        """Devuelve el valor del nodo siguiente a la posición indicada."""
        if posicion < 0 or posicion >= self.__tamaño - 1:
            raise IndexError("No hay un nodo siguiente a esta posición")
        
        nodo_actual = self.__primero
        for _ in range(posicion):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_siguiente().obtener_valor()

    def anterior(self, posicion):
        """Devuelve el valor del nodo anterior a la posición indicada."""
        if posicion <= 0 or posicion >= self.__tamaño:
            raise IndexError("No hay un nodo anterior a esta posición")

        nodo_actual = self.__primero
        for _ in range(posicion - 1):
            nodo_actual = nodo_actual.obtener_siguiente()
        
        return nodo_actual.obtener_valor()

    def recorrer(self):
        """Recorre e imprime todos los valores de la lista."""
        nodo_actual = self.__primero
        while nodo_actual is not None:
            print(nodo_actual.obtener_valor())
            nodo_actual = nodo_actual.obtener_siguiente()

    def crear(self):
        """Inicializa la lista vacía."""
        self.__primero = None
        self.__tamaño = 0

    def vaciar(self):
        """Vacía la lista eliminando todos los nodos."""
        self.__primero = None
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
                valor = int(input("Ingrese el valor a insertar: "))
                posicion = int(input("Ingrese la posición donde insertar el valor: "))
                lista.insertar(valor, posicion)
                print(f"Elemento {valor} insertado en la posición {posicion}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print("Lista actual:")
            lista.recorrer()

        elif opcion == "3":
            try:
                posicion = int(input("Ingrese la posición del elemento a suprimir: "))
                valor = lista.suprimir(posicion)
                print(f"Elemento {valor} en la posición {posicion} ha sido eliminado")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición del elemento a recuperar: "))
                valor = lista.recuperar(posicion)
                print(f"Elemento en la posición {posicion}: {valor}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            valor = int(input("Ingrese el valor a buscar: "))
            posicion = lista.buscar(valor)
            if posicion != -1:
                print(f"El valor {valor} se encuentra en la posición {posicion}")
            else:
                print("El valor no se encuentra en la lista")

        elif opcion == "6":
            valor = lista.ultimo_elemento()
            if valor is not None:
                print(f"Último elemento de la lista: {valor}")
            else:
                print("La lista está vacía")

        elif opcion == "7":
            valor = lista.primer_elemento()
            if valor is not None:
                print(f"Primer elemento de la lista: {valor}")
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




