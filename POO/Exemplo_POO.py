class Objeto:
    def __init__(self, atributo1, atributo2, atributo3, atributo4, atributo5):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3
        self.atributo4 = atributo4
        self.atributo5 = atributo5

# Função para receber os atributos do usuário e criar um objeto
def criar_objeto():
    atributo1 = input("Digite o valor do atributo 1: ")
    atributo2 = input("Digite o valor do atributo 2: ")
    atributo3 = input("Digite o valor do atributo 3: ")
    atributo4 = input("Digite o valor do atributo 4: ")
    atributo5 = input("Digite o valor do atributo 5: ")
    
    # Criar e retornar o objeto com os atributos fornecidos
    return Objeto(atributo1, atributo2, atributo3, atributo4, atributo5)

# Programa principal
if __name__ == "__main__":
    novo_objeto = criar_objeto()
    print("Objeto criado com sucesso!")
    print("Atributo 1:", novo_objeto.atributo1)
    print("Atributo 2:", novo_objeto.atributo2)
    print("Atributo 3:", novo_objeto.atributo3)
    print("Atributo 4:", novo_objeto.atributo4)
    print("Atributo 5:", novo_objeto.atributo5)
