from .veiculos import veiculos

class veiculo_eletrico(veiculos):
    def __init__(self, modelo, marca, ano, cor, placa, fipe):
        # Inicializa diretamente os atributos da classe veiculos
        self._veiculos__modelo = modelo
        self._veiculos__marca = marca
        self._veiculos__ano = ano
        self._veiculos__cor = cor
        self._veiculos__placa = placa
        self._veiculos__fipe = fipe

    def calcular_consumo(self, distancia: float) -> float:
        """Retorna o consumo em kWh para a distância informada (exemplo: 0,15 kWh/km)"""
        return distancia * 0.15

    def recarregar(self):
        print(f"{self._veiculos__modelo}: Veículo elétrico recarregado!")
