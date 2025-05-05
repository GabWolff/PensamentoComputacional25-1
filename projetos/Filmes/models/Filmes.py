class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao
        self.__avaliacao = avaliacao

    def avaliar(self, nota: float):
        if 0 <= nota <= 10:
            self.__avaliacao = nota
            print(f"Avaliação atualizada para {nota}/10.")
        else:
            print("Nota inválida. Informe uma nota entre 0 e 10.")

    def exibir_informacoes(self):
        print("===== INFORMAÇÕES DO FILME =====")
        print(f"Título: {self.__titulo}")
        print(f"Gênero: {self.__genero}")
        print(f"Duração: {self.__duracao} minutos")
        print(f"Avaliação: {self.__avaliacao}/10")
        print("================================\n")
