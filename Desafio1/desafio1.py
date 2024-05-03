menu = f'''
######  QUAL OPERAÇÂO VOCÊ DESEJA EFETUAR   ######

SAQUE --> [S]
DEPOSITO --> [D]
EXTRATO --> [E]
SAIR --> [Q]
>>> 
'''
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_VALOR_POR_SAQUE = 500


while True:
    opcao = input(menu)
    if opcao.upper == "D":
        # OPERAÇÂO DEPÒSITO
        valor = float(input("Qual o valor que deseja depositar: "))
        #verificação para garantir que valores não são negativos
        if valor > 0: 
            saldo =+ valor
        #OPERAÇÂO DE GUARDAR O DEPOSITO NO EXTRATO
        else:
            print("valor inválido, tente novamente!")
            break

quit()
