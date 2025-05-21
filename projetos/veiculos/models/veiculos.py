import re


class veiculos:

    def __init__(self, modelo, marca, ano, cor, placa, fipe):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.setPlaca(placa)  # usa o setter para validar
        self.__fipe = fipe

    def __str__(self) -> str:
        """Retorna uma representação em string do veículo"""
        infos = f"placa: {self.__placa}\n"
        infos += f"modelo: {self.__modelo}\n"
        infos += f"marca: {self.__marca}\n"
        infos += f"ano: {self.__ano}\n"
        infos += f"cor: {self.__cor}\n"
        infos += f"fipe: {self.__fipe}\n"
        return infos

    def getPlaca(self) -> str:
        """Retorna a placa do veículo"""
        return self.__placa

    def setPlaca(self, placa: str) -> bool:
        """Define a placa do veículo se for válida (3 letras e 4 números)"""
        if re.fullmatch(r"[A-Za-z]{3}[0-9]{4}", placa):
            self.__placa = placa.upper()
            return True
        else:
            print("Placa inválida! Use o padrão: 3 letras e 4 números (ex: ABC1234).")
            return False

    def calcular_consumo(self, distancia: float) -> float:
        """Calcula o consumo do veículo em função da distância percorrida"""
        consumo_total = distancia / 12  # Exemplo: 12 km/l
        return consumo_total

    def __eq__(self, other):
        """Compara dois veículos pela placa"""
        if isinstance(other, veiculos):
            return self.__placa == other.__placa
        return False
