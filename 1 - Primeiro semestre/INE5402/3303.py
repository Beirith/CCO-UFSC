while True:
    try:
        a = input()
        a = list(a)
        x = 0
        for i in range(len(a)):
            x += 1
        if x >= 10:
            print("palavrao")
        else:
            print("palavrinha")    
    except EOFError:
        break
# a primeira entrada consiste da palavra. para cada caractere da palavra
# adiciono 1 a variável x, que representa o número de caracteres da palavra
# caso a variavel x seja maior ou igual a 10, sera printado "palavrao"
# caso contrário, sera printado "palavrinha"