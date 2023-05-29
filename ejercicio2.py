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

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

while not pila.esta_vacia():
    elemento = pila.desapilar()
    print("Desapilando:", elemento)
