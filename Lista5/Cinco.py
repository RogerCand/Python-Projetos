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

def verificar_balanceamento(raiz):

    if raiz is None:
        return True

    altura_esquerda = calcular_altura(raiz.esquerda)
    altura_direita = calcular_altura(raiz.direita)

    if abs(altura_esquerda - altura_direita) <= 1 and verificar_balanceamento(raiz.esquerda) and verificar_balanceamento(raiz.direita):
        return True

    return False

arvore_balanceada = NoArvore(1)
arvore_balanceada.esquerda = NoArvore(2)
arvore_balanceada.direita = NoArvore(3)
arvore_balanceada.esquerda.esquerda = NoArvore(4)
arvore_balanceada.esquerda.direita = NoArvore(5)

balanceada = verificar_balanceamento(arvore_balanceada)

if balanceada:
    print("A árvore é balanceada.")
else:
    print("A árvore não é balanceada.")
