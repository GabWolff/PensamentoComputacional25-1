class MinhaEscxecao(Exception):
    pass    

def dividir(a, b):
    if b == 0:
        raise MinhaEscxecao("Divisão por zero não é permitida.")
    return a / b
# Exemplo de uso
try:
    print(dividir(10, 0))
except MinhaEscxecao as e:
    print(f"Erro: {e}")