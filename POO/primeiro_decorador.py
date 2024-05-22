def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar')
        funcao()
        print('faz algo depois de executar')

    return envelope #ao decorar uma funcao deixar a funcao envelope sem ()

@meu_decorador #açucar sintatico para decoradoresusahuhsau
def ola_mundo():
    print('olá mundo')

#aqui é o decorar da funcao em python, atribuir um novo valor a funcao com outra funcao
#ola_mundo = meu_decorador(ola_mundo)
ola_mundo()