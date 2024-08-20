from PilaEncadenada import Pila
from PilaEncadenada import Celda

def IntToBinary (x):
    while x > 0:
        resto = x % 2  # Obtener el resto de la división por 2
        pila.insertar(resto)  # Almacenar el resto en la pila
        x = x // 2  # Actualizar el número dividiéndolo por 2

def recorrer( aux):
        # Método para recorrer la pila y mostrar sus elementos
        if aux is not None:  # Verifica si la celda actual no es None
            print(aux.obtener_item())  # Imprime el valor del elemento en la celda actual
            recorrer(aux.obtener_sig())  # Llama recursivamente al método para recorrer la siguiente celda

if __name__ == '__main__':
    pila = Pila() #USO LA ESTRUCTURA PILA ENCADENADA
    numero = int(input("Ingrese un numero decimal para convertirlo a binario: \n"))
    IntToBinary(numero)
    print("Representación binaria: ")
    pila.mostrarHorizontalmente()  # Mostrar los restos en orden inverso (pop de la pila)
    