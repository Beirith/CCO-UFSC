from multiprocessing import Process
import threading
import time
import sys

def validaEntrada():
    while True:
        # Entrada do usuário, utilizada para abrir o arquivo e definir o número de processos e threads.
        entry = input('Digite o nome do arquivo, o número de processos e o número de threads: ').split()

        # O número de argumentos passados na entrada deve ser igual a 3.
        if len(entry) != 3:
            print('Erro! Você deve digitar <nome do arquivo de entrada> <número de processos> <número de threads>!')
            print()
            continue
        
        # Caso o número de argumentos seja 3, verifica se o nome do arquivo é válido.
        else:
            nome = entry[0]
            nProcess = entry[1]
            nThread = entry[2]

            try:
                file = open(nome)
                file.close()
            except FileNotFoundError:
                print('Erro! Arquivo não existe!')
                print('Você deve digitar o nome do arquivo de entrada com a extensão .txt!')
                print()
                continue

            # Verifica se o número de processos e threads é um inteiro positivo.
            if not nProcess.isdigit() or not nThread.isdigit():
                print('Erro! O número de processos e o número de threads devem ser inteiros positivos!')
                print()
                continue

            # Verifica se o número de processos e threads é maior do que zero.
            elif (int(nProcess) < 1) or (int(nThread) < 1):
                print("ERRO! O número de processos e o número de threads devem ser maiores que zero!")
                print()

            else:
                return entry

def lerArquivo(nome):
    with open(nome, 'r') as file:
        lista = []
        tabuleiros = []
        contador = 0

        # Lê o arquivo e armazena o conteúdo em uma lista.
        for linha in file:
            if linha != '\n':
                lista.append(linha.strip())
                contador += 1
            
            if contador == 9:
                tabuleiros.append(lista)
                contador = 0
                lista = []
    
    return tabuleiros
          
def dividirTrabalho(nProcess, nThread, tabuleiros):
    for i in range(nProcess):
        # Cria um processo e atribui a ele uma função e os argumentos que serão passados para a função.
        p = multiprocessing.Process(target=verificaErro, args=(nThread, tabuleiros[i]))
        p.start()
    pass

def verificaErro():
    pass

def main():
    # Chama a função que valida a entrada do usuário e atribui os valores de retorno as variáveis.
    argumentos = validaEntrada()
    nome = argumentos[0]
    nProcess = int(argumentos[1])
    nThread = int(argumentos[2])

    # Lê o arquivo e armazena o conteúdo em uma lista, que contém todos os tabuleiros.
    tabuleiros = lerArquivo(nome)

    # Para que não hajam processos ociosos, o número de processos é limitado pelo número de tabuleiros.
    if len(tabuleiros) > nProcess:
        nProcess = len(tabuleiros)

    dividirTrabalho(nProcess, nThread, tabuleiros)
    verificaErro()

if __name__ == '__main__':
    main()

    #Teste

