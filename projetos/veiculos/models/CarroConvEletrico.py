from .carroCombustao import carroCombustao
from .carroEletrico import carroEletrico


class CarroConvEletrico(carroCombustao, carroEletrico):
    # OBS: Esta classe representa um carro originalmente a combustão que foi convertido para elétrico,
    # herdando características de ambas as classes carroCombustao e carroEletrico.

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
        nivel_bateria: int,
        tipo_bateria: str,
        autonomia: int,
    ) -> None:
        """Construtor da classe CarroConvEletrico"""
        # Inicializa os atributos da classe pai
        super().__init__(
            modelo,
            marca,
            ano,
            cor,
            placa,
            fipe,
            combustivel,
            nPortas,
            nAssentos,
            nCilindradas,
            nCambio,
            nivelCombustivel,
        )

        carroEletrico.__init__(
            self,
            placa,
            marca,
            modelo,
            ano,
            cor,
            fipe,
            nAssentos,
            nPortas,
            nivel_bateria,
            tipo_bateria,
            autonomia,
        )
        # Inicializa os atributos da classe CarroConvEletrico

    def __str__(self) -> str:
        infos = carroCombustao.__str__(self)
        infos += f"Nível de bateria: {CarroConvEletrico.get_nivel_bateria(self)}"
        infos += f"\nTipo de bateria: {CarroConvEletrico.get_tipo_bateria(self)}"
        infos += f"\nAutonomia: {CarroConvEletrico.get_autonomia(self)}"
        return infos

    def abastecer(self, percentual_adicionado: float) -> bool:
        """Método que abastece o carro elétrico"""
        print("Carro convertido para eletrico! não é mais possivel abastecer.")
        # Aqui você pode adicionar a lógica específica para abastecer o carro elétrico
        return super().abastecer(percentual_adicionado)
