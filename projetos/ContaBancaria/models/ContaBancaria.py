import time

class ContaBancaria:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
        
    def dpositar(self, valor):
        '''
        Objetivo: Método que realiza do depósito na conta bancária.
        Entrada: Valor(float)
        Return: True, se a operação fopi realizada com sucesso, False, se a operação não foi realizada

        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": 1,
                                "remetente": self.titular,
                                "destinatario": "",
                                "valor": valor,
                                "saldo": self.saldo,
                                "dataetempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é invalido") 
            return False           
        
    def sacar(self, valor):
        '''
        Objetivo: Método que realiza do depósito na conta bancária.
        Entrada: Valor(float)
        Return: True, se a operação fopi realizada com sucesso, False, se a operação não foi realizada

        '''
        
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": 0,
                                   "remetente": self.titular,
                                   "destinatario": "",
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
                    print("Saque realizado")
                    return True
                else:
                    print("Saldo e Limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
            return False
            
    #def transferir(self):
    
 

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
                f"Data e tempo:"
                f"{dt.tm_mday}/{dt.tm_mon}/{dt.tm_year} às:"
                f"{dt.tm_hour} : {dt.tm_min} : {dt.tm_sec}")
            

    #def exibirSaldo(self):