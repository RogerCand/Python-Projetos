class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def calcular_altura(raiz):
    if raiz is None:
        return -1

    altura_esquerda = calcular_altura(raiz.esquerda)
    altura_direita = calcular_altura(raiz.direita)

    return max(altura_esquerda, altura_direita) + 1

raiz = NoArvore(10)
raiz.esquerda = NoArvore(5)
raiz.direita = NoArvore(15)
raiz.esquerda.esquerda = NoArvore(3)
raiz.esquerda.direita = NoArvore(7)

altura = calcular_altura(raiz)

print(f"A altura da BST é: {altura}")
