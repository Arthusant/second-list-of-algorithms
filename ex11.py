cont = 0
otimo = 0
total_idd = 0
bom = 0
for i in range (1,16):
    for n in range (1,16):
        i = int(input('Qual a sua idade? '))
        n = int(input('Qual nota você dá para esse filme? \n 3 - ótimo \n 2 - bom \n 1 - regular: '))
        total_idd +=i
        if n ==3:
            otimo +=1
            media_idd = total_idd / otimo

        if n ==1:
            cont+=1


        if n ==2:
            bom+=1
            total_bom = (bom*100) / 15
    print (f'A média da idade das pessoas que votaram ótimo é: {media_idd:.2f} anos')
    print (f'A quantidade de pessoas que responderam regular foi: {cont}')
    print (f'A porcentagem de pessoas que responderam bom foi de {total_bom:.2f}%')