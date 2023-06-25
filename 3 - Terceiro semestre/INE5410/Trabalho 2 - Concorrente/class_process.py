import multiprocessing
import threading

class Processo():
    def __init__(self, nome, nThreads, tabuleiros):
        self.nome = nome
        self.nThreads = nThreads
        self.tabuleiros = tabuleiros
        self.processo = None
        self.erros = {}	

    def validaLinha(self):
        for tabuleiro in self.tabuleiros:
            errosTabuleiro = []
            for i in range(9):
                celulas_aux = self.tabuleiros[tabuleiro][i]
                celulas = ''.join(sorted(celulas_aux))
                for j in range(len(celulas)-1):
                    if celulas[j] == celulas[j+1]:
                        errosTabuleiro.append(f'L{i+1}')
                        break
                self.erros[tabuleiro] = errosTabuleiro
            
            
    def validaColuna(self):
        for tabuleiro in self.tabuleiros:
            errosTabuleiro = []
            for i in range(9):
                celulas = []
                for j in range(9):
                    celulas.append(self.tabuleiros[tabuleiro][j][i])
                celulas.sort()
                for j in range(len(celulas)-1):
                    if celulas[j] == celulas[j+1]:
                        errosTabuleiro.append(f'C{i+1}')
                        break
                self.erros[tabuleiro] = errosTabuleiro
    
    def validaRegiao(self):
        for tabuleiro in self.tabuleiros:
            errosTabuleiro = []
            for i in range(9):
                celulas = []
                for j in range(3):
                    for k in range(3):
                        celulas.append(self.tabuleiros[tabuleiro][j][k])
                celulas.sort()
                for j in range(len(celulas)-1):
                    if celulas[j] == celulas[j+1]:
                        errosTabuleiro.append(f'C{i+1}')
                        break
                self.erros[tabuleiro] = errosTabuleiro
        print(self.erros)

    def criaThreads(self):
        for i in range(self.nThreads):
            thread = threading.Thread(target=self.validaColuna)
            thread.start()
    
    def criaProcesso(self):
        self.processo = multiprocessing.Process(target=self.validaColuna)

    def printProcesso(self):
        print(self.nome)
        for tabuleiro in self.tabuleiros:
            print("Tabuleiro %d" % (tabuleiro))
            for linha in self.tabuleiros[tabuleiro]:
                print(linha)
            print("\n")