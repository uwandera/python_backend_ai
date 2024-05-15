from abc import ABC, abstractmethod 


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 #todos os atributos são privados
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod #class methods
    def nova_conta(cls,cliente, numero):#recebe cliente e numero
        return cls(numero, cliente)#retorna uma instancia de conta

    @property #não sei pra que serve esa propriedade
    def saldo(self):
        return self._saldo
    
        
    @property #usamos para definir a usabilidade de atributos privados que não podem ser modificados
    def numero(self):
        return self._numero
    
    @property # mapeando os métodos para serem ultilizados pelo inicializador da conta
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ a operação falhou, valor informado não está disponível!")



class ContaCorrente(Conta):
    def _limite():
        pass
    def _limite_saques(): 
        pass

class Historico(Conta, Transacao):
    def adicionar_transacao(cls, transacao):
        pass

#class abstrata
class Transacao(ABC):
    pass


class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

class Cliente:
    #construtor de cliente
    def __init__(self, endereco):
        self.endereco = endereco #endereço do cliente
        self.contas = [] #lista de contas de 1 cliente, pois pode ter muitas contas
        
        #registrador de transacao que usa método de outra class
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        #adicionando a nova conta na lista do cliente
        self.contas.append(conta)

#no diagrama UML vemos que Pessoa fisica deriva de cliente
class PessoaFisica(Cliente):
#ao inicializar a pessoa física usamos a notação de super().__init__() para dar referencia ao atributos herdados
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf