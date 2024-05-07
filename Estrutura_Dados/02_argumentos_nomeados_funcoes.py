def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


dict_carro = {"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")# por não estar estruturado pode causar problemas
#se trocar os argumentos de ordem ocorrerá um erro
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")#a estrutura ajuda a não se confundir
#os dois asteriscos são para passar o dicionario pra função
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
salvar_carro(**dict_carro) #estrutura de dicionario ajuda mas imprecindivel os asteriscos(Kwargs)
