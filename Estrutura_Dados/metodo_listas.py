lista = []

#o valor append adiciona a lista qualquer objeto
lista.append(1)
lista.append("python")
lista.append([40,30,20])

# método .copy copia e transforma em outro objeto mas com as mesmas caracteristicas
l2 = lista.copy()
print(lista)

# limpa a lista 
lista.clear()
print(lista)

print(l2)
print(id(l2),id(lista))

cores = ["vermelho", "azul","azul", "verde","vermelho","amarelo"]
print(cores.count("vermelho"))#quantas vezes um mesmo elemento aparece na lista

linguagens = ["python","javascript","c"]

linguagens1 = ["java", "c#"]

# .extend() faz um merge das listas final de uma com começo da outra
linguagens.extend(linguagens1)

print(linguagens)

#.index() nos tras o indice da primeira ocorrencia do objeto na lista
print(linguagens.index("java"))

# .pop tira o ultimo elemento adicionado pois o append e extend deixam a lista em forma de pilha(ultimo são os primeiros)
linguagens.pop()
print(linguagens)

# .remove() remove uma ocorrencia do objeto

cores.remove("vermelho")
#para remover mais de uma ocorrencia usar count e recursividade 
print(cores)

# .reverse() faz o espelhamento da lista da mesma forma que lista[::-1]
print(linguagens.reverse())

# .sort() vai ordenar nossa lista

print(linguagens.sort(key=lambda x: len(x))) # ordena em ordem alfabetica


