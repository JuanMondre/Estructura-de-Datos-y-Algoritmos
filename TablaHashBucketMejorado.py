import numpy as np
import random

class tabla_hash_buckets:
    __lista: np.ndarray
    __capacidad_buckets: int
    __tamaño: int
    __contadores: list
    
    def __init__(self, claves=1000, capacidad_buckets=4):
        # Capacidad máxima de elementos por bucket
        self.__capacidad_buckets = capacidad_buckets
        # Tamaño total de la tabla hash calculado con un 20% extra de espacio
        self.__tamaño = int(claves / capacidad_buckets + (claves / capacidad_buckets) * 0.2)
        # Matriz de buckets, cada bucket con capacidad para 'capacidad_buckets' elementos
        self.__lista = np.zeros((self.__tamaño, capacidad_buckets))
        # Arreglo que cuenta cuántos elementos tiene cada bucket
        self.__contadores = np.zeros(self.__tamaño, dtype=int)
        # Dirección inicial para manejo de overflow
        self.__direccion_overflow = int(claves / capacidad_buckets)
    
    def metodo_extraccion(self, clave):
        # Extracción de los últimos dos dígitos de la clave
        return int(clave[-2:])
    
    def insertar(self, clave):
        direccion = self.metodo_extraccion(clave)
        
        if self.__contadores[direccion] < self.__capacidad_buckets:
            # Insertamos en el bucket si hay espacio disponible
            self.__lista[direccion][self.__contadores[direccion]] = float(clave)
            self.__contadores[direccion] += 1
            print(f"Insertó en la dirección {direccion} la clave {clave}.")
        else:
            # Manejo de overflow: encontrar el siguiente bucket disponible
            aux = self.__direccion_overflow
            while self.__contadores[aux] >= self.__capacidad_buckets and aux < self.__tamaño - 1:
                aux += 1
            if aux < self.__tamaño - 1:
                # Insertamos en el bucket de overflow encontrado
                self.__lista[aux][self.__contadores[aux]] = float(clave)
                self.__contadores[aux] += 1
                print(f"Insertó en la dirección {aux} la clave {clave} en overflow.")
    
    def buscar(self, clave):
        direccion = self.metodo_extraccion(clave)
        comparaciones = 0

        # Búsqueda secuencial en el bucket correspondiente
        for i in range(self.__capacidad_buckets):
            comparaciones += 1
            if self.__lista[direccion][i] == float(clave):
                print(f"Se encontró {clave} en {comparaciones} comparaciones.")
                return
        print(f"Clave {clave} no encontrada después de {comparaciones} comparaciones.")
    
    def contar_desbordados(self):
        # Contar buckets completamente llenos (desbordados)
        cont = 0
        for i in range(self.__tamaño):
            if self.__contadores[i] == self.__capacidad_buckets:
                cont += 1
        print(f"Cantidad de buckets desbordados: {cont}\n")
    
    def contar_subocupados(self):
        # Contar buckets que tienen menos de un tercio de su capacidad ocupada (subocupados)
        cont = 0
        for i in range(self.__tamaño):
            if self.__contadores[i] < int(self.__capacidad_buckets / 3):
                cont += 1
        print(f"Cantidad de buckets subocupados: {cont}\n")
    
    def contar_overflows(self):
        # Contar cuántos buckets en la zona de overflow están completamente llenos
        cont = 0
        aux = self.__direccion_overflow
        while aux < self.__tamaño:
            if self.__contadores[aux] == self.__capacidad_buckets:
                cont += 1
            aux += 1
        print(f"Cantidad de claves en overflow: {cont}\n")
    
    def contar_otros(self):
        # Contar buckets moderadamente ocupados (ni subocupados ni desbordados)
        cont = 0
        for bucket in self.__lista:
            elementos_ocupados = np.count_nonzero(bucket)
            if int(self.__capacidad_buckets / 3) < elementos_ocupados < self.__capacidad_buckets:
                cont += 1
        print(f"Cantidad de buckets moderadamente ocupados: {cont}\n")


if __name__ == '__main__':
    # Instancia de la tabla hash con buckets
    tabla = tabla_hash_buckets()

    # Insertamos 1000 claves aleatorias
    for _ in range(1000):
        clave = str(random.randint(46000000, 46999999))
        tabla.insertar(clave)

    # Llamadas a los métodos de conteo
    tabla.contar_desbordados()
    tabla.contar_subocupados()
    tabla.contar_overflows()
    tabla.contar_otros()
