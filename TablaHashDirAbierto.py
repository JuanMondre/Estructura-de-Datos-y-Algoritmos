import numpy as np
import random                                                                           #Lo utlizamos para generar las claves aleatorias
class TablaHash:
    __lista:np.array
    
    def __init__(self,flag, N=100):
        """
        El constructor inicializa la tabla hash. Recibe dos parámetros:
            Flag: Booleano que determina si el tamaño de la tabla debe ser un número primo.
            N: Que por defecto es 100 y es el número de elementos aproximado que se quieren almacenar.
            La tabla necesita más espacio del que se planea usar para evitar colisiones. Se ajusta con un factor de carga de 0.7 (int(N / 0.7)).
            Si flag es True, se llama a la función primo para asegurar que el tamaño sea un número primo.
        """                                       
        if flag:
            self.__M = self.primo(int(N/0.7))
        else:
            self.__M = int(N/0.7)
        self.__lista = np.ndarray(self.__M, dtype=object)
        self.__lista.fill(None)                                                         #Llenamos la lista con None para evitar valores basura.
    
    def primo(self,x):
        i = 2
        while i < x and x % i != 0:                                                     #Verificamos si el número 'x' es primo
            i += 1
        if i == x:                                                                      
            return x                                                                    #Si es primo, devolvemos 'x'
        else:
            return self.primo(x + 1)                                                    #Si no es primo, buscamos el siguiente número primo
    
    #Metodos de transformacion de claves
    def division(self,clave):                                                           #Aplica el módulo con el tamaño de la tabla (self.__M), utilizando el valor numérico de la clave.
        return int(clave) % self.__M
    
    def extraccion(self,clave):                                                         #Toma los últimos tres dígitos de la clave.
        return int(clave[-3:])
    
    def plegado(self,clave):                                                            #Suma grupos de dos dígitos de la clave y devuelve el resultado modulado por el tamaño de la tabla.
        claveStr = str(clave)
        suma = 0
        for i in range(0,len(claveStr),2):
            suma+=int(claveStr[i:i+2])
        return suma % self.__M
    
    def cuadradoMedio(self,clave):                                                      #Calcula el cuadrado de la clave, extrae los dígitos centrales y devuelve el resultado modulado.
        cuadrado = str(int(clave)**2)
        midIndex=len(cuadrado) // 2
        if len(cuadrado) > 2:
            resultado = int(cuadrado[midIndex - 1: midIndex +1])
        else:
            resultado = int(cuadrado)
        return resultado % self.__M
    
    def alfanumerico(self,clave):                                                       #Convierte cada carácter de la clave en su valor ASCII y suma estos valores.
        suma=0
        for char in str(clave):
            suma+= ord(char)
        return suma % self.__M
    
    def insertar(self,clave,metodo):                                                    #Inserta una clave utilizando la función de hash seleccionada por el usuario
        """
        El parámetro metodo indica qué función de hash utilizar (división, extracción, plegado, etc.).
        Direccion obtiene la posición inicial donde intentará insertar la clave.
        """
        cont = 1                                                                        #Contador de intentos de comparación/inserción(cuenta cuantas veces se ha tratado de inserta una clave en una posicion ya ocupada)
        if metodo == 1:
            direccion = self.division(clave)
        elif metodo == 2:
            direccion = self.extraccion(clave)
        elif metodo ==3:
            direccion = self.plegado(clave)
        elif metodo == 4:
            direccion = self.cuadradoMedio(clave)
        elif metodo == 5:
            direccion = self.alfanumerico(clave)
        else:
            print("Opcion ingresada incorrecta\n")
            return
        
        direccion = direccion % self.__M                                                #Asegurar que dirección esté en el rango
        
        while self.__lista[direccion] is not None and cont != self.__M:                 #Si la posición direccion ya está ocupada, se avanza a la siguiente posición en el arreglo (direccion + 1), en forma circular (gracias al operador % self.__M).
            cont+=1                                                                     #Se incrementa por cada intento de encontrar una posición vacía
            direccion = (direccion+1) % self.__M                                        #Intentamos la siguiente posición de manera circular
            direccion = direccion % self.__M                                            #Asegurar que dirección esté en el rango
        if cont != self.__M:                                                            #Si se encuentra un espacio disponible, se inserta la clave en la tabla.
            self.__lista[direccion] = clave
            print(self.__lista[direccion])
            print(f"Comparaciones que ocupó: {cont}")
        else:
            print("Tabla llena")
            
    def buscar(self,clave):
        """
        Este método busca una clave en la tabla. Empieza en la posición calculada por la función de hash y sigue avanzando en caso de colisiones, usando el mismo patrón circular que en la inserción.
        Si encuentra la clave, reporta el número de comparaciones. Si no, indica que no se encontró.
        """
        print("Buscando")
        direccion = self.division(clave)
        cont = 1                                                                       #Cuenta cuántas comparaciones han sido necesarias para encontrar la clave en la tabla hash.
        band = False
        while self.__lista[direccion] is not None  and cont != self.__M:
            if self.__lista[direccion] == clave:
                print(f"el valor: {self.__lista[direccion]} se encontró en {cont} comparaciones\n")
                cont = self.__M
                band = True
            else:
                direccion = (direccion+1) % self.__M
                cont+=1
        if not band:
            print("No se encontró")
            
if __name__ == '__main__':
    op = int(input("Ingrese una opcion: \n1) Tabla Hash con numero primo \n2) Tabla Hash sin primo\n"))
    op_metodo = int(input("Elección de la Función de Transformación:\n1)Division.\n2)Extración.\n3)Plegado.\n4)Cuadrado medio.\n5)Alfanumerico.\n"))
    while op!=0:
        if op ==1:
            tabla = TablaHash(True) #para que sea primo el tamaño
            for _ in range(1,100):
                tabla.insertar(str(random.randint(46000000,46999999)),op_metodo)
            
        elif op==2:
            tabla = TablaHash(False) #para que no sea primo el tamaño
            for _ in range(1,100):
                tabla.insertar(str(random.randint(46000000,46999999)),op_metodo)
        op = int(input("Ingrese una opcion: \n1) Tabla Hash con numero primo \n2) Tabla Hash sin primo\n"))
        op_metodo = int(input("Elección de la Función de Transformación:\n 1)Division.\n 2)Extración.\n 3)Plegado.\n 4)Cuadrado medio.\n 5)Alfanumerico.\n"))
            
