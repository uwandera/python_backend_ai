import csv

from pathlib import Path

ROOT_PATH = Path(__file__).parent

'''

try:

    with open(ROOT_PATH/'usuario1.csv','w',newline="", encoding='utf-8') as arquivo: #o argumento newline deixa o arquivo csv sem os espaçoes extras
        escritor = csv.writer(arquivo)
        escritor.writerow(['nome','id'])
        escritor.writerow(['Alice','1'])
        escritor.writerow(['Bob','2'])

except IOError as exc:
    print(f'Erro @{exc}@ ')

'''

'''
try:

    with open(ROOT_PATH/'usuario1.csv','r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

except IOError as exc:
    print(f'Erro @{exc}@ ')
'''


try:
    with open(ROOT_PATH/'usuario1.csv','r', newline="", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo) #dictireader ja entende que a linha 0 é ond declaramos o header
        print(leitor.fieldnames)# printa o nome das colunas
        for linha in leitor:
            print(linha['nome'], linha['id'])
except IOError as exc:
    print(f'Erro @{exc}@ ')





'''

with open('example.csv','r') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        print(linha)


with open('example.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['nome',"idade"])
    writer.writerow(['Alice',"30"])
    writer.writerow(['Bob',"22"])
    '''