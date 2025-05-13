from models.ContaBancaria import ContaBancaria
from utils.ferramentas import ferramentas

# Lista para armazenar todas as contas criadas
Contas = []

while True:
    # Exibe o menu de opções para o usuário
    print("\n--- Menu ---")
    print("1 - Criar conta")
    print("2 - Exibir saldo")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Realizar transferência")
    print("6 - Exibir histórico de transações")
    print("7 - Excluir conta (Escolha conta para transferir o valor que resta na conta)")
    print("8 - Digite a sua chave pix")
    print("0 - Sair")

    # Recebe a escolha do usuário
    escolha = input("Tecle qual opção deseja fazer: ")

    # Opção 1: Criar conta
    if escolha == "1":
        titular = input("Digite o nome do titular: ")
        if ferramentas.buscar_conta(titular, Contas):
            print(f"A conta de {titular} já existe!")
        else:
            while True:
                try:
                    deposito_inicial = float(input("Digite o valor do depósito inicial: "))
                    break
                except ValueError:
                    print("Valor inválido! Digite um número.")
            limite = 0  # Limite de crédito padrão é 0

            # Cadastro das chaves Pix (até 3)
            chaves_pix = []
            for i in range(1, 4):
                chave = input(f"Digite a chave Pix {i}: ")
                chaves_pix.append(chave)

            conta = ContaBancaria(titular, deposito_inicial, limite, chaves_pix)
            Contas.append(conta)

            print(f"Conta criada com sucesso para {titular} com saldo inicial de R${deposito_inicial}!")
            print("Chaves Pix cadastradas:")
            for chave in chaves_pix:
                print(f"- {chave}")

    # Opção 2: Exibir saldo
    elif escolha == "2":
        titular = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            print(f"Seu saldo é de R${conta.saldo}")
        else:
            print("Conta não encontrada")

    # Opção 3: Sacar dinheiro
    elif escolha == "3":
        titular = input("Titular da conta: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            try:
                valor = float(input("Qual valor deseja sacar? "))
            except ValueError:
                print("Valor inválido!")
                continue
            if conta.sacar(valor, None):
                print(f"Saque de R${valor} realizado com sucesso!")
            else:
                print("Saque não realizado!")
        else:
            print("Conta não encontrada")

    # Opção 4: Depositar dinheiro
    elif escolha == "4":
        titular = input("Titular da conta: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            valor = float(input("Qual valor deseja depositar? "))
            if conta.depositar(valor, None):
                print(f"Depósito de R${valor} realizado com sucesso!")
            else:
                print("Depósito não realizado!")
        else:
            print("Conta não encontrada")

    # Opção 5: Transferir dinheiro entre contas
    elif escolha == "5":
        titular_origem = input("Titular da conta de origem: ")
        conta_origem = ferramentas.buscar_conta(titular_origem, Contas)
        if conta_origem:
            titular_destino = input("Titular da conta de destino: ")
            conta_destino = ferramentas.buscar_conta(titular_destino, Contas)
            if conta_destino:
                valor = float(input("Qual valor deseja transferir? "))
                if conta_origem.transferir(conta_destino, valor):
                    print(f"Transferência de R${valor} realizada com sucesso!")
                else:
                    print("Transferência não realizada!")
            else:
                print("Conta de destino não encontrada!")
        else:
            print("Conta de origem não encontrada!")

    # Opção 6: Exibir histórico de transações
    elif escolha == "6":
        titular = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            conta.exibirHistorico()
        else:
            print("Conta não encontrada")

    # Opção 7: Excluir conta (com transferência de saldo se necessário)
    elif escolha == "7":
        titular = input("Digite o nome do titular para excluir a conta: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            valor_restante = conta.saldo
            if valor_restante > 0:
                print(f"A conta tem um saldo de R${valor_restante}. Transferindo o saldo restante...")
                titular_transferencia = input("Para qual titular deseja transferir o saldo restante? ")
                conta_destino = ferramentas.buscar_conta(titular_transferencia, Contas)
                if conta_destino:
                    conta.transferir(conta_destino, valor_restante)
                    print(f"Saldo de R${valor_restante} transferido com sucesso!")
                    Contas.remove(conta)
                    print(f"Conta de {titular} excluída com sucesso!")
                else:
                    print("Conta de destino não encontrada!")
            else:
                Contas.remove(conta)
                print(f"Conta de {titular} excluída com sucesso!")
        else:
            print("Conta não encontrada")

    # Opção 8: Exibir chaves Pix cadastradas
    elif escolha == "8":
        titular = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(titular, Contas)
        if conta:
            print("Chaves Pix cadastradas:")
            for chave in conta.chavePix:
                print(f"{chave}")
        else:
            print("Conta não encontrada")

    # Opção 0: Sair do programa
    elif escolha == "0":
        print("Saindo...")
        break
