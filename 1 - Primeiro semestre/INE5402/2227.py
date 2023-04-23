teste = 0
while True:
    try:
        teste += 1
        a, v = input().split()
        a = int(a)
        v = int(v)
        l = []
        o = 0
        ii = 0
        if a == v == 0:
            print()
            break
        for i in range(a+1):
            l.append(0)
        for i in range(v):
            x, y = input().split()
            x = int(x)
            y = int(y)
            l[x] += 1
            l[y] += 1
        print("Teste %d" % (teste))
        for i in range(len(l)):
            if l[i] > o:
                o = l[i]
                l[i] = 0
                ii = i
        print(ii, end=" ")
        for i in range(len(l)):
            if l[i] == o:
                if i != len(l) - 1:
                    ii = i
                    print(ii, end=" ")
                elif i == len(l) - 1:
                    ii = i
                    print(ii)     
        print()             
    except EOFError:
        break