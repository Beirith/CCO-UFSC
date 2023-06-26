import threading

# Função que divide o tabuleiro em colunas.
def divideColunas(tabuleiro):
    for i in range(9):
        celulas = []
        for j in range(9):
            celulas.append(tabuleiro[j][i])
        tabuleiro.append(celulas)
    return tabuleiro    

# Função que divide o tabuleiro em regiões.
def divideRegioes(tabuleiro):
    for i in range(3):
        for j in range(3):
            celulas = []
            for k in range(3):
                for l in range(3):
                    celulas.append(tabuleiro[i*3+k][j*3+l])
            tabuleiro.append(celulas)
    return tabuleiro

# Função que verifica se há repetições em determinado espaço.
def verificaRepeticao(array):
    if isinstance(array, str):
        array_aux = array
        array = ''.join(sorted(array_aux))
    else:
        array.sort()

    for i in range(len(array)-1):
            if array[i] == array[i+1]:
                return True
    
    return False


def rotinaThread(*args):
    erros = []
    for i in range(len(args)):
        tipo = args[i][0]
        num = args[i][1]
        array = args[i][3]

        if verificaRepeticao(array):
            erros.append(f"{tipo}{num}")
    #print(erros)

    # # Indicia se é coluna, linha ou região
    # tipo = args[0]

    # # Indicia o número da coluna, linha ou região
    # num = args[1]

    # # Array de erros
    # erros = args[2]

    # # Array de células que serão verificadas
    # array = args[3]

def validaTabuleiro(processID, tabuleiros, numThreads, idTabuleiros, barreira,
                    lock):

    for i in range(len(tabuleiros)):
        with lock:
            print('Processo ', processID, ': resolvendo quebra-cabeças: ', 
                  idTabuleiros[i])

        threadArgs = []
        threads = []
        erros = []
        for l in range(numThreads): threadArgs.append([])

        tabuleiros[i] = divideColunas(tabuleiros[i])
        tabuleiros[i] = divideRegioes(tabuleiros[i])

        for j in range(len(tabuleiros[i])):
            array = tabuleiros[i][j]
            if j < 9:
                threadArgs[j % numThreads].append(['L', (j%9)+1, erros, array])
            elif j < 18:
                threadArgs[j % numThreads].append(['C', (j%9)+1, erros, array])
            else:
                threadArgs[j % numThreads].append(['R', (j%9)+1, erros, array])

        for k in range(numThreads):
            thread = threading.Thread(target=rotinaThread, args=threadArgs[k])
            threads.append(thread)

        
        for z in range(numThreads):
            threads[z].start()

        for z in range(numThreads):
            threads[z].join()
            