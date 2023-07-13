menu = '''
O que deseja fazer?
[d] Depósito
[s] Saque
[e] Extrato
[c] Close
Digite aqui: '''

saldo= 0

extrato = ""

saque = 0
soma_saque = 0
LIMITE_SAQUES = 0

conta = 0
deposito = 0

fecharCores ='\033[m'
azul = '\033[34m'
vermelho = '\033[31m'
amarelo = '\033[33m'

while True:

    opcao = str(input(menu)).lower().strip()[0]

    if opcao == 'c':
        print('Fim do Programa')
        break

    if opcao == 's':

        if conta > 0:
            print(f'Seu saldo é de R${conta:.2f}')
            saque = int(input('Quanto deseja sacar: '))

            if saque > 500:
                print('Seu limite de saque é de R$ 500.00.')
                print(f'Seu saldo é de R${conta:.2f}')

            elif soma_saque >= 1500:
                print('Seu limite diário de R$1500.00 foi excedido e será liberado amanhã. Operação cancelada')
                print(f'Seu saldo é de R${conta:.2f}')

            elif LIMITE_SAQUES >= 3:
                print(f'Você fez 3 saques e sua quantidade de saques foram excedidas. Operação cancelada')
                print(f'Seu saldo é de R${conta:.2f}')

            elif saque < 1:
                print('Você não pode sacar esse valor')

            elif conta - saque < 0:
                print('Saldo insuficiente para esse saque.')
                print(f'Seu saldo é de R${conta:.2f}')

            else:
                extrato += f'Saque: R${vermelho}{saque:.2f}-{fecharCores}\n'
                conta -= saque
                LIMITE_SAQUES += 1
                soma_saque += saque

        else:
            print('Você não tem saldo, para ser sacado')


    if opcao == 'd':
        print(f'Seu saldo é de R${conta:.2f}')
        deposito = int(input('Quanto deseja depositar? '))

        if deposito > 0:
            conta += deposito
            extrato += f'Depósito: R${azul}{deposito:.2f}+{fecharCores}\n'
        else:
            print('Operação cancelada')

    if opcao == 'e':
        if extrato == "":
            print(f'\n'
                  f'{10 * "="} Extrato: {10 * "="}\n')
            print(f'{amarelo}Sua conta não teve nenhuma movimentação.{fecharCores}\n')
            print(f'Saldo da conta: R${amarelo}{conta:.2f}{fecharCores}\n')
        else:
            print(f'\n'
                  f'{10*"="}Extrato:{10*"="}\n'
                  f'{extrato}')
            print(f'Saldo da conta: R${amarelo}{conta:.2f}{fecharCores}\n')

