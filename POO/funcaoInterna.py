def principal():
    print("Executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao2():
        print("executando a funcao 2")

    funcao_interna()
    funcao2()


#funcao_interna()

principal()# as funcoes internas e funcoa 2 sao definidas dentro da principal, logo só sao definidas dentro da principal e não tem contexto fora