# L(M) = {w | w consiste em todas as cadeias com um número impar de 1's}

cadeias = ['0','1', '01', '001', '111', '110', '1101', '00001111', '0001', '001100', '00100', '11', '111', '11', '111110', '10', '']


for c in cadeias:
    q_par = True
    q_impar = False
    for i in c:
        if i == '1' and q_par:
            q_par = False
            q_impar = True
        elif i == '1' and q_impar:
            q_par = True
            q_impar = False
        

        if i == '0' and q_par:
            q_impar = False
            q_par = True
        elif i == '0' and q_impar:
            q_par = False
            q_impar = True
    
    if q_impar == True and q_par == False:
        print(f'{c} - Aceita')
    elif q_par == True and q_impar == False:
        print(f'{"vazio" if not c else c} - Rejeita')


