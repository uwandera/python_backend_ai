from abc import ABC, abstractmethod, abstractproperty 
#declarando os métodos que serão ultilizados

'''
interfaces definem oq a classe deve fazer, mas não como!

Forma como implementar algo de forma padrão e sai um resultado final

o conceito de interface é definir um contrato onde são declarados os métodos(o que deve ser feito) e suas respectivas assinaturas
em python utilizamos classes abstratas para criar contratos
classes abstratas nao podem ser instanciadas

conceito de classe abstrata
herança multipla

Abstract Based Class (abc module)
por padrao python não fornece classes abstratas
existe um módulo chamado abc que funciona como decorador de metodo de classe (classe base da cascata de herança)
registrando classes concretas como implementação da base abstrata
decorador: @abstractmethod

'''

#classe base recebendo o modulo ABC
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando Tv ...")

    def desligar(self):
        print("desligando a Tv ... Tv desligada!")

#nao colocar o @property nas funções de implementação ou acorrerá um erro        
    def marca(self):
        return "LG"

class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o Arcondicionado")

    def desligar(self):
        print("desligando o AR Condicionando")

#nao colocar o @property nas funções de implementação ou acorrerá um erro    
    def marca(self):
        return "Nokia"


controle = ControleTV()
controle.ligar()  
controle.desligar()
print(controle.marca()) 

controleAr = ControleArcondicionado()
controleAr.ligar()
print(controleAr.marca())

#quando temos contratos e classes abstratas, quando um método é abstrato, a classe filha é obrigada a implementar o método, recurso para padronização do codigo

