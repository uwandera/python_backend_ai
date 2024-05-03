nome = "Thomas "
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Thomas", "idade": 28}
print(dados)

# %s para substituir string , %d para substituir por inteiro, %f substitui por ponto flutuante
print("Nome: %s Idade: %d" % (nome, idade))# a ordem das variaveis tem que ser obedecida senão dá erro tipo de 

#formatação de string usando abre e fecha chaves
#se trocar as variaveis de posição a resposta fica incoerente
print("Nome: {} Idade: {}".format(nome, idade))# a ordem das variasveis dentro do .format(var1,var2)

# pode usar numeros(posição) da variavel que queremos colocar na string
#da pra virar uma bagunça se não cuidar
print("Nome: {0} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {1} Nome: {1} {0} {1}".format(idade, nome))


#passar os nomes de variaveis onde irão ser utilizadas
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
#podemos trocar o nome da variavel dentro das chaves mas temos que fazer uma operação de varNEW recebe varOLD
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
#uso de dicionario para efetuação da formatação
print("Nome: {nome} Idade: {idade}".format(**dados))

#melhor forma de formatar com as variaveis
print(f"Nome: {nome} Idade: {idade}")

# width.nf onde width é um numero .n é um numero e o f é float
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:1.2f}") # sem espaços a esquerda e com duas casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:1.1f}") #10 casas de espaço e 1 casa decimal
