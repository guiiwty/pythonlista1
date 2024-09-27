def is_bissexto(ano):
    """Verificar se um ano é bissexto."""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):
    """Verificar se a data é válida."""
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if is_bissexto(ano):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    
    return True

data = input("Digite uma data no formato dd/mm/aaaa: ")
partes = data.split('/')

if len(partes) == 3:
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        if data_valida(dia, mes, ano):
            print("A data informada é válida.")
        else:
            print("A data informada é inválida.")
    except ValueError:
        print("Erro. Insira números válidos para dia, mês e ano.")
else:
    print("Formato de data inválido. Use apenas dd/mm/aaaa.")