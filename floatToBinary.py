class Celda:
    def __init__(self, item=None, sig=None):
        self.item = item  # Almacena el valor del elemento en la celda
        self.sig = sig  # Almacena la referencia a la siguiente celda en la pila

class PilaEncadenada:
    def __init__(self):
        self.tope = None  # Inicializa el tope de la pila como None, indicando que la pila está vacía
        self.cant = 0  # Inicializa el contador de elementos en la pila en 0

    def vacia(self):
        return self.tope is None  # Devuelve True si la pila está vacía, es decir, si el tope es None

    def insertar(self, x):
        # Crea una nueva celda con el valor x y la referencia al tope actual
        nueva_celda = Celda(x, self.tope)
        self.tope = nueva_celda  # Actualiza el tope de la pila a la nueva celda
        self.cant += 1  # Incrementa el contador de elementos en la pila

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")  # Si la pila está vacía, imprime un mensaje y devuelve None
            return None
        else:
            x = self.tope.item  # Obtiene el valor del elemento en el tope
            self.tope = self.tope.sig  # Actualiza el tope al siguiente nodo (celda)
            self.cant -= 1  # Decrementa el contador de elementos en la pila
            return x  # Devuelve el valor eliminado

    def mostrar(self):
        actual = self.tope  # Comienza desde el tope de la pila
        resultado = ""
        while actual is not None:
            resultado += str(actual.item)  # Agrega el valor del elemento a la cadena resultado
            actual = actual.sig  # Avanza al siguiente nodo en la pila
        return resultado  # Devuelve la representación en cadena de la pila

def convertir_a_binario(numero):
    parte_entera = int(numero)  # Separa la parte entera del número
    parte_fraccionaria = numero - parte_entera  # Calcula la parte fraccionaria restando la parte entera al número

    # Convertir la parte entera a binario
    pila_entera = PilaEncadenada()
    if parte_entera == 0:
        pila_entera.insertar(0)  # Si la parte entera es 0, se inserta directamente un 0 en la pila
    else:
        while parte_entera > 0:
            resto = parte_entera % 2  # Calcula el resto de dividir la parte entera por 2
            pila_entera.insertar(resto)  # Inserta el resto en la pila
            parte_entera = parte_entera // 2  # Actualiza la parte entera dividiéndola por 2

    # Convertir la parte fraccionaria a binario
    pila_fraccionaria = PilaEncadenada()
    contador_precision = 10  # Limitar la precisión de la conversión a 10 bits
    while parte_fraccionaria > 0 and contador_precision > 0:
        parte_fraccionaria *= 2  # Multiplica la parte fraccionaria por 2
        bit = int(parte_fraccionaria)  # Toma la parte entera del resultado como el siguiente dígito binario
        pila_fraccionaria.insertar(bit)  # Inserta el dígito binario en la pila
        parte_fraccionaria -= bit  # Resta la parte entera de la fracción actual para continuar con la parte fraccionaria
        contador_precision -= 1  # Decrementa el contador de precisión

    # Mostrar el resultado
    binario_entero = pila_entera.mostrar()  # Obtiene la representación binaria de la parte entera
    binario_fraccionario = pila_fraccionaria.mostrar()[::-1]  # Invierte la cadena de la parte fraccionaria para mostrarla correctamente

    # Si hay una parte fraccionaria, combina las dos partes con un punto decimal
    # Si no hay parte fraccionaria, simplemente devuelve la parte entera
    return f"{binario_entero}.{binario_fraccionario}" if binario_fraccionario else binario_entero

# Ejemplo de uso
if __name__ == "__main__":
    numero_decimal = float(input("Ingrese un número decimal (puede incluir decimales): "))
    binario = convertir_a_binario(numero_decimal)
    print(f"Representación binaria: {binario}")
