
class Celda:
    __item:int
    def __init__(self, __item=None, __sig=None):
        # Constructor de la clase Celda
        self.__item = __item  # Almacena el valor del elemento en la celda
        self.__sig = __sig  # Almacena la referencia a la siguiente celda en la pila
    
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
    def __init__(self):
        self.__tope=None
        
    def vacia(self):
        return self.__tope is None
    
    def insertar(self, x):
        nueva_celda = Celda(x,self.__tope)
        self.__tope = nueva_celda
        
    def suprimir(self):
        if self.vacia():
            return None
        else:
            x = self.__tope.obtener_item()
            self.__tope = self.__tope.obtener_sig()
            return x
    def mostrar(self):
        actual = self.__tope
        elementos=[]
        while actual:
            elementos.append(str(actual.obtener_item()))
            actual = actual.obtener_sig()
        return ' -> '.join(elementos)
    
def factorial_simulado(n):
    pila=Pila()
    resultado=1
    while True:
        if n>0:
            pila.insertar(n)
            print(f"Insertando {n} en la pila. Pila Actual: {pila.mostrar()}")
            n-=1
        else:
            resultado=1
            print("Alcandado el caso base: n=o, resultado =1")
            break
    while not pila.vacia():
        n=pila.suprimir()
        resultado *=n
        print(f"Sacando {n} de la pila. Pila Actual: {pila.mostrar()}")
        print(f"Calculando factorial de {n}. Resultado: {resultado}")
    return resultado

if __name__ == "__main__":
    
    numero=int(input("Ingrese un numero para calcular su factorial: "))
    resultado = factorial_simulado(numero)
    print(f"Calculando factorial de {numero}. Resultado: {resultado}")        