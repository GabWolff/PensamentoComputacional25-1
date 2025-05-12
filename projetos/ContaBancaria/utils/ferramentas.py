class ferramentas:

# Função para buscar uma conta pelo titular
    def buscar_conta(titular):
        for conta in Contas:
            if conta.titular == titular:
                return conta
        return None