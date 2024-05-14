'''
  métodos de de classe estão ligados à classe e nao ao objeto.
  eles tem acesso ao estado da classe, pois recebem um parametro 
  que aponta para a classe e não para a instancia do objeto

  self = cls (convenção)

  métodos estáticos não recebe um primeiro argumento explicito. 
  ele tambem e um método vinculado à classe e não ao objeto da classe.
  este método não pode acessar ou modificar o estado da classe.
  ele está presente em uma classe porque faz sentido que o método esteja presente na classe
  
'''
#forma não padronizada deixando valores de None para variaveis nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #criando metodos de classe para ter contexto de classe
    @classmethod
    def data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        #idade = 2024 - ano
        return cls(nome, ano)
    
    @staticmethod #não precisa do contexto de classe
    def maior_idade(idade):
        return idade >= 18
    

p = Pessoa("Thomas", 28)
#print(p.nome, p.idade)

p2 = Pessoa.data_nascimento(1995,"fevereiro",29,"Farrorios")

#print(p2)
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(19))