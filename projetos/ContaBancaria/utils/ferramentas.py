class ferramentas:
    """
    Classe utilitária com métodos estáticos para manipulação de contas bancárias.
    """

    @staticmethod
    def buscar_conta(titular, contas):
        """
        Busca uma conta pelo nome do titular na lista de contas.
        Retorna o objeto ContaBancaria se encontrar, ou None se não encontrar.
        """
        for conta in contas:
            if conta.titular == titular:
                return conta
        return None

    @staticmethod
    def gerenciar_pix(conta):
        """
        Exibe todas as chaves Pix cadastradas para a conta informada.
        """
        print(f"Gerenciando PIX para {conta.titular}")
        for chave in conta.chavePix:
            print(f"- {chave}")
