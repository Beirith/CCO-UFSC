a = input()
a = list(a)
l = []
z = 0
for i in range(len(a)):
    z += 1
    if z % 2 == 0:
        l.append(a[i])
    if a[i] == " ":
        z = 0
        l.append(a[i])
for i in range(len(l)):
    print(l[i],end="")
print()
print()