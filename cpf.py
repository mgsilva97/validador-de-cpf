cpf = "11111111111"
soma = 0
controle = 10
digito_1 = 0
digito_2 = 0
resto_divisao = 0
verificador = cpf[9:]

# Calculo primeiro digito validador
for i in cpf:
    if controle < 2:
        break
    else:
        calculo = int(i) * controle
        soma = soma + calculo
        controle -= 1
resto_divisao = (soma % 11)

if resto_divisao < 2:
    digito_1 = 0
    controle = 11
    soma = 0
elif resto_divisao >= 2:
    digito_1 = (11 - resto_divisao)
    controle = 11
    soma = 0

# calculo segundo digito validador
for i in cpf:
    if controle < 2:
        break
    else:
        # print(i, controle)
        calculo = int(i) * controle
        soma = soma + calculo
        controle -= 1
resto_divisao = (soma % 11)

if resto_divisao < 2:
    digito_2 = 0

elif resto_divisao >= 2:
    digito_2 = (11 - resto_divisao)

final = f'{digito_1}{digito_2}'
if final == verificador:
    print("CPF Válido")
else:
    print("CPF INVÁLIDO BITCH")
