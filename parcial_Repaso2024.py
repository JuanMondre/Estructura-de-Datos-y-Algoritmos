import numpy as np
"""1_a) estructura de datos pila secuencial
b) codifique un codigo para pasar de decimal a binario
2a) estructura de datos de la cola circular
b) haga el insertar
3a) estructura de datos de la lista encadenada
b) haga el codigo para concatenar dos listas"""

#1a
class pila_sec:
    __tope: int
    __elementos: np.array
    __cant_max: int
    def __init__(self,cant_max):
        self.__elementos = np.zeros(cant_max,dtype=int)
        self.__tope = 0
        self.__cant_max = cant_max
    def insertar(self,dato):
        if self.__tope == self.__cant_max:
            print("Llena")
        else:
            self.__elementos[self.__tope] = dato
            self.__tope+=1

    def eliminar(self):
        if self.vacia():
            print("No hay nada que eliminar\n")
        else:
            x = self.__elementos[self.__tope-1]
            self.__tope-=1
            return x
    def recorrer(self):
        for i in range(self.__tope-1,-1,-1):
            print(self.__elementos[i], end=" ")
            
def binario(n,pila):
    while n > 0:
        resto = n%2
        n = n//2
        pila.insertar(resto)
#2a)
class cola_cir:
    __pr: int
    __ul: int
    __cant_max:int
    __elementos: np.array
    __cant_elem: int
    def __init__(self,cant_max):
        self.__pr = 0
        self.__ul = 0
        self.__cant_max = cant_max
        self.__elementos = np.zeros(cant_max,dtype=int)
        self.__cant_elem = 0
    def vacia(self):
        return self.__cant_elem == 0
    def insertar(self,dato):
        if self.__cant_elem == self.__cant_max:
            print("Cola llena\n")
        else:
            self.__elementos[self.__ul] = dato
            self.__ul = (self.__ul+1) % self.__cant_max
            self.__cant_elem +=1
    def suprimir(self):
        if self.vacia():
            print("Nada que suprimir")
        else:
            x = self.__elementos[self.__pr]
            self.__pr = (self.__pr+1) % self.__cant_max
            self.__cant_elem-= 1
            return x
    def recorrer(self):
        if self.vacia():
            print("Nada que eliminar")
        else:
            i = self.__pr
            j = 0
            while j < self.__cant_elem:
                print(self.__elementos[i])
                i = (i+1) % self.__cant_max
                j +=1
class Nodo:
    __dato:int
    __sig: object
    def __init__(self,dato):
        self.__dato = dato
        self.__sig = None
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,sig):
        self.__sig = sig
class lista_enc:
    __cabeza: Nodo
    __cant_elem: int
    def __init__(self):
        self.__cabeza = None
        self.__cant_elem = 0
    def vacia(self):
        return self.__cant_elem == 0
    def insertar(self,dato,pos):
        nuevo = Nodo(dato)
        if 1 > pos > self.__cant_elem+1:
            print("mal ingresa la pos")
        else:
            if self.vacia() and pos == 1:
                self.__cabeza = nuevo
                self.__cant_elem+=1
            else:
                aux = self.__cabeza
                for _ in range(1,pos-1):
                    aux = aux.obtener_sig()
                if aux is not None:
                    nuevo.set_sig(aux.obtener_sig())
                    aux.set_sig(nuevo)
                    self.__cant_elem+=1
                else:
                    print("mal ingresa la pos")
            
    def suprimir(self,pos):
        if 1>pos> self.__cant_elem+1:
            print("Pos mal ingresada")
        else:
            if pos ==1:
                self.__cabeza = self.__cabeza.obtener_sig()
                self.__cant_elem-=1
            else:
                aux = self.__cabeza
                for _ in range(1,pos-1):
                    aux = aux.obtener_sig()
                if aux is not None and aux.obtener_sig() is not None:
                    aux.set_sig(aux.obtener_sig().obtener_sig())
                    self.__cant_elem-=1
                else:
                    print("Pos mal ingresada")
            
    def recuperar(self,pos):
        if 1 > pos > self.__cant_elem+1:
            print("Pos mal ingresada")
        else:
            aux = self.__cabeza
            for _ in range(1,pos):
                aux = aux.obtener_sig()
            if aux is not None:
                print(f"dato de la posicion {pos} es: {aux.obtener_dato()}")
                return aux.obtener_dato()
            else:
                print("Pos mal ingresada")
    def buscar(self,dato):
        aux = self.__cabeza
        band = False
        pos = 1
        while aux is not None and not band:
            if aux.obtener_dato() == dato:
                band = True
            else:
                aux = aux.obtener_sig()
                pos+=1
        print(f"elemento en la posicion:{pos}")
        return pos
    def primer_elem(self):
        if not self.vacia():
           #print(f"primer elemento: {self.__cabeza.obtener_dato()}")
            return self.__cabeza
    def ultimo_elem(self):
        if not self.vacia():
            aux = self.__cabeza
            while aux.obtener_sig() is not None:
                aux = aux.obtener_sig()
            #print(f"Ultimo elemento: {aux.obtener_dato()}")
            return aux
    def anterior(self,pos):
        if 1< pos<= self.__cant_elem:
            print(f"posicion anterior {pos-1}")
        else:
            print("no tiene anterior")
        return pos-1
    def siguiente(self,pos):
        if 1<= pos< self.__cant_elem:
            print(f"posicion siguiente {pos+1}")
        else:
            print("no tiene siguiente")
        return pos+1
    def recorrer(self):
        if self.vacia():
            print("No hay elemento en la lista\n")
        else:
            aux = self.__cabeza
            while aux is not None:
                print(aux.obtener_dato())
                aux = aux.obtener_sig()
    def concatenar(self,lista2):
        if not lista2.vacia() and not lista1.vacia(): #2ut + 2ut + 1ut
            self.ultimo_elem().set_sig(lista2.primer_elem())# 3ut
        #8ut complejidad constante mejor caso
if __name__ == '__main__': 
    """pila = pila_sec(8)
    binario(4,pila)
    pila.recorrer()
    cola = cola_cir(4)
    for i in range(4):
        cola.insertar(i+1)
    cola.suprimir()
    cola.recorrer()"""
    lista1 = lista_enc()
    lista1.insertar(1,1)
    lista1.insertar(2,2)
    lista1.insertar(3,3)
    lista1.insertar(4,4)
    """lista1.suprimir(4)
    lista1.primer_elem()
    lista1.ultimo_elem()
    lista1.siguiente(2)
    lista1.anterior(1)
    lista1.recuperar(2)
    lista1.buscar(2)"""
    print("LISTA 1:")
    lista1.recorrer()
    lista2 = lista_enc()
    lista2.insertar(5,1)
    lista2.insertar(6,2)
    lista2.insertar(7,3)
    lista2.insertar(8,4)
    print("LISTA 2:")
    lista2.recorrer()
    print("CONCATENAR 1 CON 2")
    lista1.concatenar(lista2)
    lista1.recorrer()