class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def e_simetrica(raiz):
    def e_espelhada(esq, dir):
        if esq is None and dir is None:
            return True

        if (
            esq is not None and
            dir is not None and
            esq.valor == dir.valor and
            e_espelhada(esq.esquerda, dir.direita) and
            e_espelhada(esq.direita, dir.esquerda)
        ):
            return True

        return False

    return e_espelhada(raiz, raiz)

arvore_simetrica = NoArvore(1)
arvore_simetrica.esquerda = NoArvore(2)
arvore_simetrica.direita = NoArvore(2)
arvore_simetrica.esquerda.esquerda = NoArvore(3)
arvore_simetrica.esquerda.direita = NoArvore(4)
arvore_simetrica.direita.esquerda = NoArvore(4)
arvore_simetrica.direita.direita = NoArvore(3)

simetrica = e_simetrica(arvore_simetrica)

if simetrica:
    print("A árvore é simétrica.")
else:
    print("A árvore não é simétrica.")
