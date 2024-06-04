import functools

def duplicar(funcao):
    @functools.wraps(funcao) #decorador para manter o nome da funcao original pois qunado se usa decoradores a funcao herda o nome da funcao envelope
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        result = funcao(*args, **kwargs) # guardando o resultado da funcao usada consigo retornar seu resultado na funcao decorada!!
        print('faz algo depois de executar')
        return result

    return envelope #fazer retornar aa funcao envelope apenas

@duplicar
def ola_mundo(nome,*args):
    print(f'olá mundo{nome}')
    return nome.upper()

resultado = ola_mundo('joao', 1000, "ancelo")
print(resultado)
print(ola_mundo.__name__)
