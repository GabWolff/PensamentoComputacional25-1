class moto:
    def __init__(self, modelo: str, marca: str, ano: int, cor: str, placa: str, cilindradas: int):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.cilindradas = cilindradas

    def calcular_consumo(self, distancia: float) -> float:
        """Calcula o consumo da moto em função da distância percorrida"""
        consumo_total = distancia / 20  # Exemplo: 20 km/l
        return consumo_total

    def __str__(self):
        return (f"Modelo: {self.modelo}\n"
                f"Marca: {self.marca}\n"
                f"Ano: {self.ano}\n"
                f"Cor: {self.cor}\n"
                f"Placa: {self.placa}\n"
                f"Cilindradas: {self.cilindradas} cc")

