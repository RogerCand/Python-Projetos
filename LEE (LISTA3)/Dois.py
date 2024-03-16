class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def remove_duplicatas(cabeca):
    atual = cabeca
    anterior = None

    while atual:
        if anterior and anterior.dado == atual.dado:
            anterior.proximo = atual.proximo
            atual = atual.proximo
        else:
            anterior = atual
            atual = atual.proximo

    return cabeca

def imprimir_lista(cabeca):
    atual = cabeca
    while atual:
        print(atual.dado, end=" → ")
        atual = atual.proximo
    print("None")

cabeca = No(0)
cabeca.proximo = No(1)
cabeca.proximo.proximo = No(1)
cabeca.proximo.proximo.proximo = No(5)
cabeca.proximo.proximo.proximo.proximo = No(7)
cabeca.proximo.proximo.proximo.proximo.proximo = No(10)
cabeca.proximo.proximo.proximo.proximo.proximo.proximo = No(10)

print("Lista original:")
imprimir_lista(cabeca)

cabeca = remove_duplicatas(cabeca)

print("\nLista sem duplicatas:")
imprimir_lista(cabeca)
