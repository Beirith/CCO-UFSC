m = [None] * 12
for i in range(len(m)):
    m[i] = [None] * 12

b = int(input())
o = input()
x = 0

for i in range(0,12):
    for j in range(0,12):
        a = float(input())
        m[i][j] = a

for i in range(0,12):
    for j in range(0,12):
        if i == b:
            x = x + m[i][j]

if o == 'S':
    print("%.1f" % (x))

if o == 'M':
    print("%.1f" % (x/12))