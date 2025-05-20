from models.veiculos import veiculos
from models.carroCombustao import carroCombustao
from models.carroEletrico import carroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.caminhao import Caminhao
from models.moto import moto
from models.carro import Carro
from models.frota import Frota

# # saveiro = veiculos(
# #     modelo="Saveiro",
# #     marca="Volkswagen",
# #     ano=2020,
# #     cor="Branco",
# #     placa="ABC-1234",
# #     fipe=50000,
# # )

# # Jetta_GLI = carroCombustao(
# #     modelo="Jetta GLI",
# #     marca="Volkswagen",
# #     ano=2024,
# #     cor="Preto",
# #     placa="BCE9D36",
# #     fipe=250000,
# #     combustivel="Gasolina",
# #     nPortas=4,
# #     nAssentos=5,
# #     nCilindradas=2000,
# #     nCambio="AT - 7",
# #     nivelCombustivel=24
# # )

# # telsa_model_s = carroEletrico(
# #     modelo="Tesla Model S",
# #     marca="Tesla",
# #     ano=2021,
# #     cor="Preto",
# #     placa="BCE9D36",
# #     fipe=950000,
# #     nPortas=4,
# #     nAssentos=5,
# #     nivel_bateria=100,
# #     tipo_bateria="Li-ion",
# #     autonomia=600
# # )

# # fusca_eletrico = CarroConvEletrico(
# #     modelo="Fusca 1600 Eletrico",
# #     marca="Volkswagen",
# #     ano=1975,
# #     cor="Azul",
# #     placa="IAA0D40",
# #     fipe=70000,
# #     combustivel="Gasolina",
# #     nPortas=4,
# #     nAssentos=5,
# #     nCilindradas=1600,
# #     nCambio="AT - 7",
# #     nivelCombustivel=24,
# #     nivel_bateria=65,
# #     tipo_bateria="Litio",
# #     autonomia=150
# # )

# caminhao1 = Caminhao(
#     modelo="FH 540",
#     marca="Volvo",
#     ano=2022,
#     cor="Branco",
#     placa="XYZ-1234",
#     capacidade_carga=30.0,  # toneladas
#     eixos=6,
# )

# # print(caminhao1)  # Mostra os dados do caminhão

# # # Exemplo de uso do método calcular_consumo
# # distancia = 600  # km
# # print(f"Consumo para {distancia} km: {caminhao1.calcular_consumo(distancia)} litros\n")

# moto1 = moto(
#     modelo="CG 160",
#     marca="Honda",
#     ano=2021,
#     cor="Vermelha",
#     placa="ABC-5678",
#     cilindradas=160,
# )

# # print(moto1)
# # print(f"Consumo para 200 km: {moto1.calcular_consumo(200)} litros\n")

# carro_teste = Carro(
#     modelo="Gol",
#     marca="Volkswagen",
#     ano=2018,
#     cor="Branco",
#     placa="XYZ-9876",
#     nPortas=4,
# )

# # print(carro_teste)
# # print(f"Consumo para 400 km: {carro_teste.calcular_consumo(400)} litros")

# # veiculos_lista = [caminhao1, moto1, carro_teste]

# # distancia = float(input("Digite a distância a ser percorrida (em km): "))

# # print("\nConsumo de cada veículo para", distancia, "km:")
# # for veiculo in veiculos_lista:
# #     print(f"\n{veiculo}")
# #     print(f"Consumo: {veiculo.calcular_consumo(distancia)} litros")

# # Cria uma frota (lista de veículos)
# frota = Frota()

# # Adiciona diferentes veículos à frota
# frota.adicionar_veiculo(caminhao1)
# frota.adicionar_veiculo(moto1)
# frota.adicionar_veiculo(carro_teste)

# # Solicita ao usuário a distância a ser percorrida
# distancia = float(input("Digite a distancia a ser percorrida em KM: "))

# # Calcula e exibe o consumo de cada veículo e o consumo total da frota
# frota.calcular_consumos(distancia)

# # Calcula e exibe o consumo total da frota para a distância informada
# consumo_total = frota.calcular_consumo_total(distancia)
# print(f"\nConsumo total da frota para {distancia} km: {consumo_total} litros")

from models.carro import Carro
from models.moto import moto
from models.caminhao import Caminhao
from models.veiculo_eletrico import veiculo_eletrico
from models.frota import Frota

# Criação dos veículos
carro_teste = Carro(
    modelo="Gol",
    marca="Volkswagen",
    ano=2018,
    cor="Branco",
    placa="XYZ-9876",
    nPortas=4
)

moto1 = moto(
    modelo="CG 160",
    marca="Honda",
    ano=2021,
    cor="Vermelha",
    placa="ABC-5678",
    cilindradas=160
)

caminhao1 = Caminhao(
    modelo="FH 540",
    marca="Volvo",
    ano=2022,
    cor="Branco",
    placa="XYZ-1234",
    capacidade_carga=30.0,
    eixos=6
)

eletrico1 = veiculo_eletrico(
    modelo="Tesla Model 3",
    marca="Tesla",
    ano=2023,
    cor="Preto",
    placa="ELT-2023",
    fipe=350000
)

# Cria uma frota e adiciona veículos
frota = Frota()
frota.adicionar_veiculo(caminhao1)
frota.adicionar_veiculo(moto1)
frota.adicionar_veiculo(carro_teste)
frota.adicionar_veiculo(eletrico1)

# Solicita distância
distancia = float(input("Digite a distancia a ser percorrida em KM: "))

# Calcula e exibe o consumo de cada veículo
frota.calcular_consumos(distancia)

# Calcula e exibe o consumo total da frota
consumo_total = frota.calcular_consumo_total(distancia)
print(f"\nConsumo total da frota para {distancia} km: {consumo_total} litros/kWh")

# Demonstra polimorfismo com VeiculoEletrico
print("\nDemonstração do método exclusivo do veículo elétrico:")
eletrico1.recarregar()