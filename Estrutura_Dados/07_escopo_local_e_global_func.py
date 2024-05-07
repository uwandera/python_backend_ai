salario = 2000


def salario_bonus(bonus, lista):
    global salario # variavel no escopo global, não é uma boa pratica
    lista_aux = lista.copy() 
    lista_aux.append(2)
    print(f"lista_aux={lista_aux}")#muito util pra nao sei oq shausauh
    salario += bonus # é necessario criar a definição de global das variaveis para usar dentro de funções
    return salario

lista =[1]
print(salario_bonus(500, lista))  # 2500
print(lista)