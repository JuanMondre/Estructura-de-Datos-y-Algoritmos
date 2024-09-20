class Nodo:
    def __init__(self, elemento=None, sig=None):
        self.__elemento = elemento  # Dato almacenado en la nodo
        self.__sig = sig  # Puntero a la siguiente nodo

    def obtener_elemento(self):
        return self.__elemento  # Devuelve el valor del dato almacenado en la nodo

    def cargar_elemento(self, xelemento):
        self.__elemento = xelemento  # Asigna un valor al dato almacenado en la nodo

    def cargar_sig(self, xtope):
        self.__sig = xtope  # Asigna el puntero a la siguiente nodo

    def obtener_sig(self):
        return self.__sig  # Devuelve el puntero a la siguiente nodo

class Cola:
    def __init__(self, pr=None, ul=None, cant=0):
        self.__pr = pr  # Puntero al primer elemento de la cola
        self.__ul = ul  # Puntero al último elemento de la cola
        self.__cant = cant  # Cantidad de elementos en la cola

    def vacia(self):
        return self.__cant == 0  # Verifica si la cola está vacía

    def insertar(self, x):
        # Crea una nueva nodo y asigna el valor x a su elemento
        nuevoNodo = Nodo(x)
        nuevoNodo.cargar_sig(None)  # La nueva nodo no tiene una nodo siguiente

        if self.__ul is None:  # Si la cola está vacía
            self.__pr = nuevoNodo  # La primera nodo es también la última
        else:
            self.__ul.cargar_sig(nuevoNodo)  # Conecta la nueva nodo al final de la cola

        self.__ul = nuevoNodo  # Actualiza el puntero al último elemento de la cola
        self.__cant += 1  # Incrementa la cantidad de elementos en la cola
        return self.__ul.obtener_elemento()  # Devuelve el valor insertado

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return 0  # Retorna 0 si la cola está vacía
        else:
            aux = self.__pr  # Guarda la referencia a la nodo a eliminar
            x = self.__pr.obtener_elemento()  # Obtiene el valor del primer elemento de la cola
            self.__pr = self.__pr.obtener_sig()  # Actualiza el puntero al siguiente elemento
            self.__cant -= 1  # Decrementa la cantidad de elementos en la cola

            if self.__pr is None:  # Si la cola quedó vacía
                self.__ul = None  # Se actualiza ul a None

            del aux  # Libera la memoria ocupada por la nodo eliminada
            return x  # Devuelve el valor del elemento eliminado

    def recuperar_pr(self):
        return self.__pr  # Devuelve el puntero al primer elemento de la cola

    def recorrer(self):
        aux = self.__pr  # Comienza desde el primer elemento
        while aux is not None:  # Mientras haya elementos en la cola
            print(aux.obtener_elemento())  # Muestra el valor del elemento actual
            aux = aux.obtener_sig()  # Pasa al siguiente elemento
# Ejemplo de uso


def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Cargar Cola")
    print("2. Mostrar Cola")
    print("3. Suprimir elemento de la Cola")
    print("0. Finalizar")
    print("------------------------")

if __name__ == "__main__":
    cola = Cola()
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
Explicación y Comentarios Detallados del Código
Clase nodo:

__init__: Inicializa una nodo con un elemento y un puntero sig al siguiente nodo.
obtener_elemento: Devuelve el valor almacenado en la nodo.
cargar_elemento: Asigna un valor a la nodo.
cargar_sig: Asigna el puntero al siguiente nodo.
obtener_sig: Devuelve el puntero al siguiente nodo.
Clase Cola:

__init__: Inicializa la cola con punteros al primer y último nodo, y un contador de elementos.
vacia: Devuelve True si la cola está vacía, de lo contrario, False.
insertar: Inserta un nuevo valor en la cola:
Crea una nueva nodo con el valor x.
Si la cola está vacía, la nueva nodo se convierte en el primer elemento.
Si no, conecta la nueva nodo al final de la cola.
suprimir: Elimina y devuelve el primer elemento de la cola:
Si la cola está vacía, devuelve 0.
Si no, elimina el primer elemento y actualiza los punteros.
recuperar_pr: Devuelve el puntero al primer elemento de la cola.
recorrer: Muestra todos los elementos de la cola, comenzando desde el primer elemento.
Este diseño sigue la estructura original del código C++ pero adaptado a la sintaxis y filosofía de Python, usando la POO y manteniendo los atributos de la clase privados.


"""