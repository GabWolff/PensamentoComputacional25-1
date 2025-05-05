class Livros:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual
        

    def avancar_pagina(self):
        if self.pagina_atual < self.numero_paginas:
            self.pagina_atual += 1
            print("Passou para a próxima página.")
        else:
            print("Você já está na última página.")

            
    def voltar_pagina(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            print("Você retornou uma página.")
        else:
            print("Não pode mais voltar, já está na primeira página.")

            
    def exibir_infos(self):
        print(f"O livro '{self.titulo}', escrito por {self.autor}, foi publicado em {self.ano_publicacao}.")
        print(f"Ele tem {self.numero_paginas} páginas. Página atual: {self.pagina_atual}")

        
        