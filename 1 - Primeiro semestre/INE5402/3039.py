a = int(input())
carrinhos = 0
bonecas = 0
for i in range(a):
    c = input().split()
    for i in range(len(c)):
        if c[i] == 'F':
            bonecas += 1
        if c[i] == 'M':
            carrinhos += 1
print("%d carrinhos" % (carrinhos))
print("%d bonecas" % (bonecas))
# a primeira entrada consiste do numero de crianças. as proximas entradas são
# os nomes e sexo biológico da criança. caso seja menino, adiciono 1 a variavel
# carrinhos, que representa o número de carrinhos que serão entregues pelo papai noel
# e caso seja menina, adiciono 1 a variavel bonecas, que representa o número de bonecas
# entregues pelo papai noel. ao final, printo o número de carrinhos e bonecas
# que serão entregues