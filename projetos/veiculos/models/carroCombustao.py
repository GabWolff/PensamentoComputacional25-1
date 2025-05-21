class veiculos:
    def __init__(
        self, modelo: str, marca: str, ano: int, cor: str, placa: str, fipe: float
    ):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.fipe = fipe

    def __str__(self) -> str:
        return (
            f"modelo: {self.modelo}\n"
            f"marca: {self.marca}\n"
            f"ano: {self.ano}\n"
            f"cor: {self.cor}\n"
            f"placa: {self.placa}\n"
            f"fipe: {self.fipe}\n"
        )


from .veiculos import veiculos


class carroCombustao(veiculos):
    """Classe que representa um veículo do tipo carro a combustão"""

    def __init__(
        self,
        modelo: str,
        marca: str,
        ano: int,
        cor: str,
        placa: str,
        fipe: float,
        combustivel: str,
        nPortas: int,
        nAssentos: int,
        nCilindradas: int,
        nCambio: str,
        nivelCombustivel: int,
    ) -> None:
        """Construtor da classe carroCombustao"""
        # Inicializa os atributos da classe pai
        veiculos.__init__(self, modelo, marca, ano, cor, placa, fipe)
        # Inicializa os atributos da classe carroCombustao
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
        self.__nivelCombustivel = nivelCombustivel

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do carro a combustão"""
        # Chama o método __str__ da classe pai (veiculos)
        infos = super().__str__()
        # e adiciona as informações específicas da classe carroCombustao
        infos += f"combustivel: {self.__combustivel}\n"
        infos += f"nPortas: {self.__nPortas}\n"
        infos += f"nAssentos: {self.__nAssentos}\n"
        infos += f"nCilindradas: {self.__nCilindradas}\n"
        infos += f"nCambio: {self.__nCambio}\n"
        infos += f"nivelCombustivel: {self.__nivelCombustivel}\n"
        return infos

    def abastecer(self, percentual_adicionado: int) -> None:
        novo_percentual = self.__nivelCombustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivelCombustivel = novo_percentual
            return True
        return False
