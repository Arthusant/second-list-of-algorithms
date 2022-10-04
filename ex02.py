primeiro_numero = int(input('Digite um número: '))
menor = primeiro_numero
maior = primeiro_numero
for i in range (0,9):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O maior valor foi {maior} e o menor foi {menor}')