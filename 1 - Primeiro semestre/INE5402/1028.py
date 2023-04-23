a = int(input())

def mdc(z,h):
    while h !=0:
        resto = z % h
        z = h
        h = resto
    return z

for i in range(a):
    x, y = input().split()
    x = int(x)
    y = int(y)

    print(mdc(x,y))