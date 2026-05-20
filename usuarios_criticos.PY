A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

usuarios = [101, 102, 103, 104, 105, 106, 107, 108, 109]

for usuario in usuarios:

    p = usuario in A
    q = usuario in B
    r = usuario in C

    if (p or q) and r:
        print(usuario, "-> Critico")
    else:
        print(usuario, "-> No critico")
