#modelo hibrido posição e nome
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido pois a função é hibrida! inpondo onde é nome e onde é posição

#modelo apenas por nome
def criar_garagem(*, rua, tamanho, capacidade_maxima):
    print(rua, tamanho,capacidade_maxima)

criar_garagem(rua="rua sete", tamanho="400m2", capacidade_maxima="20 carros") # apenas por nome