class Personagem:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def apresentar(self):
        print(f"Meu nome é {self.nome} e sou um(a) {self.raca}.")

class Humano(Personagem):
    def __init__(self, nome, cidade_origem):
        super().__init__(nome, "Humano")
        self.cidade_origem = cidade_origem

    def apresentar(self):
        super().apresentar()
        print(f"Sou da cidade de {self.cidade_origem}.")

class Elfo(Personagem):
    def __init__(self, nome, reino):
        super().__init__(nome, "Elfo")
        self.reino = reino

    def apresentar(self):
        super().apresentar()
        print(f"Sou do reino de {self.reino}.")


# Exemplo de uso:
aragorn = Humano("Aragorn", "Minas Tirith")
legolas = Elfo("Legolas", "Lothlórien")

aragorn.apresentar()
legolas.apresentar()

'''
In this example:

The Personagem class is the base class, representing any character in Middle-earth. 
It has attributes nome (name) and raca (race), and a method apresentar() (present) to introduce the character.
The Humano class inherits from Personagem and represents a human character. 
It adds an attribute cidade_origem (hometown) and overrides the apresentar() method to include the hometown.
The Elfo class also inherits from Personagem and represents an elf character. 
It adds an attribute reino (kingdom) and overrides the apresentar() method to include the kingdom.
In the example usage, we create instances of Humano (Aragorn) and Elfo (Legolas) and 
 the apresentar() method on each to see their introductions.
'''