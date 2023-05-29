class Pila:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.pila.pop()


def es_simetrica(lista):
    pila = Pila()
    mitad = len(lista) // 2

    # Apilar la primera mitad de la lista
    for i in range(mitad):
        pila.apilar(lista[i])

    # Comparar con la segunda mitad de la lista
    for i in range(mitad, len(lista)):
        if lista[i] != pila.desapilar():
            return False

    return True


# Ejemplo de uso
lista_1 = [1, 2, 3, 2, 1]
lista_2 = [1, 2, 3, 4, 5]

if es_simetrica(lista_1):
    print("La lista 1 es simétrica.")
else:
    print("La lista 1 no es simétrica.")

if es_simetrica(lista_2):
    print("La lista 2 es simétrica.")
else:
    print("La lista 2 no es simétrica.")
