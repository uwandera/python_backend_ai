def mensagem(nome):
    print(f" executandodo nome")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print("executando a mensagem longa")
    return f'olá tudo bem com vo~ce {nome}'

def executar(funcao, nome):#pra poder usar funcoes aninhadas é necessario passar o parametro que deseja dentro da funcao "ninho"
    print('executando a funcao executar')
    return funcao(nome)#chumbadão não é a solução correta



print(executar(mensagem, "jiboia"))
print(executar(mensagem_longa, "skywalker"))


def principal():
    print("Executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao2():
        print("executando a funcao 2")

    funcao_interna()
    funcao2()
