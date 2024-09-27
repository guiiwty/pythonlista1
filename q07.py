preco_produto = float(input("Qual o preço do produto? "))
desconto = float(input("Qual a porcentagem do desconto? "))

valor_desconto = (desconto / 100) * preco_produto
valor_final = preco_produto - valor_desconto

print(f"Você ganhou R$ {valor_desconto} de desconto!")
print(f"O produto ficou por R$ {valor_final} com o desconto aplicado.")