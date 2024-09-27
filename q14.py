perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

respostas_positivas = 0

for pergunta in perguntas:
    while True:
        resposta = input(pergunta + " (sim/não): ").lower()
        if resposta == "sim" or resposta == "não":
            if resposta == "sim":
                respostas_positivas += 1
            break
        else:
            print("Por favor, responda apenas com 'sim' ou 'não'.")

if respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(f"Você foi classificado como: {classificacao}")