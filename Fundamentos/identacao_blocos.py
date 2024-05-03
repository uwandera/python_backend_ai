#bloco de comandos do python são marcados por 1 tab ou 4 espaços
#identação obrigatória
#bloco de definição do método sacar

def sacar(valor): 
    saldo = 500
    #bloco do if que não enra
    if saldo >= valor:
        print("valor sacado!")#quatros espaços
        print("retire o seu dinheiro na boca do caixa.")
    #else esta omitido aqui e o comando sera feito de qualquer maneira
    print("obrigado por ser nosso cliente, tenha um bom dia!")



def depositar(valor):
    saldo = 500
    saldo += valor

sacar(399)
depositar(500)


