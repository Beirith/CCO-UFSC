n = int(input())
l = []
l1 = []

def aparece(l1,l):
    for i in range (len(l1)):
        rep = l.count(l1[i])
        print("%d aparece %d vez(es)" % (l1[i], rep))
                                    
for i in range(n):
    x = int(input())
    l.append(x)
    if x not in l1:
        l1.append(x)
        l1.sort()

aparece(l1,l)