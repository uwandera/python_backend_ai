texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("\n")  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 123, 9):
    #start, stop=stop-1, step are the arguments
    #list(range(4))
    print(numero, end=" ")
