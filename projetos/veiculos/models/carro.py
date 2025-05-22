from .veiculos import veiculos

class Carro(veiculos):
    def __init__(
        self, modelo: str, marca: str, ano: int, cor: str, placa: str, nPortas: int
    ):
        veiculos.__init__(self, modelo, marca, ano, cor, placa, fipe=0)
        self.nPortas = nPortas

    def calcular_consumo(self, distancia: float) -> float:
        """Calcula o consumo do veículo em função da distância percorrida"""
        # Implementar lógica de cálculo de consumo
        consumo_total = distancia / 12  # Exemplo: 12 km/l
        # O consumo de uma moto é geralmente maior que o de um carro
        return consumo_total

    def __str__(self):
        return (
            f"Modelo: {self.__modelo}\n"
            f"Marca: {self.marca}\n"
            f"Ano: {self.ano}\n"
            f"Cor: {self.cor}\n"
            f"Placa: {self.placa}\n"
            f"Portas: {self.nPortas}"
        )
