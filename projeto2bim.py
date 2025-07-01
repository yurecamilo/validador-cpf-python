dados = list()
cpf = list()
num1 = list()
soma = 0
dig2list = []
ultdig = []
dadosUsuario = dict()
cpflist = []
cpfsvalidos = 0
cpfsinvalidos = 0

while True:

    cpf = input('digite um cpf: ')
    while (len(cpf) !=11 or cpf.isnumeric() == False):
        print('CPF inválido! Digite novamente.')
        cpf = input('digite um cpf: ')
    for i in range (0,11):
        cpflist.append(int(cpf[i]))

    dadosUsuario['CPF'] = cpflist[:]
    ultdig.append(cpflist.pop(9))
    ultdig.append(cpflist.pop(9))
    listdig1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    for i in range (0,9):
        soma += int(cpflist[i]) * listdig1[i]
    if soma % 11 < 2:
        dig1 = 0
    else:
        dig1 = 11 - (soma%11)

    dig2list = cpflist[:]
    dig2list.append(dig1)
    listdig2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range (0,10):
        soma += int(dig2list[i]) * listdig2[i]
    if soma % 11 < 2:
        dig2 = 0
    else:
        dig2 = 11 - (soma%11)

    
    if (dig1 == ultdig[0]) and (dig2 == ultdig[1]):
        dadosUsuario['VALIDAÇÃO'] = 'VÁLIDO'
    else:
        dadosUsuario['VALIDAÇÃO'] = 'INVÁLIDO'
    dados.append(dadosUsuario.copy())
 
    
    soma = 0
    ultdig = []
    cpflist = []

    
    while True:
        opcao = input('Deseja continuar? [S/N] ')
        if opcao in 'Nn':
            break
        elif opcao in 'Ss':
            break
        else:
            print('Opção inválida! Digite apenas S para sim ou N para não.')
    if opcao in 'Nn':
        break

for i in enumerate(dados):
    if i[1]['VALIDAÇÃO'] == 'VÁLIDO':
        cpfsvalidos +=1
    else:
        cpfsinvalidos +=1

cpfstotal = cpfsvalidos + cpfsinvalidos
porcentagemvalidos = (cpfsvalidos/cpfstotal) * 100
porcentageminvalidos = (cpfsinvalidos/cpfstotal) * 100
print ('*' * 50)
print(dados)
print(f'Quantidade de CPFS VÁLIDOS: {cpfsvalidos}')
print(f'Quantidade de CPFS INVÁLIDOS: {cpfsinvalidos}')
print(f'Quantidade total de CPFS testados: {cpfstotal}')
print(f'Porcentagem de CPFS VÁLIDOS: {porcentagemvalidos:.2f}%')
print(f'Porcentagem de CPFS INVÁLIDOS: {porcentageminvalidos:.2f}%')
