numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Insira um número válido (menor que 1000).")
else:
    centenas = numero // 100
    resto = numero % 100
    dezenas = resto // 10
    unidades = resto % 10
    
    if centenas >0:
        print(f"{centenas}", end=(", "))
    if dezenas > 0 or centenas > 0:
        print(f"{dezenas} dezenas", end=", ")
    print(f"{unidades} unidades")