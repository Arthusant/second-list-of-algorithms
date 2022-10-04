soma = 0
temperaturas = 0

temp = float(input("Informe a temperatura em Kelvin: "))
while temp < 0:
    print("Digite uma temperatura positiva")
    temp = float(input("Informe a temperatura em Kelvin: "))

maior_temp = temp
menor_temp = temp

soma += temp
temperaturas += 1

while temp >= 0:
    temp = float(input("Informe a temperatura em Kelvin, escreva negativo para parar: "))

    if temp > 0:
        temperaturas += 1
        soma += temp

    if temp > maior_temp:
        maior_temp = temp

    if temp > 0:
        if temp < menor_temp:
            menor_temp = temp

media = soma / temperaturas

print("a maior temperatura é: ", maior_temp)
print("a menor temperatura é: ", menor_temp)
print("a média das temperaturas é: {:.2f}".format(media))