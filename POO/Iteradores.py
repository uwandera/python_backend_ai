# usar iteradores para manipular arquivos grandes
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
        

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2 #logica do programa de exemplo em questão e não tem haver com iteradores
        except IndexError:
            raise StopIteration
    


for i in MeuIterador(numeros=[1,2,3,4,3,4,6,7,8,9,0,8,7,5,4,32,2]):
    print(i)