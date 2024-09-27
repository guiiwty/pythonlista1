valor_hora = float(input("Informe o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 1903.98:
    ir_percentual = 0
elif salario_bruto <= 2826.65:
    ir_percentual = 7.5 / 100
elif salario_bruto <= 3751.05:
    ir_percentual = 15 / 100
elif salario_bruto <= 4664.68:
    ir_percentual = 22.5 / 100
else: 
    ir_percentual = 27.5 / 100

ir_desconto = salario_bruto * ir_percentual
sindicato_desconto = salario_bruto * 3 / 100
fgts = salario_bruto * 11 / 100

salario_liquido = salario_bruto - ir_desconto - sindicato_desconto

print("\n--- Resumo da folha de Pagamento ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR ({ir_desconto * 100:.2f}%): R$ {ir_desconto}")
print(f"Desconto Sindicato (3%): R$ {sindicato_desconto:.2f}")
print(f"Valor do FGTS depositado pela empresa (11%): R$ {fgts:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")