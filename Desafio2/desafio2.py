import textwrap

def menu():
    menu = """ \n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\Listar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==>  """
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, / ):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falha! O valor informado é invalido. @@@")

    return saldo, extrato





def sacar(*, saldo, valor, extrato,limite,numero_saques,limite_saques):




def exibir_extrato(saldo, /, *,extrato):




def criar_usuario(usuario):



def filtrar_usuario(cpf, usuario):





def criar_conta(agencia, numero_conta, usuario):





def listar_contas(contas):




def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0.1
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("quanto deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)


        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")


main()
