class Conta:
    def __init__(self, nro_agencia, saldo=0):
        #_saldo é uma variavel privada e a convenção do pytho diz isso pelo undeline no inicio
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        #devemos acessar as variaveis privadas no escopo da classe e não fora
        self._saldo += valor
        
    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo




conta1 = Conta("0001",100)
#conta1._saldo +=100 #driblando o encapsulamento
conta1.depositar(100)
#print(conta1._saldo)# não usar ou manipular variaveis privadas, usar methodos para maniipularlas
print(conta1.nro_agencia)
print(conta1.mostrar_saldo())