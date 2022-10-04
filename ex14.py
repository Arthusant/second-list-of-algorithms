pessoas = int (input('Quantas pessoas? '))
if pessoas <0:
    print ('Não é possivel haver pessoas negativas em um local')

else:
    total = 0
    for i in range (1, pessoas+1):
        idade = int(input('Quais as idades: '))
        if idade>=0:
            total = total + idade
            media = total / pessoas
        if idade <0:
            print ('não existe idade negativa')

    if idade >=0:

        if media >=0 and media <= 25:
            print ('A turma é JOVEM!')

        if media >=26 and media <= 60:
            print ('A turma é ADULTA!')

        if media >60:
            print ('A turma é IDOSA!')


