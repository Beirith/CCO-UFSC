a = int(input())
brinquedos = 0
b = 0 # numero de horas trabalhadas na equipe dos bonecos
ar = 0 # numero de horas trabalhadas na equipe dos arquitetos
m = 0 # numero de horas trabalhadas na equipe dos musicos
d = 0 # numero de horas trabalhadas na equipe dos desnhistas
for i in range(a):
    h = input().split()
    for i in range(len(h)):
         h[2] = int(h[2])
         if h[i] == "bonecos":
             b += h[2]
         if h[i] == "arquitetos":
             ar += h[2]
         if h[i] == "musicos":
             m += h[2]
         if h[i] == "desenhistas":
             d += h[2]
brinquedos = b//8 + ar//4 + m//6 + d//12
print(brinquedos)

# a primeira entrada a consiste do numero de elfos. as outras a entradas
# são relacionadas ao nomes, grupos e horas de trabalho dos elfos. 
# somando as horas trabalhadas em cada equipe, e dividindo pelo número de horas
# necessárias para produzir um presente respectivo de cada grupo, se obtém o número de presentes
# ao somar todos os números de presentes, obtemos a resposta final, que foi armazenada na ]
# variável brinquedos.
