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


def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        letra = pila.desapilar()
        palabra_invertida += letra

    return palabra == palabra_invertida


# Ejemplo de uso
palabra_1 = "radar"
palabra_2 = "python"

if es_palindromo(palabra_1):
    print(palabra_1, "es un palíndromo.")
else:
    print(palabra_1, "no es un palíndromo.")

if es_palindromo(palabra_2):
    print(palabra_2, "es un palíndromo.")
else:
    print(palabra_2, "no es un palíndromo.")
