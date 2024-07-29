from random import randint
cpf_Gerado = ""
for i in range(9):
    cpf_Gerado += str(randint(0, 9))
lista_de_multiplicacao = []
multiplicacao = 10
for indices in cpf_Gerado:
    indices = int(indices)
    x = indices * multiplicacao
    lista_de_multiplicacao.append(x)
    multiplicacao -= 1

soma1 = sum(lista_de_multiplicacao)
multi_da_Soma = soma1 * 10
resto_da_Divisão = multi_da_Soma % 11
primeiro_digito = resto_da_Divisão if resto_da_Divisão < 10 else 0
cpf_Gerado += str(primeiro_digito)
lista_para_Soma = []
contagem_regressiva = 11
for i in cpf_Gerado:
    x = int(i) * contagem_regressiva
    lista_para_Soma.append(x)
    contagem_regressiva -= 1
soma2 = sum(lista_para_Soma)
multi_da_Soma2 = soma2 * 10
resto_da_Divisão2 = multi_da_Soma2 % 11
segundo_digito = resto_da_Divisão2 if resto_da_Divisão2 < 10 else 0

cpf_Gerado += str(segundo_digito)

print(f"CPF Gerado: {cpf_Gerado}")
