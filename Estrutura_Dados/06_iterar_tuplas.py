carros = (
    "gol",
    "celta",
    "palio",
)
#iterar é percorrer a tupla
for carro in carros:
    print(carro)

#prestar atenção na lógica da iteração
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
