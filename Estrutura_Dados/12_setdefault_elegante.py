contato = {"nome": "Guilherme", "telefone": "3333-2221"}

#não altera a chave pois já existe
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

#não existia a chave idade então ele incluiu
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

#maneira elegante de adicionar o valor dentro do dicionario caso ele não exista