class Vehiculo():
    def __init__(self,placa,marca,modelo,cor,numero_rodas):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor do vehiculo")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join({f'{chave}={valor}' for chave, valor in self.__dict__.items()})}"

class Carro(Vehiculo):
    pass


class Motocicleta(Vehiculo):
    pass

class Caminhao(Vehiculo):
    #é necessario declarar os atributos da classse pai
    def __init__(self, carregado,placa,marca,modelo,cor,numero_rodas):
        #ao usar super().__init__(atributos pai) posso tratar como herança importada para não ter que reescrever todos os atributos manualmente
        super().__init__(marca,modelo,placa, cor, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'SIM'if self.carregado else 'não estou carregado'} ")



moto1 = Motocicleta("123dsfe","Honda","hayabusa","Crimson-Red",2)
#moto1.ligar_motor()
print(moto1)

carro1 = Carro("153dswe","Jaguar","phantom","Crimson-Green",4)
#carro1.ligar_motor()
print(carro1)

caminhao1 = Caminhao(False, "153xrte","Scania","BR-7765","Maybach-blue",16,)
#caminhao1.ligar_motor()
#caminhao1.esta_carregado()
print(caminhao1)
