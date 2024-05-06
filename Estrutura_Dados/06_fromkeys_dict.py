resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado) #adicionar chaves de dicionario sem valores

resultado = dict.fromkeys(["nome", "telefone"], "vazio") #adicionar chaves no dicionario com valor padrão {"nome": "vazio", "telefone": "vazio"}
print(resultado)
