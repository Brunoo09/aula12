# 1: Verificando se uma string é vazia ou não

string = input('==')
match string:
    case a if a:
        print('cheio')
    case _:
        print('vazio')

# 2: Verificando se um número é maior, menor ou igual a 10

numero = int(input('digite um numero'))

match numero:
    case numero if numero == 10:
        print('é dez')
    case numero if numero < 10:
        print('é menor que dez')
    case numero if numero > 10:
        print(' é maior que dez')


# 3: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso

idade = int(input('digite sua idade'))

match idade:
    case idade if idade < 12:
        print('criança')
    case idade if idade < 17:
        print('jovem')
    case idade if idade > 18:
        print('adulto')
    case idade if idade > 63:
        print('idoso')

