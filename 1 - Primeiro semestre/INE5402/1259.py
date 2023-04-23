n = int(input())

pares = []
impares = []

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

pares.sort()
impares.sort(reverse=True)

for i in range(len(pares)):
    print(pares[i])
for i in range(len(impares)):
    print(impares[i])
