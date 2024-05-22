from abc import ABC, abstractclassmethod,  abstractmethod, abstractproperty #ainda não sei pq essas propriedades estão cortadas
from datetime import datetime
import textwrap


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
        
    

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes #esta sendo usada na classe conta corrente
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H-%M-%s")
            }
        )

#class abstrata
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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




def menu():
    menu = """ \n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\Listar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==>  """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf ]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_clientes(cliente):
    if not cliente.contas:
        print("\n@@@@@ Cliente não possui conta! @@@@@")
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n @@@@@@ Cliente não encontrado! @@@@@@")
        return
    
    valor = float(input("Informe o valor do deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):



def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            de(clientes)
            
        elif opcao == "s":
           
        
        elif opcao == "e":
            

        elif opcao == "nu":
           

        elif opcao == "nc":
           
            
        
        elif opcao == "lc":
            

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada