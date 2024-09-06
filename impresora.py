class Trabajo:
    def __init__(self, tiempo):
        self.__tiempo = tiempo  # Tiempo necesario para imprimir el trabajo
        self.__sig = None  # Puntero al siguiente trabajo en la cola

    def obtener_tiempo(self):
        return self.__tiempo

    def cargar_tiempo(self, tiempo):
        self.__tiempo = tiempo

    def obtener_sig(self):
        return self.__sig

    def cargar_sig(self, siguiente):
        self.__sig = siguiente


class ColaImpresion:
    def __init__(self):
        self.__pr = None  # Puntero al primer trabajo en la cola
        self.__ul = None  # Puntero al último trabajo en la cola
        self.__cant = 0  # Cantidad de trabajos en la cola
        self.__tiempo_espera_total = 0  # Tiempo total de espera de los trabajos procesados
        self.__trabajos_procesados = 0  # Cantidad de trabajos procesados

    def vacia(self):
        return self.__cant == 0

    def insertar(self, tiempo):
        nuevo_trabajo = Trabajo(tiempo)
        if self.__ul is None:  # Si la cola está vacía
            self.__pr = nuevo_trabajo
        else:
            self.__ul.cargar_sig(nuevo_trabajo)
        self.__ul = nuevo_trabajo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            return None
        else:
            trabajo = self.__pr
            self.__pr = self.__pr.obtener_sig()
            self.__cant -= 1
            if self.__pr is None:
                self.__ul = None
            return trabajo

    def procesar_trabajos(self, duracion_total):
        tiempo_transcurrido = 0
        while tiempo_transcurrido < duracion_total:
            if self.vacia():
                break
            trabajo_actual = self.suprimir()
            tiempo_impresion = trabajo_actual.obtener_tiempo()

            if tiempo_impresion > 5:
                # No se pudo terminar de imprimir el trabajo, se reencola con el tiempo restante
                self.insertar(tiempo_impresion - 5)
                tiempo_transcurrido += 5
            else:
                # Trabajo impreso completamente
                tiempo_transcurrido += tiempo_impresion
                self.__tiempo_espera_total += tiempo_transcurrido
                self.__trabajos_procesados += 1

    def trabajos_pendientes(self):
        return self.__cant

    def promedio_espera(self):
        if self.__trabajos_procesados == 0:
            return 0
        return self.__tiempo_espera_total / self.__trabajos_procesados

    def mostrar_estado(self):
        aux = self.__pr
        while aux is not None:
            print(f"Trabajo con {aux.obtener_tiempo()} minutos restantes.")
            aux = aux.obtener_sig()


# Ejemplo de uso
if __name__ == "__main__":
    cola = ColaImpresion()

    # Simulando llegada de trabajos cada 5 minutos (duración aleatoria entre 1 y 10 minutos)
    trabajos = [8, 3, 7, 2, 5, 6, 12, 4]  # Duraciones de los trabajos en minutos
    for tiempo in trabajos:
        cola.insertar(tiempo)

    print("Estado inicial de la cola de impresión:")
    cola.mostrar_estado()

    print("\nProcesando trabajos...")
    duracion_simulacion = 60  # Simulamos 60 minutos de tiempo total de la impresora
    cola.procesar_trabajos(duracion_simulacion)

    print("\nEstado final de la cola de impresión:")
    cola.mostrar_estado()

    # Resultados
    print(f"\nCantidad de trabajos que quedaron sin atender: {cola.trabajos_pendientes()}")
    print(f"Promedio de espera de los trabajos impresos: {cola.promedio_espera()} minutos")
