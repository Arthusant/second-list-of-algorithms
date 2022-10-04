pessoas = int(input("Digite a quantidade de pessoas: "))
soma_idade = 0
while pessoas < 1:
  print("Digite uma quantidade de pessoas válida: ")
  pessoas = int(input("Digite a quantidade de pessoas: "))

for i in range(pessoas):
  idade = int(input("Digite a sua idade: "))
  while idade < 0:
    print("Digite uma idade válida: ")
    idade = int(input("Digite a sua idade: "))
  soma_idade += idade

media_idade = soma_idade/pessoas
if media_idade < 26:
  print("A turma é jovem")
else:
  if media_idade < 61:
    print("A turma é adulta")
  else:
    print("A turma é idosa")