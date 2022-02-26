import time


class Conta:

    def __init__(self, numero_da_conta, titular, saldo, cheque_especial_disponivel, max_cheque_especial, senha):
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__cheque_especial_disponivel = cheque_especial_disponivel
        self.__max_cheque_especial = max_cheque_especial
        self.__senha = senha


    def get_cheque_especial(self):
        return self.__cheque_especial_disponivel

    def get_saldo(self):
        return self.__saldo

    def get_numero_da_conta(self):
        return self.__numero_da_conta

    def get_titular(self):
        return self.__titular

    def extrato(self):
        return self.__saldo

    def get_max_cheque_especial(self):
        return self.__max_cheque_especial

    def get_limite(self):
        return self.get_saldo() + self.get_cheque_especial()

    def max_cheque_especial(self):
        return self.__cheque_especial_disponivel

    def msg_deposito(self, valor):
        for i in range(3):
            print("Depositando R$ {}..".format(valor))
            time.sleep(1)


    def depositar(self, valor):
        self.msg_deposito(valor)

        if (self.__cheque_especial_disponivel + valor) <= self.__max_cheque_especial:

            self.__cheque_especial_disponivel += valor

        elif (self.__cheque_especial_disponivel + valor) > self.__max_cheque_especial:

            saldo_negativo = self.__max_cheque_especial - self.__cheque_especial_disponivel

            valor_com_desconto = valor - saldo_negativo

            self.__cheque_especial_disponivel += saldo_negativo

            self.__saldo += valor_com_desconto


    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque de R$ {} efetuado com sucesso!".format(valor))

        elif valor <= self.get_limite():
            valor_necessario = self.__saldo - valor
            self.__cheque_especial_disponivel -= abs(valor_necessario)
            self.__saldo = 0
            self.get_limite()
            print("Saque de R$ {} efetuado com sucesso!\nUtilizados R$ {} do limite da conta ".format(valor, valor_necessario))
        else:
            print("Você nao tem saldo suficiente!")

    def tranferencia(self, valor, destino):
        if valor <= self.__saldo:
            self.__saldo -= valor
            destino.__saldo += valor
            print("Transferencia de R$ {} para conta {}, Titular: {}, efetuada com sucesso!".format(valor, destino.__numero_da_conta, destino.__titular))
        elif valor <= self.get_limite():
            valor_necessario = self.__saldo - valor
            self.__cheque_especial_disponivel -= abs(valor_necessario)
            self.__saldo = 0
            self.get_limite()
            destino.depositar(valor)
            print("Transferencia de R$ {} para conta {}, Titular: {}, efetuada com sucesso!\nUtilizados R$ {} do limite da conta.".format(valor, destino.__numero_da_conta, destino.__titular, valor_necessario))
        else:
            print("Você nao tem saldo suficiente!")




