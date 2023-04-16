# ∑ = {0, 1}
# L(M) = {w | w é a cadeia ε Ou termina em 0}

cadeias = ['', '0', '0', '00', '001', '10', '1111010', '111111', '101']

for c in cadeias:
    aceitacao = 1

    for s in c:
        if s == '0':
            if aceitacao == 1:
                aceitacao = 1
            else:
                aceitacao = 1

        if s == '1':
            if aceitacao == 1:
                aceitacao = 2
            else:
                aceitacao = 2


    if aceitacao == 1:
        print('Aceita')
    else:
        print('Rejeita')
