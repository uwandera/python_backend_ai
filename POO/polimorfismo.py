class Passaro:
    def voar(self):
        print("voando..")

class Pardal(Passaro):
    def voar(self):
        return super().voar() # aqui estamos usando a implementação do método base
    

class Aveztruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

#Exemplo não tão usual para ganhar um método sem ter que refazelo usando herança e polimorfismo
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ....")

#polimorfismo introduzido pois todo obj vai ser filho da classe base e assim carregando sentidos diferentes
def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Aveztruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())
