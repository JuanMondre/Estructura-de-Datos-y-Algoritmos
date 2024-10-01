"""class PilaSecuencial:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.capacidad

    def insertar(self, item):
        if not self.esta_llena():
            self.items.append(item)

    def suprimir(self):
        if not self.esta_vacia():
            return self.items.pop()

    def mostrar(self):
        return self.items

    def tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None


def mostrar_estado(pilas):
    for i in range(3):
        print(f"Pila {i + 1}: {pilas[i].mostrar()}")
    print("=" * 40)


def movimiento_valido(origen, destino, pilas):
    if pilas[origen].esta_vacia():
        print("La pila origen está vacía. Movimiento no válido.")
        return False
    if not pilas[destino].esta_vacia() and pilas[destino].tope() < pilas[origen].tope():
        print("No se puede mover un disco grande sobre uno pequeño. Movimiento no válido.")
        return False
    return True


def mover_disco(origen, destino, pilas):
    if movimiento_valido(origen, destino, pilas):
        disco = pilas[origen].suprimir()
        pilas[destino].insertar(disco)
        return True
    return False


def juego_torres_de_hanoi(num_discos):
    # Crear las tres pilas
    pilas = [PilaSecuencial(num_discos) for _ in range(3)]

    # Inicializar la primera pila con los discos
    for i in range(num_discos, 0, -1):
        pilas[0].insertar(i)

    print("Estado inicial:")
    mostrar_estado(pilas)

    jugadas = 0
    while len(pilas[2].mostrar()) != num_discos:
        try:
            origen = int(input("Ingrese la pila de origen (1, 2, 3): ")) - 1
            destino = int(input("Ingrese la pila de destino (1, 2, 3): ")) - 1

            if origen in [0, 1, 2] and destino in [0, 1, 2]:
                if mover_disco(origen, destino, pilas):
                    jugadas += 1
                    mostrar_estado(pilas)
                else:
                    print("Movimiento no válido. Intente nuevamente.")
            else:
                print("Entrada inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    print(f"¡Juego terminado en {jugadas} jugadas!")


if __name__ == "__main__":
    num_discos = int(input("Ingrese el número de discos: "))
    juego_torres_de_hanoi(num_discos)
"""

class PilaSecuencial:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad

    def esta_vacia(self):
        return not self.items

    def esta_llena(self):
        return len(self.items) >= self.capacidad

    def insertar(self, item):
        if not self.esta_llena():
            self.items.append(item)

    def suprimir(self):
        if not self.esta_vacia():
            return self.items.pop()

    def mostrar(self):
        return self.items

    def tope(self):
        return self.items[-1] if not self.esta_vacia() else None


def mostrar_estado(pilas):
    for idx, pila in enumerate(pilas, 1):
        print(f"Pila {idx}: {pila.mostrar()}")
    print("=" * 40)


def movimiento_valido(origen, destino, pilas):
    if pilas[origen].esta_vacia():
        print("La pila origen está vacía. Movimiento no válido.")
        return False
    if not pilas[destino].esta_vacia() and pilas[destino].tope() < pilas[origen].tope():
        print("No se puede mover un disco grande sobre uno pequeño. Movimiento no válido.")
        return False
    return True


def mover_disco(origen, destino, pilas):
    if movimiento_valido(origen, destino, pilas):
        disco = pilas[origen].suprimir()
        pilas[destino].insertar(disco)
        return True
    return False


def juego_torres_de_hanoi(num_discos):
    pilas = [PilaSecuencial(num_discos) for _ in range(3)]
    pilas[0].items = list(range(num_discos, 0, -1))

    print("Estado inicial:")
    mostrar_estado(pilas)

    jugadas = 0
    while len(pilas[2].mostrar()) != num_discos:
        try:
            origen = int(input("Ingrese la pila de origen (1, 2, 3): ")) - 1
            destino = int(input("Ingrese la pila de destino (1, 2, 3): ")) - 1

            if 0 <= origen < 3 and 0 <= destino < 3:
                if mover_disco(origen, destino, pilas):
                    jugadas += 1
                    mostrar_estado(pilas)
                else:
                    print("Movimiento no válido. Intente nuevamente.")
            else:
                print("Pilas deben ser 1, 2 o 3. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números enteros.")

    print(f"¡Juego terminado en {jugadas} jugadas!")


if __name__ == "__main__":
    try:
        num_discos = int(input("Ingrese el número de discos: "))
        if num_discos < 1:
            print("Debe haber al menos un disco.")
        else:
            juego_torres_de_hanoi(num_discos)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
