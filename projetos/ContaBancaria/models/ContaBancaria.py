import time

class ContaBancaria:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''
    def __init__(self, titular: str, saldo: float, limite: float, chavePix: list, historico: list = None):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chavePix = chavePix  # lista de chaves Pix
        self.__historico = historico if historico is not None else []  # OBS: Se um histórico for passado, usa ele; senão, cria uma lista vazia para começar um novo histórico.

    def depositar(self, valor: float, remetente: str) -> bool:
        '''
        Realiza um depósito na conta.
        valor: valor a ser depositado
        remetente: nome do remetente (None se for depósito comum, string se for transferência)
        Retorna True se o depósito foi realizado, False caso contrário.
        '''
        op = 1  # 1 = depósito comum
        # Se tiver remetente, é uma transferência recebida
        if remetente is not None:
            op = 2
        if valor > 0:
            self.__saldo += valor
            # Adiciona a operação ao histórico
            self.__historico.append({
                "operacao": op,
                "remetente": remetente,
                "destinatario": "",
                "valor": valor,
                "saldo": self.__saldo,
                "dataetempo": int(time.time())
            })
            return True
        else:
            print(f"O valor {valor} é inválido")
            return False

    def sacar(self, valor: float, destinatario: str) -> bool:
        '''
        Realiza um saque na conta.
        valor: valor a ser sacado
        destinatario: nome do destinatário (None se for saque comum, string se for transferência)
        Retorna True se o saque foi realizado, False caso contrário.
        '''
        op = 0  # 0 = saque comum
        # Se tiver destinatário, é uma transferência enviada
        if destinatario is not None:
            op = 2
        if valor <= self.__saldo:
            self.__saldo -= valor
            # Adiciona a operação ao histórico
            self.__historico.append({
                "operacao": op,
                "remetente": self.__titular,
                "destinatario": destinatario,
                "valor": valor,
                "saldo": self.__saldo,
                "dataetempo": int(time.time())
            })
            print("Saque realizado!")
            return True
        else:
            # Se não tem saldo suficiente, pergunta se quer usar o limite
            a = input(f"Deseja utilizar o Limite?({self.__limite}) [s] ou [n] ")
            if a == "s":
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    self.__historico.append({
                        "operacao": op,
                        "remetente": self.__titular,
                        "destinatario": destinatario,
                        "valor": valor,
                        "saldo": self.__saldo,
                        "dataetempo": int(time.time())
                    })
                    print("Saque realizado")
                    return True
                else:
                    print("Saldo e Limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
            return False

    def transferir(self, destinatario, valor: float):
        """
        Realiza uma transferência para outra conta.
        destinatario: objeto ContaBancaria do destinatário
        valor: valor a ser transferido
        Retorna True se a transferência foi realizada, False caso contrário.
        """
        if self.sacar(valor, destinatario.titular):
            destinatario.depositar(valor, self.__titular)
            return True
        return False

    def exibirHistorico(self) -> None:
        '''
        Exibe o histórico de transações da conta.
        '''
        print("Histórico de transações:")
        for transacao in self.__historico:
            dt = time.localtime(transacao["dataetempo"])
            print(
                f"\nOp: {transacao['operacao']}"
                f"\nRemetente: {transacao['remetente']}"
                f"\nDestinatário: {transacao['destinatario']}"
                f"\nValor: {transacao['valor']}"
                f"\nSaldo: {transacao['saldo']}"
                f"\nData e tempo:"
                f" {dt.tm_mday}/{dt.tm_mon}/{dt.tm_year}"
                f"\nAs: {dt.tm_hour}:{dt.tm_min}:{dt.tm_sec}")

    def atualizar_chaves_pix(self, novas_chaves):
        '''
        Atualiza as chaves Pix da conta.
        novas_chaves: lista de novas chaves Pix
        '''
        if isinstance(novas_chaves, list):
            self.__chavePix = novas_chaves
        else:
            print("A chave Pix deve ser uma lista.")


    # Getters para acessar atributos privados
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def chavePix(self):
        return self.__chavePix

    @property
    def historico(self):
        return self.__historico