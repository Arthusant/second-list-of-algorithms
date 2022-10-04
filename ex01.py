for a in range (0,5):
    nota1 = float(input('Informe a Primeira nota do aluno: '))
    nota2 = float(input('Informe a Segunda nota do aluno: '))
    if nota1 <0 or nota2 <0 or nota1>10 or nota2 >10:
        print ('Nota invalida, por favor digite uma nota entre 0 e 10')
    else:
        media = (nota1 + nota2)/2
        if media >=7 and media <=10:
            print (f'a media ficou {media}, então o aluno foi APROVADO!')
        if media >=0 and media <=4:
            print (f'a media ficou {media}, O aluno foi reprovado!')
        if media >4 and media <7:
            print (f'a media ficou {media}, O aluno vai para recuperação!')

        if nota1 <0 or nota2 <0 or nota1>10 or nota2 >10:
            print ('Nota invalida, por favor digite uma nota entre 0 e 10')