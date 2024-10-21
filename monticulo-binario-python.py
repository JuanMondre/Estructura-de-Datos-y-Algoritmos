import numpy as np

class MonticuloBinarioSimplificado:
    """
    Implementación simplificada de un Montículo Binario Mínimo usando NumPy.
    """

    def __init__(self, capacidad):
        """
        Inicializa el montículo binario.

        Args:
            capacidad (int): Número máximo de elementos que puede contener el montículo.
        """
        self.__heap = np.zeros(capacidad, dtype=int)
        self.__tamano = 0
        self.__capacidad = capacidad

    def __obtener_padre(self, i):
        """Calcula el índice del padre de un nodo."""
        return (i - 1) // 2

    def __obtener_hijo_izquierdo(self, i):
        """Calcula el índice del hijo izquierdo de un nodo."""
        return 2 * i + 1

    def __obtener_hijo_derecho(self, i):
        """Calcula el índice del hijo derecho de un nodo."""
        return 2 * i + 2

    def __intercambiar(self, i, j):
        """Intercambia dos elementos en el montículo."""
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def insertar(self, elemento):
        """
        Inserta un nuevo elemento en el montículo.

        Args:
            elemento (int): El elemento a insertar.
        """
        if self.__tamano >= self.__capacidad:
            print("Error: El montículo está lleno")
            return

        # Agregar el elemento al final del montículo
        self.__heap[self.__tamano] = elemento
        self.__tamano += 1

        # Reorganizar el montículo para mantener la propiedad de montículo mínimo
        indice_actual = self.__tamano - 1
        while indice_actual > 0:
            indice_padre = self.__obtener_padre(indice_actual)
            if self.__heap[indice_actual] < self.__heap[indice_padre]:
                self.__intercambiar(indice_actual, indice_padre)
                indice_actual = indice_padre
            else:
                break

    def eliminarMinimo(self):
        """
        Elimina y retorna el elemento mínimo del montículo.

        Returns:
            int: El elemento mínimo, o None si el montículo está vacío.
        """
        if self.__tamano == 0:
            print("Error: El montículo está vacío")
            return None

        # Guardar el elemento mínimo (raíz) para devolverlo
        minimo = self.__heap[0]

        # Mover el último elemento a la raíz y reducir el tamaño
        self.__heap[0] = self.__heap[self.__tamano - 1]
        self.__tamano -= 1

        # Reorganizar el montículo para mantener la propiedad de montículo mínimo
        indice_actual = 0
        while True:
            indice_hijo_izq = self.__obtener_hijo_izquierdo(indice_actual)
            indice_hijo_der = self.__obtener_hijo_derecho(indice_actual)
            indice_menor = indice_actual

            if indice_hijo_izq < self.__tamano and self.__heap[indice_hijo_izq] < self.__heap[indice_menor]:
                indice_menor = indice_hijo_izq

            if indice_hijo_der < self.__tamano and self.__heap[indice_hijo_der] < self.__heap[indice_menor]:
                indice_menor = indice_hijo_der

            if indice_menor != indice_actual:
                self.__intercambiar(indice_actual, indice_menor)
                indice_actual = indice_menor
            else:
                break

        return minimo

    def obtenerMinimo(self):
        """
        Retorna el elemento mínimo sin eliminarlo.

        Returns:
            int: El elemento mínimo, o None si el montículo está vacío.
        """
        if self.__tamano == 0:
            print("Error: El montículo está vacío")
            return None
        return self.__heap[0]

    def tamano(self):
        """Retorna el número de elementos en el montículo."""
        return self.__tamano

    def estaVacio(self):
        """Verifica si el montículo está vacío."""
        return self.__tamano == 0

    def imprimir(self):
        """Imprime los elementos del montículo."""
        print(self.__heap[:self.__tamano])

def main():
    """
    Función principal para probar la implementación del Montículo Binario Simplificado.
    """
    monticulo = MonticuloBinarioSimplificado(10)

    print("Prueba 1: Insertar elementos")
    elementos = [5, 3, 7, 1, 4, 6, 2]
    for elemento in elementos:
        monticulo.insertar(elemento)
        print(f"Insertado {elemento}. Montículo actual:", end=" ")
        monticulo.imprimir()

    print("\nPrueba 2: Obtener mínimo")
    print("Mínimo actual:", monticulo.obtenerMinimo())

    print("\nPrueba 3: Eliminar mínimo")
    for _ in range(len(elementos)):
        minimo = monticulo.eliminarMinimo()
        print(f"Eliminado {minimo}. Montículo actual:", end=" ")
        monticulo.imprimir()

    print("\nPrueba 4: Intentar eliminar de un montículo vacío")
    monticulo.eliminarMinimo()

    print("\nPrueba 5: Insertar más elementos que la capacidad")
    for i in range(12):
        monticulo.insertar(i)

if __name__ == "__main__":
    main()