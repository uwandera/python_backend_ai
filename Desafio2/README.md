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
