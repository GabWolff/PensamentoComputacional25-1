class ferramentas:
# Função para buscar conta
    
    def buscar_conta(titular, contas):
        for conta in contas:
            if conta.titular == titular:
                return conta
        return None


    def gerenciar_pix(conta):
        while True:
            print("\n--- Gerenciamento de Chaves Pix ---")
            print("1 - Visualizar chaves Pix")
            print("2 - Adicionar nova chave Pix")
            print("3 - Remover chave Pix")
            print("0 - Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                if conta.chavePix:
                    print("Chaves Pix cadastradas:")
                    for chave in conta.chavePix:
                        print(f"- {chave}")
                else:
                    print("Nenhuma chave Pix cadastrada.")

            elif opcao == "2":
                nova_chave = input("Digite a nova chave Pix (CPF, email, telefone, etc.): ")
                if nova_chave in conta.chavePix:
                    print("Essa chave já está cadastrada.")
                else:
                    conta.chavePix.append(nova_chave)
                    print("Chave Pix adicionada com sucesso!")

            elif opcao == "3":
                chave_remover = input("Digite a chave Pix que deseja remover: ")
                if chave_remover in conta.chavePix:
                    conta.chavePix.remove(chave_remover)
                    print("Chave Pix removida com sucesso!")
                else:
                    print("Chave não encontrada.")

            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
