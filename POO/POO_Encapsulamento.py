class Personagem:
    def __init__(self, nome, raca, poder):
        self.__nome = nome  # Encapsulated attribute
        self.__raca = raca  # Encapsulated attribute
        self.__poder = poder  # Encapsulated attribute

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}, sou da raça {self.__raca} e meu poder é {self.__poder}.")

    def get_nome(self):  # Getter method for __nome
        return self.__nome

    def set_poder(self, novo_poder):  # Setter method for __poder
        if novo_poder > 0:
            self.__poder = novo_poder
        else:
            print("O poder deve ser um número positivo.")

# Exemplo de uso:
goku = Personagem("Goku", "Saiyajin", 10000)
goku.apresentar()

# Tentativa de acesso direto ao atributo encapsulado (__nome)
# Isso resultará em um erro
# print(goku.__nome)

# Acessando o atributo encapsulado através do getter
print("Nome do personagem:", goku.get_nome())

# Alterando o poder do personagem usando o setter
goku.set_poder(15000)
goku.apresentar()

# Tentativa de atribuir um poder negativo
goku.set_poder(-5000)

'''
In this example:

The Personagem class represents characters from the Dragon Ball universe. 
It has encapsulated attributes __nome, __raca, and __poder (name, race, and power), 
prefixed with double underscores to indicate they are private.
The apresentar() method introduces the character, accessing the encapsulated attributes.
We have getter and setter methods for accessing and modifying the encapsulated attributes. 
The get_nome() method allows us to access the character's name, 
and the set_poder() method allows us to change the character's power. 
The setter method includes a validation to ensure that the power is a positive number.
In the example usage, we create an instance of Personagem (Goku), introduce him, 
and then demonstrate accessing the encapsulated attributes using the getter method and 
modifying the power using the setter method. We also attempt to directly access the encapsulated attribute (__nome), 
which results in an error, demonstrating data hiding.

'''