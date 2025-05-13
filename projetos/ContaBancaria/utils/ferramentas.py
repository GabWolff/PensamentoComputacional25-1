class ferramentas:
# Função para buscar conta
    
    def buscar_conta(titular, contas):
        for conta in contas:
            if conta.titular == titular:
                return conta
        return None
