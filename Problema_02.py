import random

def joknpoh():

    opcao_de_continuacao = True
    while (opcao_de_continuacao == True):

        print(f'Bem vindo ao jokenpoh!\n')
        print(f'Escolha uma opção para jogar: \n ')
        print(f'[0] Pedra')
        print(f'[1] Papel')
        print(f'[2] Tesoura\n')

        opcao_jogador = int(input("Digite sua escolha: "))

        opcao_maquina = random.randint(0,2)

        print('JO ')
        print('KEN ')
        print('POH!!')

        print('-=-=-=-=-=-=-=-=-=-=-=-=-')

        print(f'O computador escolheu a opcao {opcao_maquina}')
        print(f'O jogador escolheu {opcao_jogador}')

        print('-=-=-=-=-=-=-=-=-=-=-=-=-')

        if opcao_maquina == 0:
            if opcao_jogador == 0:
                print('Empate')
            elif opcao_jogador == 1:
                return 'Você ganhou!'
            elif opcao_jogador == 2:
                print('Você perdeu!')
            else:
                print('Opção inválida!')

        elif opcao_maquina == 1:
            if opcao_jogador == 0:
                print('Você perdeu')
            elif opcao_jogador == 1:
                print('Empate')
            elif opcao_jogador == 2:
                print('Você perdeu!')
            else:
                print('Opção inválida')
        elif opcao_maquina == 2:
            if opcao_jogador == 0:
                print('Você ganhou!')
            elif opcao_jogador == 1:
                print('Você perdeu')
            elif opcao_jogador == 2:
                print('Empate')
        else:
            print('Opção inválida')

        jogar_novamente = input('Deseja jogar novamente? (S/N)')

        if (jogar_novamente == 'N'):
            print("Obrigado por jogar!")
            opcao_de_continuacao = False
        else:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-")

joknpoh()