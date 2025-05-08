from models.ContaBancaria import ContaBancaria
from utils.ferramentas import ferramentas

Gabriel = ContaBancaria("Gabriel", 1000, 500, [])
Mariana = ContaBancaria("Mariana", 4000, 500, [])
# Gabriel.depositar(400)
# Gabriel.transferir(Mariana, 300)
# Gabriel.exibirHistorico()

# # Wolff.dpositar(150)
# # Wolff.sacar(100)
# Gabriel.exibirHistorico()
Contas = []
       
while True:
    print("1 - Criar conta")
    print("2 - Exibir saldo")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Realizar transferencia")
    print("6 - Exibir histórico de transações")
    print("7 - Excluir conta (Escolha conta para transferir o valor que resta na conta)")
    
    escolha = input("Tecle qual opção deseja fazer: ")
    
    if escolha == 1:
        titular = input("Digite o nome do titular: ")
           
    elif escolha == 2:
        titular = input("Digite o nome do titular: ")
        conta = buscar_conta(titular)
        if conta:
            print(f"Seu saldo é de {conta.saldo}")
        else:
            print("Conta não encontrada")
    elif escolha == 3:
        titular = input("Titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            valor = float(input("Qaul valor deseja sacar?"))
            if conta.sacar(valor):
                print(f"Saque de {valor} realizado com sucesso")
            else:
                print("")
            
    elif escolha == 4:
        pass
    elif escolha == 5:
       break