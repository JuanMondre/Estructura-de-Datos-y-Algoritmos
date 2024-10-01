class Nodo:
    __elem:int
    __sig:object
    def __init__(self,elem):
        self.__sig = None 
        self.__elem = elem  
    def setSig(self,sig):
        self.__sig = sig
    def setElem(self,elem):
        self.__elem = elem
    def getSig(self):
        return self.__sig
    def getElem(self):
        return self.__elem  
    
class colaEnlazada:
    __pr: Nodo
    __ul: Nodo
    __cant:int
    
    def __init__(self,cant=0):
        self.__ul = None
        self.__pr = None
        self.__cant = cant
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nodo = Nodo (x)
        if self.vacia(): 
            self.__pr = nodo #si la cola esta vacia entonces el nodo creado es el prmer elemenro
            self.__ul = nodo
        else:
            self.__ul.setSig(nodo) #si no esta vacia entonces el siguiente del ultimo apunta al nuevo nodo y el ultimo ahora es el nuevo nodo
        self.__ul = nodo
        self.__cant+=1
    
    def eliminar(self):
        if self.vacia():
            print("No hay nada para eliminar")
        else:   
            aux = self.__pr
            x = aux.getElem()
            self.__pr = aux.getSig()
            self.__cant -=1
        return x
    
    def mostrar(self):
        if self.vacia():
            print("No hay nada para mostrar")
        else:
            aux = self.__pr
            while aux is not None:
                print(aux.getElem())
                aux = aux.getSig()
                
    def mostrarCant(self):
        return self.__cant
        
if __name__ == "__main__":
    cola = colaEnlazada()
    tiempoSimulacion = 45 #TIEMPO QUE DURA LA ATENCION
    frecuenciaCliente=10  #FRECUENCIA DE LLEGADA DEL CLIENTE
    tiempoAtencion = 15  #TIEMPO QUE SE DEMORAN EN ANTENDER A UN CLEINTE

    proxLLegada = 0
    tiempoActual=0
    personasAtendidas=0
    empleadoLibre =0
    clienteID = 1
    
    while tiempoActual < tiempoSimulacion:
        if tiempoActual == proxLLegada:   #LLEGA EL PRIMER CLIENTE Y SE PONE A LA COLA 
            cola.insertar(clienteID)
            print(f"Minuto {tiempoActual}: Llega el solicitante {clienteID} a la cola.")
            clienteID +=1
            proxLLegada += frecuenciaCliente # LOS CLIENTES SE VAN INSERTANDO A MEDIDA QUE VAN LLEGANDO
            
        if tiempoActual >= empleadoLibre and not cola.vacia(): #EL PRIMERCLIENTE ES ATENDIDO 
            clienteAtendido = cola.eliminar()
            if clienteAtendido is not None:
                personasAtendidas+=1
                empleadoLibre = tiempoActual + tiempoAtencion  
                print(f"Minuto {tiempoActual}: Se atiende al solicitante {clienteAtendido}. El empleado estará libre en el minuto {empleadoLibre}.")
        
        tiempoActual+=1 #CORRE EL TIEMPO
            
    print("\n--- Resultados de la Simulación ---")
    print(f"Cantidad de solicitantes atendidos: {personasAtendidas}")
    print(f"Cantidad de solicitantes en la cola al finalizar: {cola.mostrarCant()}")        
    