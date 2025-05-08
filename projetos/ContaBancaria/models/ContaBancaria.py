import time

class ContaBancaria:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''
    def __init__(self, titular, saldo = 1000, limite = [] , historico = 0):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
        
    def depositar(self, valor, remetente = None):
        '''
        Objetivo: Método que realiza do depósito na conta bancária.
        Entrada: Valor(float) e remetente (String)
        Return: True, se a operação fopi realizada com sucesso, False, se a operação não foi realizada

        '''
        op = 1
        #Detecta se é uma transferencia
        if remetente != None:
            op = 2
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": op,
                                "remetente": remetente,
                                "destinatario": "",
                                "valor": valor,
                                "saldo": self.saldo,
                                "dataetempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é invalido") 
            return False           
        
    def sacar(self, valor, destinatario = None):
        '''
        Objetivo: Método que realiza do depósito na conta bancária.
        Entrada: Valor(float) e destinatario (String)
        Return: True, se a operação fopi realizada com sucesso, False, se a operação não foi realizada

        '''
        op = 0
        #Detecta se é uma transferencia
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Saque realizado!")
            return True
        else:
            a = input(f"Deseja utilizar o Limite?({self.limite}) [s] ou [n]")
            if a == "s": 
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    self.historico.append({"operacao": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
                    print("Saque realizado")
                    return True
                else:
                    print("Saldo e Limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
            return False
            
    def transferir(self, destinatario, valor):
        """
        Objetivo: método para transferir um valor entre duas contas
        entrada: valor (float) e obj ContaBancaria do destinatario
        Saida: se ok -> True, se NOK -> False
        """
        # Se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # deposita na conta do destinatario
            destinatario.depositar(valor, self.titular)
    
 

    def exibirHistorico(self):
        print("Histórico de transações:")
        for transacao in self.historico:
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
            

    #def exibirSaldo(self):