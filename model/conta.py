
class Conta:

    def __init__(self, numero_da_conta, titular, saldo, cheque_especial, limite):
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__cheque_especial = cheque_especial
        self.__limite = limite


    def get_cheque_especial(self):
        return self.__cheque_especial

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

    def limite(self):
        pass

    def depositar(self, valor):
        print("Depositando R$ {}...".format(valor))
        if self.__saldo <= 0:
            #calculo negativo
            devendo = self.__saldo + valor

            #atualiza cheque especial
            self.__cheque_especial += devendo

            #atualiza saldo
            self.__saldo += valor

            #atualiza cheque especial
            self.__cheque_especial += valor

            #atualiza limite
            self.__limite = self.__saldo + self.__cheque_especial
        else:
            self.__saldo += valor

            #atualiza limite
            self.__limite = self.__saldo + self.__cheque_especial





    def sacar(self, valor):
        if valor <= self.__saldo:

            self.__saldo -= valor

            # atualiza limite
            self.__limite = self.__saldo + self.__cheque_especial
            print("Saque de R$ {} efetuado com sucesso!".format(valor))
        elif valor <= self.__limite:



            self.__cheque_especial -= valor - self.__saldo

            self.__saldo = 0


            # calculo negativo
            devendo = self.__saldo - valor

            # atualiza cheque especial
            self.__cheque_especial -= devendo



            print("Saque de R$ {} efetuado com sucesso!\nUtilizados R$ {} do limite da conta ".format(valor, devendo))
        else:
            print("Você nao tem saldo suficiente!")

    def tranferencia(self, valor, destino):
        if valor <= (self.__saldo):
            self.__saldo -= valor
            destino.__saldo += valor
            print("Transferencia de R$ {} para conta {}, Titular: {}, efetuada com sucesso!".format(valor, destino.__numero_da_conta, destino.__titular))
        elif valor <= self.__limite:
            self.__saldo -= valor
            self.__cheque_especial -= valor
            self.__limite -= valor
            utilizando_limite = abs(self.get_saldo() - self.get_limite())
            print("Transferencia de R$ {} para conta {}, Titular: {}, efetuada com sucesso!\nUtilizados R$ {} do limite da conta.".format(valor, destino.__numero_da_conta, destino.__titular, utilizando_limite))
        else:
            print("Você nao tem saldo suficiente!")




