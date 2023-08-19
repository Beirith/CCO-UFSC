# -*- coding: utf-8 -*-
import math

n = input()
frases = []

for i in range(int(n)):
    frase = input()
    fraseASCII = []
    for j in range(len(frase)):
        if frase[j].isalpha():
            fraseASCII.append(ord(frase[j])+3)
        else:
            fraseASCII.append(ord(frase[j]))

    fraseASCII.reverse()
    frases.append(fraseASCII)

for i in range(len(frases)):
    meio = len(frases[i])//2
    meioRange = math.ceil(len(frases[i])/2)
    for j in range(meioRange):
        frases[i][j+meio] -= 1


    print(''.join(chr(c)for c in frases[i]))
