class Celda:
    __item:int
    __sig:int 
    def __init__(self, item=None, sig=None):
        # Constructor de la clase Celda
        self.__item = item  # Almacena el valor del elemento en la celda
        self.__sig = sig  # Almacena la referencia a la siguiente celda en la pila
    
    def obtener_item(self):
        # Método para obtener el valor del elemento en la celda
        return self.__item  # Retorna el valor almacenado en la celda
    
    def cargar_item(self, xitem):
        # Método para establecer el valor del elemento en la celda
        self.__item = xitem  # Asigna el valor pasado como argumento al elemento de la celda
    
    def cargar_sig(self, xtope):
        # Método para establecer la referencia a la siguiente celda
        self.__sig = xtope  # Asigna la referencia de la siguiente celda a '__sig'
    
    def obtener_sig(self):
        # Método para obtener la referencia a la siguiente celda
        return self.__sig  # Retorna la referencia a la siguiente celda

class Pila:
    __cant:int
    __tope:int
    
    def __init__(self, xtope=None, xcant=0):
        # Constructor de la clase Pila
        self.__cant = xcant  # Inicializa el contador de elementos en la pila
        self.__tope = xtope  # Inicializa el __tope de la pila como None o la celda pasada como argumento
    
    def vacia(self):
        # Método para verificar si la pila está vacía
        return self.__cant == 0  # Devuelve True si la pila no contiene elementos
    
    def insertar(self, x):
        # Método para insertar un nuevo elemento en la pila
        ps1 = Celda()  # Crea una nueva celda
        ps1.cargar_item(x)  # Carga el valor 'x' en la nueva celda
        ps1.cargar_sig(self.__tope)  # Establece la nueva celda como el __tope, apuntando al antiguo __tope
        self.__tope = ps1  # Actualiza el __tope de la pila a la nueva celda
        self.__cant += 1  # Incrementa el contador de elementos en la pila
        return ps1.obtener_item()  # Retorna el valor insertado
    
    def suprimir(self):
        # Método para eliminar el elemento en el __tope de la pila
        if self.vacia():  # Verifica si la pila está vacía
            print("Pila vacía")  # Imprime un mensaje de error si está vacía
            return 0  # Retorna 0 para indicar que no se pudo eliminar nada
        else:
            aux = self.__tope  # Almacena la referencia a la celda en el __tope
            x = aux.obtener_item()  # Obtiene el valor del elemento en el __tope
            self.__tope = aux.obtener_sig()  # Actualiza el __tope a la siguiente celda
            self.__cant -= 1  # Decrementa el contador de elementos en la pila
            return x  # Retorna el valor eliminado
    
    def mostrar_tope(self):
        # Método para mostrar el valor del elemento en el __tope de la pila
        if not self.vacia():  # Verifica si la pila no está vacía
            return self.__tope.obtener_item()  # Retorna el valor del elemento en el __tope
    
    def recuperar_tope(self):
        # Método para recuperar la referencia al __tope de la pila
        return self.__tope  # Retorna la referencia al __tope actual de la pila
    
    def recorrer(self, aux):
        # Método para recorrer la pila y mostrar sus elementos
        if aux is not None:  # Verifica si la celda actual no es None
            print(aux.obtener_item())  # Imprime el valor del elemento en la celda actual
            self.recorrer(aux.obtener_sig())  # Llama recursivamente al método para recorrer la siguiente celda
            
    def mostrarHorizontalmente(self):
        actual = self.__tope
        resultado = ""
        while actual is not None:
            resultado += str(actual.obtener_item())
            actual = actual.obtener_sig()
        print(resultado)



# Ejemplo de uso
if __name__ == '__main__':
    def mostrar_menu():
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Cargar Pila")
        print("2. Mostrar Pila")
        print("3. Suprimir")
        print("4. Agregar Elemento a la Pila")
        print("0. Finalizar")
        print("------------------------")
    pila = Pila()  
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
                pila.insertar(numero)
                print(f"Número {numero} agregado a la pila.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        elif op == 2:
            print("\n--- Mostrando Pila ---")
            pila.recorrer(pila.recuperar_tope())
            print(f"El tope es: {pila.mostrar_tope()}\n")
        elif op == 3:
            suprimido = pila.suprimir()
            if suprimido != 0:
                print(f"Elemento {suprimido} eliminado de la pila.\n")
        elif op == 4:
            try:
                numero = int(input("\nIngrese un número para agregar: "))
                pila.insertar(numero)
                print(f"Número {numero} agregado a la pila.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        elif op == 0:
            print("Finalizando el programa...\n")
        else:
            print("Opción no válida. Intente nuevamente.\n")


