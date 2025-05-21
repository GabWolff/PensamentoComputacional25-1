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
veiculos_lista = [
    Carro(
        modelo="Gol",
        marca="Volkswagen",
        ano=2018,
        cor="Branco",
        placa="XYZ-9876",
        nPortas=4,
    ),
    moto(
        modelo="CG 160",
        marca="Honda",
        ano=2021,
        cor="Vermelha",
        placa="ABC-5678",
        cilindradas=160,
    ),
    Caminhao(
        modelo="FH 540",
        marca="Volvo",
        ano=2022,
        cor="Branco",
        placa="CAM1234",
        capacidade_carga=30.0,
        eixos=6,
    ),
    veiculo_eletrico(
        modelo="Tesla Model 3",
        marca="Tesla",
        ano=2023,
        cor="Preto",
        placa="ELT-2023",
        fipe=350000,
    ),
    Carro(
        modelo="Onix",
        marca="Chevrolet",
        ano=2020,
        cor="Prata",
        placa="XYZ-9876",
        nPortas=4,
    ),  # placa repetida com Gol
    moto(
        modelo="Fazer 250",
        marca="Yamaha",
        ano=2022,
        cor="Azul",
        placa="ABC-5678",
        cilindradas=250,
    ),  # placa repetida com CG 160
    veiculo_eletrico(
        modelo="Leaf",
        marca="Nissan",
        ano=2021,
        cor="Branco",
        placa="ELT-2023",
        fipe=200000,
    ),  # placa repetida com Tesla
    Carro(
        modelo="Fox",
        marca="Volkswagen",
        ano=2019,
        cor="Preto",
        placa="ZZZ9999",
        nPortas=4,
    ),  # placa igual à moto abaixo
    moto(
        modelo="Biz",
        marca="Honda",
        ano=2020,
        cor="Preta",
        placa="ZZZ9999",
        cilindradas=125,
    ),  # placa igual ao Fox
    veiculo_eletrico(
        modelo="Bolt",
        marca="Chevrolet",
        ano=2022,
        cor="Azul",
        placa="XYZ-9876",
        fipe=300000,
    ),  # placa igual ao Gol e Onix
]

print("\n--- Verificando veículos duplicados pela placa ---")
duplicados = set()
for i in range(len(veiculos_lista)):
    for j in range(i + 1, len(veiculos_lista)):
        if veiculos_lista[i] == veiculos_lista[j]:
            chave = tuple(
                sorted(
                    [
                        veiculos_lista[i].getPlaca(),
                        type(veiculos_lista[i]).__name__,
                        type(veiculos_lista[j]).__name__,
                    ]
                )
            )
            if chave not in duplicados:
                duplicados.add(chave)
                print(
                    f"Duplicado: {type(veiculos_lista[i]).__name__} e {type(veiculos_lista[j]).__name__} com placa {veiculos_lista[i].getPlaca()}"
                )
                print(f"  1: {veiculos_lista[i]}")
                print(f"  2: {veiculos_lista[j]}\n")

if not duplicados:
    print("Nenhum veículo duplicado encontrado.")
else:
    print(f"Total de pares duplicados encontrados: {len(duplicados)}")

# Demonstração de polimorfismo:
print("\n--- Demonstração de polimorfismo na comparação ---")
carro_dup = Carro("Fox", "Volkswagen", 2019, "Preto", "ZZZ9999", 4)
moto_dup = moto("Biz", "Honda", 2020, "Preta", "ZZZ9999", 125)
if carro_dup == moto_dup:
    print("Carro e Moto são considerados iguais pois possuem a mesma placa.")
else:
    print("Carro e Moto são diferentes.")
