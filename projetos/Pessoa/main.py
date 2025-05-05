from models.Pessoa import Pessoa

# Criação do objeto pessoa
pessoa_teste = Pessoa("Gabriel", 25, 1.75)

# Testando os métodos
pessoa_teste.exibir_informacoes()
pessoa_teste.aniversario()
pessoa_teste.exibir_informacoes()
pessoa_teste.crescer(0.05)
pessoa_teste.exibir_informacoes()
pessoa_teste.crescer(-0.02)  # teste com valor inválido
