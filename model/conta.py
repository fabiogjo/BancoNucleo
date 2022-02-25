class Conta:

    def __init__(self, numero_da_conta, titular, saldo, limite):
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def get_limite(self):
        return self.__limite

    def get_saldo(self):
        return self.__saldo

    def get_numero_da_conta(self):
        return self.__numero_da_conta

    def get_titular(self):
        return self.__titular

    def extrato(self):
        return self.__saldo

    def depositar(self, valor):
        print("Depositando R$ {}...".format(valor))
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            print("Sacando valor {}".format(valor))
            self.__saldo -= valor
        else:
            print("Você nao tem saldo suficiente!")

    def tranferencia(self, valor, destino):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
            destino.__saldo -= valor
            print("Transferencia de R$ {} para conta {}, Titular: {}, efetuada com sucesso!".format(valor, destino.__numero_da_conta, destino.__titular))
        else:
            print("Você nao tem saldo suficiente!")




