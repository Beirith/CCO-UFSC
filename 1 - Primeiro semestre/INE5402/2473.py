a = input().split()
x = input().split()
acertos = 0
for i in range(len(a)):
    for p in range(len(x)):
        if a[i] == x[p]:
            acertos += 1
if acertos == 3:
    print("terno") 
if acertos == 4:
    print("quadra") 
if acertos == 5:
    print("quina")  
if acertos == 6:
    print("sena")
if acertos < 3:
    print("azar")
# a primeira entrada consiste dos numeros apostados por
# flavinho. a segunda entrada são os número sorteados. percorro
# a aposta de pedrinho (a) e, percorrendo a aposta de pedrinho,
# percorro os números sorteados (x), para descobrir se existe algum número no vetor de números
# sorteados (x) que seja igual ao primeiro número a[i] do vetor a. caso exista algum número igual
# somo 1 ao valor da variavel acertos, que corresponde ao número de acertos de pedrinho.
# ao final, analiso o valor da variavel acertos e printo a mensagem correspondente a cada número de acertos.

