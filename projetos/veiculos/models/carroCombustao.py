class veiculos:
    def __init__(self, modelo: str, marca: str, ano: int, cor: str, placa: str, fipe: float, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str):
        # ...

from .veiculos import veiculos
class carroCombustao(veiculos):
    """Classe que representa um veículo do tipo carro a combustão"""
    
    def __init__(self, modelo: str, marca: str, ano: int, cor: str, placa: str, fipe: float, combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str) -> None:
        """ Construtor da classe carroCombustao"""
        # Inicializa os atributos da classe pai
        
        super().__init__(modelo, marca, ano, cor, placa, fipe, nPortas, nAssentos, nCilindradas, nCambio)
        # Inicializa os atributos da classe carroCombustao
        self.__combustivel = combustivel
        
    def __str__(self) -> str:
        """ Método que retorna uma string com as informações do carro a combustão"""
        # Chama o método __str__ da classe pai (veicuilos)
        infos = super().__str__()
        # e adiciona as informações específicas da classe carroCombustao
        infos += f"combustivel: {self.__combustivel}\n"
        return infos


