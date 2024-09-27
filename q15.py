preco_alcool = 1.90
preco_gasolina = 2.50

litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").strip().upper()

valor_a_pagar = 0.0

if tipo_combustivel == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_bruto = litros * preco_alcool
    valor_a_pagar = valor_bruto - (valor_bruto * desconto)

elif tipo_combustivel == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06 
    valor_bruto = litros * preco_gasolina
    valor_a_pagar = valor_bruto - (valor_bruto * desconto)

else:
    print("Tipo de combustível inválido.")

print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")