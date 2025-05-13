from models.ContaBancaria import ContaBancaria
from utils.ferramentas import buscar_conta

# Lista de contas
Contas = []



# Função principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1 - Criar conta")
        print("2 - Exibir saldo")
        print("3 - Sacar")
        print("4 - Depositar")
        print("5 - Realizar transferência")
        print("6 - Exibir histórico de transações")
        print("7 - Excluir conta (Escolha conta para transferir o valor que resta na conta)")
        print("0 - Sair")

        escolha = input("Tecle qual opção deseja fazer: ")

        if escolha == "1":
            titular = input("Digite o nome do titular: ")
            if buscar_conta(titular):
                print(f"A conta de {titular} já existe!")
            else:
                deposito_inicial = float(input("Digite o valor do depósito inicial: "))
                conta = ContaBancaria(titular, saldo=deposito_inicial)
                if deposito_inicial > 0:
                    conta.depositar(deposito_inicial)
                    print(f"Depósito inicial de R${deposito_inicial} realizado com sucesso!")
                Contas.append(conta)
                print(f"Conta criada com sucesso para {titular} com saldo inicial de R${deposito_inicial}!")

        elif escolha == "2":
            titular = input("Digite o nome do titular: ")
            conta = buscar_conta(titular)
            if conta:
                print(f"Seu saldo é de R${conta.saldo}")
            else:
                print("Conta não encontrada")

        elif escolha == "3":
            titular = input("Titular da conta: ")
            conta = buscar_conta(titular)
            if conta:
                valor = float(input("Qual valor deseja sacar? "))
                if conta.sacar(valor):
                    print(f"Saque de R${valor} realizado com sucesso!")
                else:
                    print("Saque não realizado!")
            else:
                print("Conta não encontrada")

        elif escolha == "4":
            titular = input("Titular da conta: ")
            conta = buscar_conta(titular)
            if conta:
                valor = float(input("Qual valor deseja depositar? "))
                if conta.depositar(valor):
                    print(f"Depósito de R${valor} realizado com sucesso!")
                else:
                    print("Depósito não realizado!")
            else:
                print("Conta não encontrada")

        elif escolha == "5":
            titular_origem = input("Titular da conta de origem: ")
            conta_origem = buscar_conta(titular_origem)
            if conta_origem:
                titular_destino = input("Titular da conta de destino: ")
                conta_destino = buscar_conta(titular_destino)
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

        elif escolha == "6":
            titular = input("Digite o nome do titular: ")
            conta = buscar_conta(titular)
            if conta:
                conta.exibirHistorico()
            else:
                print("Conta não encontrada")

        elif escolha == "7":
            titular = input("Digite o nome do titular para excluir a conta: ")
            conta = buscar_conta(titular)
            if conta:
                valor_restante = conta.saldo
                if valor_restante > 0:
                    print(f"A conta tem um saldo de R${valor_restante}. Transferindo o saldo restante...")
                    titular_transferencia = input("Para qual titular deseja transferir o saldo restante? ")
                    conta_destino = buscar_conta(titular_transferencia)
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

        elif escolha == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
