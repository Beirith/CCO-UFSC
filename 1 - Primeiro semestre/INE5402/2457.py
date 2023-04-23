a = input()
b = input()
n = 1
rep = 0
letra = False

for i in range(len(b)):
    if b[i] == a:
        letra = True
    if b[i] == " ":
        n += 1
        if letra ==  True:
            rep += 1
            letra = False
if letra == True:
    rep += 1
porcentagem = rep / n
print("%.1f" % (porcentagem * 100))