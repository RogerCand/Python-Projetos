class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def sao_arvores_identicas(raiz1, raiz2):
    if raiz1 is None and raiz2 is None:
        return True

    if raiz1 is None or raiz2 is None:
        return False

    return (
        raiz1.valor == raiz2.valor and
        sao_arvores_identicas(raiz1.esquerda, raiz2.esquerda) and
        sao_arvores_identicas(raiz1.direita, raiz2.direita)
    )

arvore1 = NoArvore(1)
arvore1.esquerda = NoArvore(2)
arvore1.direita = NoArvore(3)

arvore2 = NoArvore(1)
arvore2.esquerda = NoArvore(2)
arvore2.direita = NoArvore(3)

identicas = sao_arvores_identicas(arvore1, arvore2)

if identicas:
    print("As árvores são idênticas.")
else:
    print("As árvores não são idênticas.")
