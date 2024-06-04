def calculador(operacao):
    #innerfunction
    def soma(a, b):
        return a+b
    
    def subtracao(a, b):
        return a-b
    
    def multiplicacao(a, b):
        return a*b
    
    def divisao(a, b):
        return a/b
    
    #retornando as function que foram definidas dentro dos escopos singulares de cada operacao
    match operacao:
        case '+':
            return soma
        
        case '-':
            return subtracao
        
        case '*':
            return multiplicacao
        
        case '/':
            return divisao
        

print(calculador('+')(1,3))

somaD = calculador('+')(12333423312345456, 97898201381727391)

print(somaD)