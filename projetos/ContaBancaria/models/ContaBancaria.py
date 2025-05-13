import time

class ContaBancaria:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''
    def __init__(self, titular: str, saldo: float, limite: float, chavePix: list, historico: list = []) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chavePix = chavePix
        self.__historico = historico if historico is not None else []
        

    def depositar(self, valor: float, remetente: str) -> bool:
        '''
        Objetivo: Método que realiza o depósito na conta bancária.
        Entrada: Valor(float) e remetente (String)
        Return: True, se a operação foi realizada com sucesso, False, se a operação não foi realizada
        '''
        op = 1
        # Detecta se é uma transferência
        if remetente is not None:
            op = 2
        if valor > 0:
            self.__saldo += valor
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
        Objetivo: Método que realiza o saque na conta bancária.
        Entrada: Valor(float) e destinatário (String)
        Return: True, se a operação foi realizada com sucesso, False, se a operação não foi realizada
        '''
        op = 0
        # Detecta se é uma transferência
        if destinatario is not None:
            op = 2
        if valor <= self.__saldo:
            self.__saldo -= valor
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
            a = input(f"Deseja utilizar o Limite?({self.__limite}) [s] ou [n] ")
            if a == "s":
                if (self.saldo + self.__limite) >= valor:
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

    def transferir(self, destinatario: str, valor: float):
        """
        Objetivo: método para transferir um valor entre duas contas
        entrada: valor (float) e obj ContaBancaria do destinatário
        Saída: se ok -> True, se NOK -> False
        """
        if self.sacar(valor, destinatario.titular):
            destinatario.depositar(valor, self.__titular)

    def exibirHistorico(self) -> None:
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
            
    
    def chavePix(self, novas_chaves):
        if isinstance(novas_chaves, list):
            self.__chavePix = novas_chaves
        else:
            print("A chave Pix deve ser uma lista.")

            
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def historico(self):
        return self.__historico  # CORRIGIDO aqui

    @property
    def limite(self):
        return self.__limite

    @property
    def chavePix(self):
        return self.__chavePix  # Getter da chavePix funcionando corretamente
