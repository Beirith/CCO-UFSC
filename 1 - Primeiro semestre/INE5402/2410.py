n = int(input())
alunos = []
for i in range(n):
    h = int(input())
    alunos.append(h)
alunos = list(set(alunos))
print(len(alunos))