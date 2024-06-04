
def calcular_total(numeros):
    return sum(numeros)

#Funções em python podem retornar mais de um valor
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

#se a funções não tiver um valor retornavel explicito, ela irá retonar "none"
def func_3():
    print("olá mundo")
    


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11) retornou o valor retornado em uma tupla 
print(func_3())