a = int(input())
b = input().split()
x = 0
l = []
for i in range(a):
    l.append(0)
    
for i in range(a - 1):
    b[i] = int(b[i])
    x = b[i] - 1
    l[x] = b[i]

for i in range(len(l)):
    if l[i] == 0:
        print("%d" % (i + 1))
        
# o vetor l possui o tamanho do número de peças completas, porém inicialmente, possui todos os elementos com valor zero.
# em seguida, adiciono o valor da peça no vetor l, na posição de seu mesmo valor menos 1 (de modo que o valor fique na posição correta)
# substituindo o valor zero pelo número da peça.
# após iso, percorro o vetor l e procuro por um elemento com número zero, que seria a peça faltando.
# com isso, basta printar o índice do valor zero, que é exatamente o número que está em falta, pois o número da peça é igual a sua 
# posição no vetor l.