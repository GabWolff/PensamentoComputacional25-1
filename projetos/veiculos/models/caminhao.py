from .veiculos import veiculos


class Caminhao(veiculos):

    def __init__(
        self,
        modelo: str,
        marca: str,
        ano: int,
        cor: str,
        placa: str,
        capacidade_carga: float,
        eixos: int,
    ):
        veiculos.__init__(self, modelo, marca, ano, cor, placa, fipe=0)
        self.capacidade_carga = capacidade_carga  # em toneladas
        self.eixos = eixos

    def calcular_consumo(self, distancia: float) -> float:
        """Calcula o consumo do caminhão em função da distância percorrida"""
        consumo_total = distancia / 5  # Exemplo: 5 km/l
        return consumo_total

    def __str__(self):
        return (
            f"Modelo: {self.modelo}\n"
            f"Marca: {self.marca}\n"
            f"Ano: {self.ano}\n"
            f"Cor: {self.cor}\n"
            f"Placa: {self.placa}\n"
            f"Capacidade de carga: {self.capacidade_carga} toneladas\n"
            f"Eixos: {self.eixos}"
        )

    def calcular_consumo(self, distancia: float) -> float:
        """Calcula o consumo do veículo em função da distância percorrida"""
        # Implementar lógica de cálculo de consumo
        consumo_total = distancia / 5  # Exemplo: 5 km/l
        return consumo_total
