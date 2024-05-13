#cor; modelo ;ano; valor --> varacteristicas
#buzinar e correr ---> comportamento
#Classe bicilcleta

class Bicicleta:
    #pass é um comando que fecha classe
    # self é uma referencia explicita para o objeto, queremos dizer que essa é a instancia do objeto passado
    # c++ usa this.atributo para fazer a referencia
    #usar self em python como boa pratica, ,mas pode encontrar this.atributo tbm
    #metodo construtor, inicializar com os atributos do objeto
    def __init__(self , cor, modelo, ano, valor):
        self.cor = cor #atributos da classe {caracteristicas da classe}
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
        
    #Comportamento definidos por métodos
    # def define método
    # definir um argumento (referencia explicita de objeto : self)     
    def buzinar(self):
        print("*** PRIIIM PRIIIM ***")
    def parar(self):
        print("paaaraandoooo aa bicKE!")
        print("*** Bicke Parada! ***")
    def correr(self):
        print("VRRRUUUUUUUMMMMMMM !")

    #nomear o método com o nome do atributo pode gerar problemas
    #mas em python os atributos são acessiveis publicamente
    def cor(self):
        return self.cor

    def trocar_marcha(self, nro_marcha):
        print("CLickLCLAKR!")

        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                 print("..marcha trocada!")
            else:
                print("não foi possivel trocar de marcha!")
    
    #método ultilizado para retornar os atributos manualmente
   # def __str__(self) -> str:
       # return f"Bicicleta: Cor:{self.cor}, Modelo:{self.modelo}, Ano:{self.ano}, Valor:{self.valor}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 
    #pegando a instancia do objeto(self) atributo para encontrar a classe(__class__) e assim pegando o __name__ que é o nome da classe
    #prestar atençao na abertura e fechamento das funções
    #codigo muito util para representações de classe
'''
b1 = Bicicleta("vermelha","CALOI_Fx447", 2015, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
'''
#o que o python faz quando: classe.metodo

b2 = Bicicleta("verde","AUDI_BMX_4233FX",1997,10500)
Bicicleta.buzinar(b2) #esta chamada é equivalente a
b2.buzinar()# esta chamada
print(b2.cor) #esta mensagem é suprimida ao usar o nome do atributo como o nome do método :<bound method Bicicleta.get_cor of <__main__.Bicicleta object at 0x000001BC37196840>>
b2.correr()
print(b2)#classe que instancia a função print sub classe criada e local da memória intanciado<__main__.Bicicleta object at 0x0000026BCC286870>
b2.trocar_marcha(0)#métodos precisam de argumentos tho!
