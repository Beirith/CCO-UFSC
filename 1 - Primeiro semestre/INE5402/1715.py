a, b = input().split()
a = int(a)
b = int(b)

x = 0
jogadores = 0

l = [None] * a

for i in range(a):
    h = input().split()
    for f in range(len(h)):
        if h[f] != '0':
            x += 1
    if x == b:
        jogadores += 1
        x = 0
    else:
        x = 0

print(jogadores)           