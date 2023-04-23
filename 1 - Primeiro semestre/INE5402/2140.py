while True:    
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        troco = m - n
        notas = [100, 50, 20, 10, 5, 2]
        operation = 0
        
        def trocos(m,n,notas,troco, operation):            
            for i in range(len(notas)):
                if troco >= notas[i]:
                    if troco % notas[i] == 0:
                        if operation == 1:
                            return print("possible")
                    elif troco % notas[i] != 0:
                        troco = troco % notas[i]
                        operation += 1
            print("impossible")
            
        if n == m == 0:
            break
        
        trocos(m, n, notas, troco, operation)
        
    except EOFError:
        break