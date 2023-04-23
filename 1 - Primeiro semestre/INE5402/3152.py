terra = 0
for i in range(2):
    terra += 1
    la = []
    lb = []

    for i in range(4):
        a, b = input().split()
        a = int(a)
        b = int(b)

        la.append(a)
        lb.append(b)

    for i in range(len(la)):
        x = ((la[0] * lb[1]) + (la[1] * lb[2]) + (la[2] * lb[3]) + (la[3] * lb[0]))
        y = ((lb[0] * la[1]) + (lb[1] * la[2]) + (lb[2] * la[3]) + (lb[3] * la[0]))

        if terra == 1:
            terreno1 = x - y
            if terreno1 < 0:
                terreno1 = terreno1 * (-1)
        if terra == 2:
            terreno2 = x - y
            if terreno2 < 0:
                terreno2 = terreno2 * (-1)
if terreno1 > terreno2:
    print("terreno A")

else:
    print("terreno B")