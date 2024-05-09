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
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ operação falha! você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ operação falhou! o valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ operação falha! núrmero máximo de saques excedeu. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")

    else:
        print("\n@@@ operação fálha! O valor informado é inválido. @@@")

    return saldo, extrato




def exibir_extrato(saldo, /, *,extrato):
    print("\n================= EXTRATO =================")
    print("não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===============================================")



def criar_usuario(usuario):
    cpf = input("informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ usuário com este cpf já está cadastrado! @@@")
        return
    
    nome = input("informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("===== Usuário criado com sucesso! =====")


def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None





def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n===== Conta criada com sucesso! =====")
        return {"agência": agencia, "numero_conta": numero_conta, "usuário": usuario}
    
    print("\n@@@ usuário não encontrado, fluxo de criação de conta encerrado! @@@")



'''

def listar_contas(contas):



'''

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
            conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

            if conta:
                contas.append(conta)

        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")


main()
