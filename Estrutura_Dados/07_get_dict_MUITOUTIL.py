contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
#ao fazer a requisição de um valor de chave que não existe o programa para e da "key errror"

# contatos["chave"]  # KeyError

#para não dar erro temos que dar um valor de vazio para as chaves não existentes
resultado = contatos.get("chave")  # None
print(resultado)

#aqui usamos a sintaxe do fromkeys para gerar um valor vazio
resultado = contatos.get("chave", "chave inexistente")  # {} or qualquer valor que queira exibir para denotar chave inexistente
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {} # não entendi o pq das chaves depois 
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} NAO È ASIM QUE ESTA APARECENDO!
print(resultado)
