nome = "Tetrahidrocanabidiol"

print(nome.upper())#transforma tudo em maisuscula 
print(nome.lower())#transforma tudo em minuscula
print(nome.title())#transforma em um titulo

texto = "    Olá mundo!    "

print(texto + ".")
print(texto.strip(), end=".\n")#retira todos os espaços
print(texto.rstrip(), end=".\n")#retira todos os espaços a direita
print(texto.lstrip(), end=".\n")#retira todos os espaços a esquerda

menu = "Python"

print("####" + menu + "####")#centralização manual
print(menu.center(14))# centralizado porem com espaço em branco
print(menu.center(14, "&")) #centralizado mas com "#"
print("-".join(menu))#passar iten a iten e juntar o iten com o caracter escolhido

for i in menu:
    print(i , end="-")

