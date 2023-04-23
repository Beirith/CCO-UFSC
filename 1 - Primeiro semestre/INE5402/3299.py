a = input()
x = list(a)
m = False
for i in range(len(x)):
    ip = i + 1
    if i != len(x) - 1:
        if x[i] == '1' and x[ip] == '3':
            m = True  
if m == True:
    print("%s es de Mala Suerte" % (a))
else:
    print("%s NO es de Mala Suerte" % (a))
# a entrada consiste de um numero. atribuo a variavel x a uma lista com o valor de entrada A.
# percorro a lista x e, se o índice atual x[i] for igual a 1, e o proximo índice x[ip]
# for igual a 3, então o número é de má sorte. caso o contrário, o número não é
# de má sorte.