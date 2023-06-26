# Função que divide o tabuleiro em colunas.
def divideColunas(tabuleiro):
    colunas = []
    for i in range(9):
        celulas = []
        for j in range(9):
            celulas.append(tabuleiro[j][i])
        colunas.append(celulas)
    return colunas    

# Função que divide o tabuleiro em regiões.
def divideRegioes(tabuleiro):
    regioes = []
    for i in range(3):
        for j in range(3):
            celulas = []
            for k in range(3):
                for l in range(3):
                    celulas.append(tabuleiro[i*3+k][j*3+l])
            regioes.append(celulas)
    return regioes
            
def verificaRepeticao(array, local):
    errosEncontrados = ''
    if isinstance(array, str):
        array_aux = array
        array = ''.join(sorted(array_aux))
    else:
        array.sort()
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            errosEncontrados += local + f'{i+1}'
            break
    return errosEncontrados

def validaTabuleiro(processID, tabuleiros, numThreads):



    errosTabuleiro = {}
    errosTabuleiro[processID] = []

    for tabuleiro in tabuleiros:
        colunas = divideColunas(tabuleiro)
        regioes = divideRegioes(tabuleiro)

        for i in range(9):
            errosTabuleiro[processID].append(verificaRepeticao(colunas[i], 'C'))
            errosTabuleiro[processID].append(verificaRepeticao(regioes[i], 'R'))
            errosTabuleiro[processID].append(verificaRepeticao(tabuleiro[i], 'L'))
        
    errosTabuleiro[processID] = [item for item in errosTabuleiro[processID] if item != '']
    print(errosTabuleiro)

