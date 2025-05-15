from models.veiculos import veiculos
from models.carroCombustao import carroCombustao
from models.carroEletrico import carroEletrico
from models.CarroConvEletrico import CarroConvEletrico

saveiro = veiculos(
    modelo="Saveiro",
    marca="Volkswagen",
    ano=2020,
    cor="Branco",
    placa="ABC-1234",
    fipe=50000,
)

Jetta_GLI = carroCombustao(
    modelo="Jetta GLI",
    marca="Volkswagen",
    ano=2024,
    cor="Preto",
    placa="BCE9D36",
    fipe=250000,
    combustivel="Gasolina",
    nPortas=4,
    nAssentos=5,
    nCilindradas=2000,
    nCambio="AT - 7",
    nivelCombustivel=24
)

telsa_model_s = carroEletrico(
    modelo="Tesla Model S",
    marca="Tesla",
    ano=2021,
    cor="Preto",
    placa="BCE9D36",
    fipe=950000,
    nPortas=4,
    nAssentos=5,
    nivel_bateria=100,
    tipo_bateria="Li-ion",
    autonomia=600
)

fusca_eletrico = CarroConvEletrico(
    modelo="Fusca 1600 Eletrico",
    marca="Volkswagen",
    ano=1975,
    cor="Azul",
    placa="IAA0D40",
    fipe=70000,
    combustivel="Gasolina",
    nPortas=4,
    nAssentos=5,
    nCilindradas=1600,
    nCambio="AT - 7",
    nivelCombustivel=24,
    nivel_bateria=65,
    tipo_bateria="Litio",
    autonomia=150
)

print(fusca_eletrico)

fusca_eletrico.abastecer(10)

print(fusca_eletrico)