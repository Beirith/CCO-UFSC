a, b = input().split()
a = int(a)
b = int(b)

abx = False
aci = False
esq = False
diq = False

x, y = input().split()
x = int(x) - 1
y = int(y) - 1

l = [None] * a

for i in range(a):
    h = input().split()
    l[i] = h

for i in range(a):
    for j in range(b):
        abaixo = x + 1
        acima = x - 1
        esquerda = y - 1
        direita = y + 1

        if abaixo < a and l[abaixo][y] == '1' and x != acima:
            x = abaixo
                    
        if acima >= 0 and l[acima][y] == '1' and x != abaixo:
            x = acima
            
        if esquerda >= 0 and l[x][esquerda] == '1' and y != direita:
            y = esquerda
                    
        if direita < b and l[x][direita] == '1' and y != esquerda:
            y = direita

print("%d %d" % (x, y))