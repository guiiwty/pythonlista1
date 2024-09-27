quantidade_homens = int(input("Qual a quantidade de homens da turma? "))

quantidade_mulheres = int(input("Qual a quantidade de mulheres da turma? "))

quantidade_pessoas = quantidade_homens + quantidade_mulheres

porcentagem_homens = (float(quantidade_homens / quantidade_pessoas ))*100

porcentagem_mulheres = (float(quantidade_mulheres / quantidade_pessoas))*100

print(f"A quantidade total da turma é: {quantidade_pessoas}.")

print(f"A porcentagem de homens na turma é: {porcentagem_homens:.1f}%.")

print(f"A porcentagem de mulheres na turma é: {porcentagem_mulheres:.1f}%.")