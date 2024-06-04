lista = ["p", "y", "t", "h", "o", "n"]

# lembrando que é [start:stop:step]
print(lista[2:])  # lembrando que é [start:] começa no terceiro caracter(0,1,2) e vai até o final incluindo ["t", "h", "o", "n"] 
print(lista[:2])  # lembrando que [:stop] vai da posição 0 até a posição stop que nesse caso é o 3 caracter mas não o inclui["p", "y"]
print(lista[1:3])  # lembrando que o ultimo caracter é considerado como stop - 1 pois a marca stop não é considerada ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # se está tudo vazio todo o vetor é mostrado["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  #  inverte a posição como espelho ["n", "o", "h", "t", "y", "p"]

for letra in lista:
    print(letra)

#enumerate para sabe o indice que estamos percorrendo na lista
for i, letra in enumerate(lista):
    print(f"{i}: {letra}")

# filtros em listas
numeros = list(range(100))
pares = []

#for nova_var in var_lista: comando
for numero_par in numeros:
    if numero_par % 2 == 0:
        pares.append(numero_par) 

for i, numero_par in enumerate(pares):
    print(f"{i}: {numero_par}")

numeros = list(range(10))
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

for i, numero in enumerate(quadrado):
    print(f"{i}:{numero}")

#codigo inline
numeros = list(range(100))
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

