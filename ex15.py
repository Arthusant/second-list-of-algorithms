termos = int(input("Digite a quantidade de termos: "))
A1 = int(input("Digite o primeiro termo: "))                      # numeros decimais não são classificados em par ou ímpar por isso int
A2 = int(input("Digite o segundo termo: "))                       # numeros decimais não são classificados em par ou ímpar por isso int
Ai = 0

while termos < 3:
  print("Digite uma quantidade de termos válida")
  termos = int(input("Digite a quantidade de termos: "))

print(A1)
print(A2)
for i in range(3,termos+1):
  if i % 2 == 0:
    Ai = A1 - A2
    print(Ai)
  else:
    Ai = A1 + A2
    print(A1)
  A1 = A2   # primeiro termo vira o segundo e
  A2 = Ai   # e o segundo vira o terceiro para poder realizar a proxima sequencia

