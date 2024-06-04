def mensagem(nome):
    print(f" executandodo nome")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print("executando a mensagem longa")
    return f'olá tudo bem com vo~ce {nome}'
#passar a funcao como parametro a faz existir fora do seu contexto de definicao
def executar(funcao, nome):#pra poder usar funcoes aninhadas é necessario passar o parametro que deseja dentro da funcao "ninho"
    print('executando a funcao executar')
    return funcao(nome)#chumbadão não é a solução correta



print(executar(mensagem, "jiboia"))
print(executar(mensagem_longa, "skywalker"))



