from .veiculos import veiculos

class carroEletrico(veiculos):
    """Classe que importa métodos especificos de carros eletricos
    Argumento: classe pai veiculo
    """
    
    def __init__(self, placa: str, marca: str, modelo: str, ano: int, cor: str, fipe: float, nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int):
        """Construtor da classe carroEletrico
        Argumentos: marca, modelo, ano, cor e tipo_bateria
        """
        veiculos.__init__(self, placa, marca, modelo, ano, cor, fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas    
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
    
    def __str__(self):
        info = super().__str__()
        info += f"Número de assentos: {self.__nAssentos}"
        info += f"\nNúmero de portas: {self.__nPortas}"
        info += f"\nNível de bateria: {self.__nivel_bateria}"
        info += f"\nTipo de bateria: {self.__tipo_bateria}"
        info += f"\nAutonomia: {self.__autonomia}"
        return info
    
    def get_nivel_bateria(self) -> int:
        """Retorna o nível de bateria do carro elétrico"""
        return self.__nivel_bateria
    
    def get_tipo_bateria(self) -> str:
        """Retorna o tipo de bateria do carro elétrico"""
        return self.__tipo_bateria
    
    def get_autonomia(self) -> int:
        """Retorna a autonomia do carro elétrico"""
        return self.__autonomia
        