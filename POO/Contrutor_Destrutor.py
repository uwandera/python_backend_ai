
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("miauuuu")


    def __del__(self):
        print("Destruindo este objeto do espaço de memoria alocado dinamicamente com python mas em c++ é necessario")

    def criarcachorro():
        c = Cachorro("Thor","preto", False)
        print(c.nome)


 

c = Cachorro("Croudie", "yellowe")
c.latir() 

criarcachorro()
    