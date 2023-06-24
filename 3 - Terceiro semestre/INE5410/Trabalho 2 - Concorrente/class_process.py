class Processo():
    def __init__(self, nome, nThreads, tabuleiros):
        self.nome = nome
        self.nThreads = nThreads
        self.tabuleiros = tabuleiros

    def inciaProcesso(self):
        pass

    def printProcesso(self):
        print(self.nome)
        print(self.nThreads)
        print(self.tabuleiros)
        print("\n")