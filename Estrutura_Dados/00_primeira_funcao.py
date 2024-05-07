#funções são codigos reutilizaveis
#bloco de codigo 
#conjunto de entradas e saidas
#programação estruturada
def exibir_mensagem():#definição de uma função, não há parâmetros
    print("Olá mundo!") #oque a função irá fazer


def exibir_mensagem_2(nome):#parametro nome
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):#parametro nome  com a possibilidade de não precisar inserir um parametro na chamada da função
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(7.3)#pelo parametro não ter sido definido tipo, entra qualquer coisa
exibir_mensagem_3(89)
exibir_mensagem_3(nome=8)
