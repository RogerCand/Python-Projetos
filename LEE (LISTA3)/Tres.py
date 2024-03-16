class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self, dado):
        atual = self.cabeca
        anterior = None

        while atual:
            if atual.dado == dado:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return  # Encontrou e removeu o nó
            anterior = atual
            atual = atual.proximo

    def buscar(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dado == dado:
                return True  # Encontrou o dado na lista
            atual = atual.proximo
        return False  # Não encontrou o dado na lista

    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" → ")
            atual = atual.proximo
        print("None")

minha_lista = Lista()

minha_lista.inserir(0)
minha_lista.inserir(1)
minha_lista.inserir(1)
minha_lista.inserir(5)
minha_lista.inserir(7)
minha_lista.inserir(10)
minha_lista.inserir(10)

print("Lista original:")
minha_lista.imprimir()

minha_lista.remover(1)
minha_lista.remover(7)

print("\nLista após remoção:")
minha_lista.imprimir()

elemento_buscar = 5
if minha_lista.buscar(elemento_buscar):
    print(f"\nO elemento {elemento_buscar} foi encontrado na lista.")
else:
    print(f"\nO elemento {elemento_buscar} não foi encontrado na lista.")
