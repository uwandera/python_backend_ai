#a barra nos diz que os argumentos que a precedem são por posição e não aceitam ser nomeados, os argumentos depois da barra tato faz
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")#todos estão por posicao neste caso
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido pois é um parametro só por posição antes da barra
