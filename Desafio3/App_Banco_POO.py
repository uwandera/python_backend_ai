from abc import ABC, abstractclassmethod,  abstractmethod, abstractproperty #ainda não sei pq essas propriedades estão cortadas
from datetime import datetime


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
    
    def sacar(self, valor):# sacar é um pouco diferente de quando apenas usamos funções 
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ a operação falhou, valor informado não está disponível!")

        elif valor > 0:
            self._saldo -= valor #saque subitraido do valor em conta
            print("\n===== operação de saque efetuada com sucesso! =====")
            return True
        
        else:
            print("\n @@@@@@ operação inválida, tente novamente mais tarde @@@@@@")
            return False #sera que falso com falso da problema
        return False #pq esse return funciona com a identação aqui, para sempr retornar falso se não entrar na estrutura If Elif 


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n @@@@@ deposito realizado com sucesso")

        else:
            print("\n @@@@@ DEU RUIM, TENTA DENOVO QUEBRADA!")
            return False
        return True


class ContaCorrente(Conta): 
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor): #compressão de listas, pegamos o historico de transações, todas as transações desse histórico e verificando se o tipo de transação foi de saque  ta super estranho esse parte do códio e certeza q vai dar pau
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__])#pra que serve este aqui, o nome da classe saque 
                        #o len() esta sendo usado para contar a quantidade de saques 
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("\n @@@ limite de sauqe excedido, tente novamente mais tarde! @@@@")

        elif excedeu_saques:
            print("\n @@@@@ Numero de saques foi excedido, tente novamente mais tarde @@@@@")
    
        else:
            return super().sacar(valor)#essa classe está meio redundante, mas acho q faz sentido quando se trata de um grande banco
        
        return False # ao entrar no if ou no elif, damos o retorno padrão de false
    
    def __str__(self):
        return f'''\
            Agencia: \t{self.agencia}
            CC:\t\t{self.numero}
            Titular:\t{self.cliente.mome}
        '''
        
    

class Historico(Conta, Transacao):
    def adicionar_transacao(cls, transacao):
        pass

#class abstrata
class Transacao(ABC):
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