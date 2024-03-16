def busca(elemento, lista):
    """Função para buscar um elemento em uma lista."""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def remove(elemento, lista):
    """Função para remover um elemento de uma lista utilizando a função busca."""
    indice = busca(elemento, lista)

    if indice != -1:
        del lista[indice]
        print(f"Elemento {elemento} removido com sucesso.")
    else:
        print(f"Elemento {elemento} não encontrado na lista.")


minha_lista = [1, 2, 3, 4, 5]
elemento_a_remover = 3

remove(elemento_a_remover, minha_lista)
print("Lista atualizada:", minha_lista)
