while True:
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        
        if n == 0 and m == 0:
            break
        
        l = []
        lp = [0] * m
        cond1 = True
        cond2 = True
        cond3 = True
        cond4 = True
        ncond = 0
        
        
        for i in range(n):
            x = input().split()
            l.append(x)
            
            
        for i in range(len(l)):
            n1 = 0
            for j in range(m):
                l[i][j] = int(l[i][j])
                if l[i][j] == 1:
                    n1 += 1
                    lp[j] += 1
            if n1 == m:
                cond1 = False
            if n1 == 0:
                cond4 = False
                
                
        for i in range(len(lp)):
            if lp[i] == n:
                cond3 = False
            if lp[i] == 0:
                cond2 = False
                
                
        if cond1 == True:
            ncond += 1
        if cond2 == True:
            ncond += 1
        if cond3 == True:
            ncond += 1
        if cond4 == True:
            ncond += 1

        print(ncond)

    except EOFError:
        break