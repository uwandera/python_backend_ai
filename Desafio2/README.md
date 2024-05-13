# Desafio 2
## Desenvolver as funções dos sistema
    Linguagem: Python 3
    versão: 2
    objetivo: separar as funções existentes em modulos de função python e criar duas novas funções:
    --> cadastro usuário(cliente)
    --> cadastro conta bancária
    
## Modularização de operações existentes (transformar em Funções)
 ⁂modularizar a operação saque
 ⁂modularizar a operação deposito
 ⁂modularizar a operação extrato
 ⁂cadastro de agencia bancaria
 ⁂cadastro de conta bancaria
 ⁂todos os depositos devem ser armazenados em uma variavel
 ⁂todos os depositos devem ser exibidos em EXTRATO

## Adicionar 2 novas operações já modularizadas
    ⁂cadastro cliente (do banco em especifico)
        X usuario em uma lista(dicionario ou tupla);
        X usuario = [nome,data de nascimento,cpf,endereço];
        X endereço é string: logradouro, numero - bairro - cidade/sigla do estado;
        X cpf apenas numeros;
        X cpf é um valor unico;

    ⁂criar conta corrente (vincular com usuario)
        X armazenar contas em uma lista(dicionario ou tupla);
        X conta é composta por: agencia, numero da conta, usuario;
        X o numero da conta é sequencial iniciando em 1
        X o numero da agencia é fixo: "0001";
        Xo usuario pode ter mais de uma conta mas uma conta só pode pertencer a uma agencia;

    ⁂ função listar contas 
    ⁂função listar usuario
    ⁂funçaõ deletar usuario

## retorno e forma de chamar a função e passagem de argumento
    ⁂por posição e nomeados
    ⁂retorno ao meu criterio

    ⁂função saque deve receber argumentos por nome (keyword only) --> arg(saldo=varsque, valor=varvalor, extrato,limite,numero_saques, limite_saques)
    ⁂retorno da função saque deve ser saldo, extrato

    ⁂função deposito deve receber os argumentos apenas por posição(positional only), args(saldo,valor,extrato)

    ⁂função extrato deve receber os args por posiçaõ e nome, argPosition(saldo)argName(extrato=)
menu = f'''######  QUAL OPERAÇÂO VOCÊ DESEJA EFETUAR   ######
SAQUE --> [S]
DEPOSITO --> [D]
EXTRATO --> [E]
SAIR --> [Q]
>>>  '''

saldo_total = 1
extrato = ("")
Limite_Saque_Diario = 3
LIMITE_VALOR_POR_SAQUE = 500

opcao = input(menu)
if opcao == "d":
    def DEPOSITO(valor_deposito, saldo_total, extrato):
    
    # OPERAÇÂO DEPÒSITO
        valor_deposito = float(input("Qual o valor que deseja depositar: "))
                #verificação para garantir que valores não são negativos
        if valor_deposito > 0: 
                    #atentar a ordem do +=
            saldo_total
            saldo_total += valor_deposito
            print(f"Seu saldo é de R$ {saldo_total:2.2f}")
                    #OPERAÇÂO DE GUARDAR O DEPOSITO NO EXTRATO
            extrato 
            extrato += (f"DEPÒSITO: R$ {valor_deposito:.2f} "+"\n")
            return valor_deposito, saldo_total, extrato
                    
        else:
            print("valor inválido, tente novamente!")
            return
            
    DEPOSITO(valor_deposito="", saldo_total="",extrato="")
            
        
'''

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
                else:
                    print("este valor não é válido, tente novamente")
                    break

    elif opcao == "q":
        break

    elif opcao == "e":
        print(extrato)
    
    else:
        break

   
      
quit()
'''