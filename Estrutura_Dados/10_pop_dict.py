contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#pop remove e retorna o valor que removeu
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)
print("valor dentro do dict após o método pop: ",contatos)

resultado = contatos.pop("guilherme@gmail.com", "{dicionario vazio}")  # {}
print(resultado)
print(contatos)
