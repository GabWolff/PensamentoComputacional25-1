class veiculos:
    
    def __init__(self, modelo, marca, ano, cor, placa, fipe,):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__placa = placa
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