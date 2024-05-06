#aninhamento de dicionario funciona bem como um banco de dados
#super-dicionario {chave:{chave:valor}}
contatos = {#super dicionario {chave:{chave:valor}}
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},#subdicionario0
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},#subdicionario1
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},#subdicionario2
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766","extra":{"a": 1}},#subdicionario3
}

#chamando um valor de dentro do dicionario é preciso chamar as chaves de forma super-sub
#neste caso guardamos o valor em uma variavel 
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

extra = contatos["melaine@gmail.com"]["extra"]["a"]

print(extra)