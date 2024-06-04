def somar(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a, b): 
    return a / b

def multiplicacao(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)#que porra é essa mano
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

exibir_resultado(10, 10, divisao)