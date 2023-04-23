n = int(input())
l = []
m2 = 0
m3 = 0
m4 = 0
m5 = 0
b = input().split()
for i in range(len(b)):
    b[i] = int(b[i])
    l.append(b[i])
for i in range(len(l)):
    if l[i] % 2 == 0:
        m2 += 1
    if l[i] % 3 == 0:
        m3 += 1
    if l[i] % 4 == 0:
        m4 += 1
    if l[i] % 5 == 0:
        m5 += 1
print("%d Multiplo(s) de 2" % (m2))
print("%d Multiplo(s) de 3" % (m3))
print("%d Multiplo(s) de 4" % (m4))
print("%d Multiplo(s) de 5" % (m5))