from model.conta import Conta

seed = [

    Conta(1, "Fabio", 100, 1000),

    Conta(2, "Biel", 100, 1000)



]
def contas_abertas():
    contas_abertas = ''
    for indice, conta in enumerate(seed):
        contas_abertas += "({}) {} \n".format(indice + 1, conta.get_titular())
    return contas_abertas