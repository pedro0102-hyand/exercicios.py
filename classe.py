lass Conta:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
minha_conta = Conta("1234-5", "Léo", 1134)
minha_conta.alterarNome("Pedro")
minha_conta.deposito(500)
minha_conta.saque(200)
print(minha_conta.nome_correntista)
print(minha_conta.saldo)
