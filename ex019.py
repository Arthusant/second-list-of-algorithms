populacao = 0
soma_salario = 0
soma_filhos = 0
menor_igual_250 = 0

num_filhos = int(input("Digite o numero de filhos: "))
while num_filhos < 0:
    print("Digite um numero de filhos válido")
    num_filhos = int(input("Digite o numero de filhos: "))

salario = float(input("Digite o salário: "))
while salario < 0:
    print("Digite um salário válido")
    salario = float(input("Digite o salário: "))

populacao += 1

if salario <= 250:
    menor_igual_250 += 1

soma_salario += salario
soma_filhos += num_filhos
maior_salario = salario

while salario > 0 and num_filhos > 0:
    num_filhos = int(input("Digite o numero de filhos: "))
    if num_filhos < 0:
        num_filhos = 0

    salario = float(input("Digite o salário, para parar digite um salário negativo: "))
    if salario < 0:
        salario = 0
        num_filhos = 0

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 250 and salario > 0:
        menor_igual_250 += 1

    if salario > 0:
        populacao += 1
    soma_salario += salario
    soma_filhos += num_filhos

perc_250 = (menor_igual_250 / populacao) * 100
media_salario = soma_salario / populacao
media_filhos = soma_filhos // populacao

print("Média do salário da população: {:.2f}".format(media_salario))
print("Média do número de filhos", media_filhos)
print("Maior salário: ", maior_salario)
print("Percentual de pessoas com salário até R$250,00: {:.2f}%".format(perc_250))