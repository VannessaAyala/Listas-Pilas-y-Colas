class Cola:
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        return len(self.cola) == 0

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.cola.pop(0)


# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

while not cola.esta_vacia():
    elemento = cola.desencolar()
    print("Desencolando:", elemento)
