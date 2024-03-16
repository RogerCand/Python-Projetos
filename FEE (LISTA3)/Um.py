class NoFila:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, dado):
        novo_no = NoFila(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return None
        else:
            dado_removido = self.inicio.dado
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            return dado_removido

    def imprimir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

fila = Fila()

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print("Fila original:")
fila.imprimir()

elemento_removido = fila.desenfileirar()
print(f"Elemento removido: {elemento_removido}")

print("\nFila após remoção:")
fila.imprimir()
