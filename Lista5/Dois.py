class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_maior_elemento(no):
    while no.direita is not None:
        no = no.direita

    return no.valor

raiz = NoArvore(10)
raiz.esquerda = NoArvore(11)
raiz.direita = NoArvore(16)
raiz.esquerda.esquerda = NoArvore(3)
raiz.esquerda.direita = NoArvore(7)

maior_elemento = encontrar_maior_elemento(raiz)

print(f"O maior elemento na BST é: {maior_elemento}")
