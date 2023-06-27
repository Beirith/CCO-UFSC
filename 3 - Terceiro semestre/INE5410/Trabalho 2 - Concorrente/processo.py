import threading

# Função que divide o tabuleiro em colunas.
def divideTabuleiro(tabuleiro):
    for i in range(9):
        celulas = []
        for j in range(9):
            celulas.append(tabuleiro[j][i])
        tabuleiro.append(celulas)
    
    for i in range(3):
        for j in range(3):
            celulas = []
            for k in range(3):
                for l in range(3):
                    celulas.append(tabuleiro[i*3+k][j*3+l])
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
    for i in range(len(args)):
        tipo = args[i][0]
        num = args[i][1]
        array = args[i][3]

        if verificaRepeticao(array):
            errosTabuleiro[args[i][2]].append(f"{tipo}{num}")
            errosTabuleiro['quantidade'].append(1)
        
def validaTabuleiro(processID, tabuleiros, numThreads, idTabuleiros, barreira,
                    lock):
    global errosTabuleiro

    for i in range(len(tabuleiros)):
        with lock:
            print('Processo %d: resolvendo quebra-cabeças %d' % (processID, idTabuleiros[i]))

        threadArgs = []
        threads = []
        errosTabuleiro = {'quantidade': []}
        for l in range(numThreads): 
            threadArgs.append([]) 
            errosTabuleiro[l+1] = []

        tabuleiros[i] = divideTabuleiro(tabuleiros[i])

        for j in range(len(tabuleiros[i])):
            array = tabuleiros[i][j]
            if j < 9:
                threadArgs[j % numThreads].append(['L', (j%9)+1, (j % numThreads)+1, array])
            elif j < 18:
                threadArgs[j % numThreads].append(['C', (j%9)+1, (j % numThreads)+1, array])
            else:
                threadArgs[j % numThreads].append(['R', (j%9)+1, (j % numThreads)+1, array])

        for k in range(numThreads):
            thread = threading.Thread(target=rotinaThread, args=threadArgs[k])
            threads.append(thread)

        for z in range(numThreads):
            threads[z].start()

        for z in range(numThreads):
            threads[z].join()
        

        print('Processo %d: %d erros encontrados' % (processID, len(errosTabuleiro['quantidade'])), end=' ')
        if len(errosTabuleiro['quantidade']) == 0:
            print()
            break
        else:
            errosTabuleiro.pop('quantidade')
            print('(', end='')
            for thread in errosTabuleiro:
                if errosTabuleiro[thread] == []:
                    continue

                print('T%d:' % thread, end=' ')
                if errosTabuleiro[thread] != []:
                    for i in range(len(errosTabuleiro[thread])):
                        if i == len(errosTabuleiro[thread])-1:
                            print(f'{errosTabuleiro[thread][i]};', end=' ')
                        else:
                            print(f'{errosTabuleiro[thread][i]},', end=' ')
        print(')')