a, b = input().split()
a = int(a)
b = int(b)
assiduos = 0
alunos = input().split()
for i in range(len(alunos)):
    alunos[i] = int(alunos[i])
    if alunos[i] <= 0:
        assiduos += 1
if assiduos >= b:
    print("YES")
else:
    print("NO")
# transformo os alunos da sala em um veto. ao percorre-lo, procuro por valores menores ou iguais a 0
# e adiono 1 ao valor da varíavel assiduos, que representa o número de alunos que chegam no horário
# na sala de aula. caso o valor da variavel assiduos seja maior ou igual a b (que representa
# o número mínimo de alunos assiduos para o treinamento ser realizado), é printado "YES", caso
# contrário, será printado "NO".
    
    
    