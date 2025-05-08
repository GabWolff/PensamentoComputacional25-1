class ferramentas:

    def buscar_conta(titular):
        for conta in Contas:
            if conta.titular == titular:
                return conta