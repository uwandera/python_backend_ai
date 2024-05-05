class Varinha:
    def __init__(self, núcleo, madeira, comprimento, nível_magia, dono):
        self.núcleo = núcleo
        self.madeira = madeira
        self.comprimento = comprimento
        self.nível_magia = nível_magia
        self.dono = dono

    def exibir_informações(self):
        print("Varinha de", self.dono)
        print("Núcleo:", self.núcleo)
        print("Madeira:", self.madeira)
        print("Comprimento:", self.comprimento)
        print("Nível de Magia:", self.nível_magia)

# Exemplo de uso da classe Varinha
if __name__ == "__main__":
    # Criando uma varinha para Bruxo
    nome_bruxo = input("Qual é seu nome jovem Bruxa(o): ")
    varinha_nome_bruxo = Varinha("Pena da Fênix", "Holly", "11 polegadas", "Alto", nome_bruxo)
    varinha_nome_bruxo.exibir_informações()

    # Criando uma varinha para Hermione Granger
    varinha_hermione = Varinha("Cabelo de Veela", "Videira", "10 3/4 polegadas", "Alto", "Hermione Granger")
    varinha_hermione.exibir_informações()
