#valores do  objeto chave <variavel> são imutaveis
#{chave:valor,chave:valor,...} podem ser gigantescos
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

#na classe dict(chave=valor)
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

#adicionando um novo valor no dicionario
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
