from models.veiculos import veiculos
from models.carroCombustao import carroCombustao
from models.carroEletrico import carroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.carro import Carro
from models.moto import moto
from models.caminhao import Caminhao
from models.veiculo_eletrico import veiculo_eletrico
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
## -----------------------Exercicio 1-----------------------##
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

##----------------------Exercicio 2----------------------##

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

## -----------------------Exercicio 3-----------------------##

# Criação dos veículos
# carro_teste = Carro(
#     modelo="Gol",
#     marca="Volkswagen",
#     ano=2018,
#     cor="Branco",
#     placa="XYZ-9876",
#     nPortas=4
# )

# #criação da moto
# moto1 = moto(
#     modelo="CG 160",
#     marca="Honda",
#     ano=2021,
#     cor="Vermelha",
#     placa="ABC-5678",
#     cilindradas=160
# )

# # Criação do caminhão
# caminhao1 = Caminhao(
#     modelo="FH 540",
#     marca="Volvo",
#     ano=2022,
#     cor="Branco",
#     placa="XYZ-1234",
#     capacidade_carga=30.0,
#     eixos=6
# )

# # Criação do veículo elétrico
# eletrico1 = veiculo_eletrico(
#     modelo="Tesla Model 3",
#     marca="Tesla",
#     ano=2023,
#     cor="Preto",
#     placa="ELT-2023",
#     fipe=350000
# )

# # Cria uma frota e adiciona veículos
# frota = Frota()
# frota.adicionar_veiculo(caminhao1)
# frota.adicionar_veiculo(moto1)
# frota.adicionar_veiculo(carro_teste)
# frota.adicionar_veiculo(eletrico1)

# # Solicita distância
# distancia = float(input("Digite a distancia a ser percorrida em KM: "))

# # Calcula e exibe o consumo de cada veículo
# frota.calcular_consumos(distancia)

# # Calcula e exibe o consumo total da frota
# consumo_total = frota.calcular_consumo_total(distancia)
# print(f"\nConsumo total da frota para {distancia} km: {consumo_total} litros/kWh")

# # Demonstra polimorfismo com VeiculoEletrico
# print("\nDemonstração do método exclusivo do veículo elétrico:")
# eletrico1.recarregar()

## ----------------------Exercicio 4---------------------- ##

# Teste de alteração de placa para valores válidos e inválidos

# Cria um veículo
# veiculo_teste = veiculos(
#     modelo="Uno", marca="Fiat", ano=2015, cor="Prata", placa="ABC1234", fipe=25000
# )

# print("Placa inicial:", veiculo_teste.getPlaca())

# # Tenta alterar para uma placa válida
# print("\nTentando alterar para placa válida (DEF5678):")
# if veiculo_teste.setPlaca("DEF5678"):
#     print("Placa alterada com sucesso!")
# else:
#     print("Falha ao alterar a placa.")
# print("Placa atual:", veiculo_teste.getPlaca())

# # Tenta alterar para uma placa inválida
# print("\nTentando alterar para placa inválida (12A4567):")
# if veiculo_teste.setPlaca("12A4567"):
#     print("Placa alterada com sucesso!")
# else:
#     print("Falha ao alterar a placa.")
# print("Placa atual:", veiculo_teste.getPlaca())

# ------------------------Exercicio 5---------------------##

# Cria uma lista de veículos com placas repetidas entre carros, motos e elétricos
# veiculos_lista = [
#     Carro("Gol", "VW", 2020, "Branco", "ABC1234", 4),
#     moto("CG 160", "Honda", 2021, "Vermelha", "ABC1234", 160),
#     veiculo_eletrico("Leaf", "Nissan", 2022, "Prata", "XYZ5678", 200000),
#     Carro("Onix", "Chevrolet", 2021, "Preto", "XYZ5678", 4)
# ]

# print("\n--- Verificando veículos duplicados pela placa ---")
# for i in range(len(veiculos_lista)):
#     for j in range(i + 1, len(veiculos_lista)):
#         if veiculos_lista[i] == veiculos_lista[j]:
#             print(f"Duplicado: {veiculos_lista[i].getPlaca()}")

# Cria uma lista de veículos de diferentes tipos
veiculos_lista = [
    Carro("Gol", "Volkswagen", 2020, "Branco", "ABC1234", 4),
    moto("CG 160", "Honda", 2021, "Vermelha", "DEF5678", 160),
    Caminhao("FH 540", "Volvo", 2022, "Branco", "GHI9012", 30.0, 6),
    veiculo_eletrico("Leaf", "Nissan", 2022, "Prata", "JKL3456", 200000)
]

try:
    distancia = float(input("Digite a distância a ser percorrida em KM: "))
    if distancia < 0:
        raise ValueError("A distância não pode ser negativa.")
    if not veiculos_lista:
        raise Exception("A lista de veículos está vazia.")

    print("\nConsumo de cada veículo para", distancia, "km:")
    for veiculo in veiculos_lista:
        consumo = veiculo.calcular_consumo(distancia)
        print(f"{type(veiculo).__name__} ({veiculo.getPlaca()}): {consumo:.2f} litros ou kWh")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Erro: {e}")

try:
    distancia = float(input("Digite a distancia a ser percorrida em KM: "))
except ValueError:
    print("Valor inválido para distância! Digite um número.")
    distancia = None

if distancia is not None:
    print("Escolha o tipo de veiculo: ")
    print("1 - Carro")
    print("2 - Caminhão")
    print("3 - Moto")
    print("4 - Adicionar Nova placa")

    opcao = input("Digite o numero correspondente à sua escolha: ")

    veiculo = None
    try:
        if opcao == "1":
            veiculo = Carro("Gol", "VW", 2020, "Branco", "ABC1234", 4)
        elif opcao == "2":
            veiculo = Caminhao("FH 540", "Volvo", 2022, "Branco", "XYZ1234", 30.0, 6)
        elif opcao == "3":
            veiculo = moto("CG 160", "Honda", 2021, "Vermelha", "ABC5678", 160)
        elif opcao == "4":
            print(
                "Para fazer a criação das placas é necessario seguir esse padrão (LLLNLNN)."
            )
            try:
                novaPlaca = input("Digite a sua nova placa seguindo o padrão: ")
                print(f"Nova placa cadastrada: {novaPlaca}")
            except Exception as e:
                print(f"Erro ao cadastrar: {e}")

        else:
            raise ValueError("Tipo de veículo inexistente!")
    except Exception as e:
        print(f"Erro ao criar o veículo: {e}")
        veiculo = None

    if veiculo:
        consumo = veiculo.calcular_consumo(distancia)
        print(f"Consumo para {distancia} km: {consumo:.2f} litros ou kWh")
