class Frota:
    def __init__(self):
        # Lista privada para armazenar os veículos da frota
        self.__veiculos = []

    def adicionar_veiculo(self, veiculo):
        # Adiciona um veículo à frota
        self.__veiculos.append(veiculo)

    def listar_veiculos(self):
        # Lista todos os veículos da frota
        for veiculo in self.__veiculos:
            print(veiculo)

    def calcular_consumos(self, distancia: float):
        # Mostra o consumo de cada veículo para a distância informada
        print(f"\nConsumo de cada veículo para {distancia} km:")
        for veiculo in self.__veiculos:
            print(f"\n{veiculo}")
            print(f"Consumo: {veiculo.calcular_consumo(distancia)} litros")

    def calcular_consumo_total(self, distancia: float) -> float:
        """Retorna o consumo total da frota para a distância informada"""
        total = 0
        for veiculo in self.__veiculos:
            total += veiculo.calcular_consumo(distancia)
        return total
