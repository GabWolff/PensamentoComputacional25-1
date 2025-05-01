# Verifica se o filme já foi cadastrado
def filme_existe(nome, lista_nomes):
    for existente in lista_nomes:
        if existente.lower() == nome.lower():
            return True
    return False

# Retorna o índice do filme na lista
def encontrar_indice(nome, lista_nomes):
    for i, existente in enumerate(lista_nomes):
        if existente.lower() == nome.lower():
            return i
    return -1

# Pede o nome do filme
def solicitar_nome():
    return input("Digite o nome do filme (ou 'sair' para encerrar): ").strip()

# Pede a nota e valida
def solicitar_nota(nome):
    try:
        nota = float(input(f"Digite a nota para '{nome}' (de 0.0 a 10.0): "))
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            print("⚠️ A nota deve estar entre 0.0 e 10.0.")
            return None
    except ValueError:
        print("⚠️ Por favor, insira um número válido.")
        return None

# Mostra os resultados
def exibir_resultados(nomes, notas):
    print("\n📽️ Lista de filmes cadastrados e suas notas:")
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]} — Nota: {notas[i]}")
    if notas:
        media = sum(notas) / len(notas)
        print(f"\n⭐ Nota média dos filmes: {media:.2f}")
    else:
        print("\nNenhum filme foi cadastrado.")

# Edita a nota de um filme
def editar_filme(nomes, notas):
    nome = input("Digite o nome do filme que deseja editar: ").strip()
    indice = encontrar_indice(nome, nomes)
    if indice == -1:
        print("⚠️ Filme não encontrado.")
        return
    nova_nota = solicitar_nota(nome)
    if nova_nota is not None:
        notas[indice] = nova_nota
        print("✅ Nota atualizada com sucesso!")

# Remove um filme
def remover_filme(nomes, notas):
    nome = input("Digite o nome do filme que deseja remover: ").strip()
    indice = encontrar_indice(nome, nomes)
    if indice == -1:
        print("⚠️ Filme não encontrado.")
        return
    nomes.pop(indice)
    notas.pop(indice)
    print("🗑️ Filme removido com sucesso!")

# Programa principal
nomes = []
notas = []

print("🎬 Bem-vindo ao Festival de Filmes Pessoais!")

while True:
    print("\nO que você deseja fazer?")
    print("1 - Adicionar novo filme")
    print("2 - Editar nota de um filme")
    print("3 - Remover um filme")
    print("4 - Exibir todos os filmes")
    print("5 - Sair")

    escolha = input("Digite o número da opção: ").strip()

    if escolha == "1":
        if len(nomes) >= 1000:
            print("⚠️ Limite de 1000 filmes atingido.")
            continue
        nome = solicitar_nome()
        if nome.lower() == "sair":
            break
        if filme_existe(nome, nomes):
            print("⚠️ Esse filme já foi cadastrado!")
            continue
        nota = solicitar_nota(nome)
        if nota is not None:
            nomes.append(nome)
            notas.append(nota)

    elif escolha == "2":
        editar_filme(nomes, notas)

    elif escolha == "3":
        remover_filme(nomes, notas)

    elif escolha == "4":
        exibir_resultados(nomes, notas)

    elif escolha == "5":
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")

print("\n🎞️ Encerrando o programa. Aqui está seu festival:")
exibir_resultados(nomes, notas)
