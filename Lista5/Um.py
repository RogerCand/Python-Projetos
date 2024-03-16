class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_menor_elemento(no):
    while no.esquerda is not None:
        no = no.esquerda

    return no.valor

raiz = NoArvore(10)
raiz.esquerda = NoArvore(6)
raiz.direita = NoArvore(18)
raiz.esquerda.esquerda = NoArvore(5)
raiz.esquerda.direita = NoArvore(9)

menor_elemento = encontrar_menor_elemento(raiz)

print(f"O menor elemento na BST é: {menor_elemento}")
