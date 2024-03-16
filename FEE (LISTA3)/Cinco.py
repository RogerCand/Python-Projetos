class Processo:
    def __init__(self, id_processo, tempo_espera):
        self.id_processo = id_processo
        self.tempo_espera = tempo_espera

class NoFila:
    def __init__(self, processo):
        self.processo = processo
        self.proximo = None

class FilaProcessos:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def incluir_processo(self, processo):
        novo_no = NoFila(processo)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def matar_maior_tempo_espera(self):
        if self.esta_vazia():
            print("A fila de processos está vazia.")
        else:
            maior_tempo_espera = 0
            no_anterior = None
            atual = self.inicio

            while atual:
                if atual.processo.tempo_espera > maior_tempo_espera:
                    maior_tempo_espera = atual.processo.tempo_espera
                    no_anterior = no_anterior
                no_anterior = atual
                atual = atual.proximo

            if no_anterior:
                no_anterior.proximo = no_anterior.proximo.proximo
                if no_anterior.proximo is None:
                    self.fim = no_anterior
                print(f"Processo {maior_tempo_espera} removido (tempo de espera: {maior_tempo_espera}).")
            else:
                self.inicio = self.inicio.proximo
                if self.inicio is None:
                    self.fim = None
                print(f"Processo {maior_tempo_espera} removido (tempo de espera: {maior_tempo_espera}).")

    def executar_processo(self):
        if self.esta_vazia():
            print("A fila de processos está vazia.")
        else:
            processo_executado = self.inicio.processo
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            print(f"Executando o Processo {processo_executado.id_processo} (tempo de espera: {processo_executado.tempo_espera}).")

    def imprimir_processos(self):
        if self.esta_vazia():
            print("A fila de processos está vazia.")
        else:
            atual = self.inicio
            while atual:
                print(f"Processo {atual.processo.id_processo} (Tempo de Espera: {atual.processo.tempo_espera})", end=" -> ")
                atual = atual.proximo
            print("None")

fila_processos = FilaProcessos()

fila_processos.incluir_processo(Processo(1, 5))
fila_processos.incluir_processo(Processo(2, 8))
fila_processos.incluir_processo(Processo(3, 3))

print("Fila de Processos:")
fila_processos.imprimir_processos()

fila_processos.matar_maior_tempo_espera()

print("\nFila de Processos após remoção:")
fila_processos.imprimir_processos()

fila_processos.executar_processo()

print("\nFila de Processos após execução:")
fila_processos.imprimir_processos()
