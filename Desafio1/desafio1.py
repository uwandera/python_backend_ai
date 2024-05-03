menu = f'''
######  QUAL OPERAÇÂO VOCÊ DESEJA EFETUAR   ######

SAQUE --> [S]
DEPOSITO --> [D]
EXTRATO --> [E]
SAIR --> [Q]
>>> '''

saldo = 1
extrato = ("")
Limite_Saque_Diario = 3
LIMITE_VALOR_POR_SAQUE = 500


while True:
    opcao = input(menu)
    if opcao == "d":
        # OPERAÇÂO DEPÒSITO
        valor = float(input("Qual o valor que deseja depositar: "))
        #verificação para garantir que valores não são negativos
        if valor > 0: 
            #atentar a ordem do +=
            saldo += valor
            print(f"Seu saldo é de R$ {saldo:2.2f}")
            #OPERAÇÂO DE GUARDAR O DEPOSITO NO EXTRATO
            extrato += (f"DEPÒSITO: R$ {valor:.2f} "+"\n")
            
        
        else:
            print("valor inválido, tente novamente!")

    elif opcao == "s":         
            while Limite_Saque_Diario != 0:
                if saldo > 0:
                    print(f"Seu saldo é de R${saldo:2.2f}")
                    saque = float(input("qual valor deseja sacar: "))
                    if saque > 500:
                        print(f"seu saque limite é R$ {LIMITE_VALOR_POR_SAQUE:3.2f}")
                    elif saque > saldo:
                        print("valor desejado insuficiente no momento, tente um outro valor")
                    else:
                        #a ordem do "-="-->(saldo = saldo - saque) ou "=-" -->(saldo = -saque) muda totalmente a conta que está sendo feita, usar saldo -= 
                        saldo -= saque
                        print(f"Seu saldo é de R$ {saldo:2.2f}")
                        extrato += (f"SAQUE: R$ {saque:.2f} "+"\n")
                continuar = input(f"deseja fazer mais um saque, seu limite diario é de {Limite_Saque_Diario - 1} (S ou N):  ")
                if continuar == "s":
                    Limite_Saque_Diario -= 1
                elif continuar == "n":
                    break

    elif opcao == "q":
        break

   
print(extrato)      
quit()
