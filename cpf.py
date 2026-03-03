def validar_cpf(cpf):
    #removendo caracteres não numericos
    cpf = ''.join(filter(str.isdigit, cpf))

    #verificando se o cpf possui 11 digitos
    if len(cpf) != 11:
        return False

    #verificando se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        return False

    #calculando o primeiro digito verificador
    soma = sum(int(cpf[i]) *  (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    #verificando o primeiro digito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    # calculando o segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # verificando o segundo digito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False

    #cpf valido
    return True

#testar função
cpf = "123.456.789-09"
if validar_cpf(cpf):
    print(f'O CPF: {cpf} é valido.')
else:
    print(f'O CPF: {cpf} é invalido.')