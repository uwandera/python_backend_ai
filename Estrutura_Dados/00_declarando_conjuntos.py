numeros = set([1, 2, 3, 1, 3, 4]) 
# elementos unicos sem ser duplicados os itens duplicados serão eliminados
print(numeros)  # {1, 2, 3, 4}

# a ordem do set vem da onde??
# set na garante ordem
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio",))#não era uma tupla, agora é
print(carros)  # {"gol", "celta", "palio"}

# a outra maneira de fazer um set é usando chaves?? oloko
linguagens = {"python","java","python"}
#isso é um set que pode ser feito var = {} para receber valores e eliminar as duplicações
#conjuntos em python não suportam indexação
print(linguagens)

numeros = {1,2,3,2,7,4,3,3,7,8,9,10,11,12,32,12,32,55}
# para usar indexação em um set devemos transformar em lista primeiro 
subscriptable_numeros = list(numeros)

#consigo indexar
print(subscriptable_numeros[0])

#consigo percorrer 
print(subscriptable_numeros[:])

#podemos percorrer um set usando for sem modificalo
for numero in numeros:
    print(numero)

# método {}.union é exatamente a união de dois conjuntos matematicos sem repetição

conjunto_a = {1,2,3,4,5,6,7,5,6,7,6,8,9,10,14}
conjunto_b = {10,11,12,1,3,6,6,7,8,12,13,14,15}
conjunto_c = {101,111,122,123,3123,621,642,71,82,132,123,144,125}

# método union faz a união dos conjuntos sem repitir nenhum valor
print(conjunto_a.union(conjunto_b))
# mesmo se modificar a ordem o valor nao muda
print(conjunto_b.union(conjunto_a))

#o método .intersection() nos dá a interssecão dos dois conjuntos
print(conjunto_a.intersection(conjunto_b))

#o metodo .difference() nos da a diferença entre eles, a ordem importa!
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#o método .symmetric_difference nos dá todos os elementos que são unicos entre os dois conjuntos, logo é a (união - interseção)
print(conjunto_a.symmetric_difference(conjunto_b))

# o método issubset() é para ver quem é subconjunto de quem!
print(conjunto_a.issubset(conjunto_b))
#a resposta é um booleano
print(conjunto_b.issubset(conjunto_a))

## o método issuperset() é para ver quem é superset de quem!
#a resposta é um booleano
print(conjunto_b.issuperset(conjunto_a))
print(conjunto_a.issuperset(conjunto_b))

## o método isdisjoint() é para ver se os conjuntos são disjutos!
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_a))
print(conjunto_c.isdisjoint(conjunto_b))
print(conjunto_c.isdisjoint(conjunto_a))


sorteio = {1,23,45,67,34}
# o método .add() adiciona o valor dentro do conjunto 
sorteio.add(25)
print(sorteio)
#ele não mantem a ordem nessa incerção
sorteio.add(22)
print(sorteio)
#se o valor já é existente ele não o inclui...mesmo que incluice o set() iria retiralo não é mesmo
sorteio.add(23)
print(sorteio)

#por mais que eu tenha referenciado o sorteio em outra variavel, ao usar o método clear ele elimina a possibilidade de ter algo dentro de sortei, se der um print(sorteio_clear) >>>none e print(sorteio) >>> set{}
sortei_clear = sorteio
print(sortei_clear)
#método clear elimina todos os valores dentro do set
#print(sortei_clear.clear())

sorteio_copy = sorteio.copy()
print(sorteio_copy)
print(id(sorteio_copy),id(sorteio))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)# discarta o valor dentro do set{}
numeros.discard(45)# mesmo não existindo o valor dentro do sete ele realiza o comando e não aponta erros, mas não acontece nada

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# o método .pop() ele elimina os valores do set da esquerda pra direita
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# o remove da key error se o elemnto não existe
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

#metodo len tira o tamanho do set
print(len(numeros))  # 10

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# podemos verificar com o interador in
print(1 in numeros)  # True
print(10 in numeros)  # False

