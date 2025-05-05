from Models.Livros import Livros

# Criação do objeto
livro = Livros("1984", "George Orwell", 1949, 328, 1)

# Testes diretos dos métodos
livro.exibir_infos()
livro.avancar_pagina()

livro.exibir_infos()
livro.voltar_pagina()

livro.exibir_infos()

# Exemplos comentados caso queira testar mais:
# livro.voltar_pagina()
# livro.avancar_pagina()
# livro.exibir_infos()