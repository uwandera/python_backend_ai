class Espírito:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        raise NotImplementedError("Método atacar deve ser implementado nas classes derivadas.")

class Fantasma(Espírito):
    def atacar(self):
        return f"{self.nome} lança uma rajada de energia sombria!"

class Guardião(Espírito):
    def atacar(self):
        return f"{self.nome} golpeia o inimigo com força elemental!"

# Exemplo de uso:
fantasma_1 = Fantasma("Amidamaru")
guardiao_1 = Guardião("Bason")

# Polimorfismo: mesmo método chamado em diferentes classes produz resultados diferentes
print(fantasma_1.atacar())
print(guardiao_1.atacar())

'''
In this example:

The Espírito class is the base class representing spirits from the Shaman King universe. 
It has an attribute nome (name) and a method atacar() (attack), 
which raises a NotImplementedError to ensure that it must be implemented in derived classes.
The Fantasma class inherits from Espírito and represents a ghost spirit. 
It overrides the atacar() method to provide an attack specific to ghost spirits.
The Guardião class also inherits from Espírito and represents a guardian spirit. 
It overrides the atacar() method to provide an attack specific to guardian spirits.
In the example usage, we create instances of Fantasma (Amidamaru) and Guardião (Bason) and call the atacar() method on each. 
Despite calling the same method, each subclass provides its own implementation of the attack, demonstrating polymorphism.

'''