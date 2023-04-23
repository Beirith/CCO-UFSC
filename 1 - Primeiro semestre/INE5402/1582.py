while True:
    try:
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)

        aa = a
        bb = b
        cc = c

        def mdc(z,h):
            while h !=0:
                resto = z % h
                z = h
                h = resto
            return z

        def tripla(a, b, c, cc, bb, aa):
            if c * c == a * a + b* b:
                if mdc(b,a) == 1 and mdc(c,aa) == 1 and mdc(cc,bb) == 1:
                    print("tripla pitagorica primitiva")
                else:
                    print("tripla pitagorica")
            else:
                print("tripla")
        
        tripla(a, b, c, cc, bb, aa)

    except EOFError:
        break