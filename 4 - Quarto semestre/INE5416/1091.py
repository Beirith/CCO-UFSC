while True:
    try:
        n = int(input())
        x, y = input().split()
        x = int(x)
        y = int(y)

        for i in range(n):
            x1, y1 = input().split()
            x1 = int(x1)
            y1 = int(y1)

            if (x1 == x) or (y1 == y):
                print("divisa")
                continue
            
            if (x1 > x):
                if (y1 > y): print("NE")
                else: print("SE")
                continue

            else:
                if (y1 > y): print("NO")
                else: print("SO")
                continue
    
    except EOFError:
        break
