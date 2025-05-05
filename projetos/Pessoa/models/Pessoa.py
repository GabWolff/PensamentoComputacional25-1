class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def aniversario(self):
        self.__idade += 1
        print(f"{self.__nome} fez aniversário! Agora tem {self.__idade} anos.")

    def crescer(self, valor: float):
        if valor > 0:
            self.__altura += valor
            print(f"{self.__nome} cresceu! Agora tem {self.__altura} metros de altura.")
        else:
            print("Valor de crescimento inválido. O valor deve ser positivo.")

    def exibir_informacoes(self):
        print("===== INFORMAÇÕES DA PESSOA =====")
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade} anos")
        print(f"Altura: {self.__altura} metros")
        print("================================\n")
