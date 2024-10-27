import numpy as np
import random
class TablaHash:
    __lista:np.array
    __M:int
    __N:int
    def __init__(self, N):
        self.__N = N
        self.__M = int(N/0.7)
        self.__lista = np.ndarray(self.__M, dtype = object)
        self.__lista.fill(None)
    def getTamaño(self):
        return self.__M
    
    def division(self,clave):
        return int (clave) % self.__M
    
    def insertar(self, clave):
        direccion = self.division(clave)                                                                              # Obtener la direccionición inicial usando el método de división
        cont = 1
        while self.__lista[direccion] is not None and cont<=self.__M:                                                 # Mientras no encontremos una direccionición vacía y no hayamos dado la vuelta completa
            cont+=1
            direccion = (direccion+1) % self.__M
        if cont <= self.__M:
            self.__lista[direccion] = clave
            print(f"Clave {clave} insertada en posición {direccion}")
            print(f"Comparaciones que ocupó: {cont}")
        else:
            print("Tabla llena")
            
    def buscar(self,clave):
        direccion = self.division(clave)
        cont=1
        flag=False
        while self.__lista[direccion] is not None and cont<=self.__M:
            if self.__lista[direccion] == clave:
                print("\nSe encontro la clave")
                flag =True
                return flag
            else:
                cont+=1
                direccion = (direccion+1) % self.__M
        if flag==False:
            print("\nNo se encontro el elemento")
            

    def imprimir_tabla(self):
        for i in range(self.__M):
            if self.__lista[i] is not None:
                print(f"direccion {i}: {self.__lista[i]}")

if __name__ == "__main__":
    # Ejemplo de uso
    tabla = TablaHash(11)  # Crea una tabla hash con tamaño primo
    print("\nEl tamaño total de la tabla es: ",tabla.getTamaño())
    for _ in range(1,20):
        tabla.insertar(random.randint(0,25))
    tabla.imprimir_tabla()
    tabla.buscar(10)
