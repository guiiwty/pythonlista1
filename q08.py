letra = input("Digite uma letra: ")

if len(letra) !=1 or not letra.isalpha():
    print("Apenas letra é permitido, tente novamente.")
else:
    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")