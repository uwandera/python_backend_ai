#lembrando que o detalhe que separa a tupla da lista é essa ultima virgula
tupla = ("p", "y", "t", "h", "o", "n",)
 
 #fatiamento sendo a forma de separar objetos de uma tupla 
print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")
