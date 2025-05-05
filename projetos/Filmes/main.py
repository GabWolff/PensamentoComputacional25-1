from models.Filmes import Filme

# Criação do objeto filme
filme_teste = Filme("A Origem", "Ficção Científica", 148, 8.5)

# Testando métodos
filme_teste.exibir_informacoes()
filme_teste.avaliar(9.2)
filme_teste.exibir_informacoes()
filme_teste.avaliar(11)  # teste com valor inválido
filme_teste.exibir_informacoes()
