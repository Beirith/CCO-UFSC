while True:
    try:
        a = int(input())
        caso = 0
        for i in range(a):
            m, n, x, y = input().split()
            caso += 1
            m = int(m)
            n = int(n)
            x = int(x)
            y = int(y)
            parede = [None] * m
            for i in range(m):
                parede[i] = input().split

            for i in range(m):
                for j in range(n):
                    abaixo = x + 1
                    acima = x - 1
                    esquerda = y - 1
                    direita = y + 1

                    parede[i][j] = int(parede[i][j])
                    parede[x][y] = 10
                    parede[x][y] = 10


                    

            



    



    except EOFError:
        break