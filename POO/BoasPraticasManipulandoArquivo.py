from pathlib import Path

ROOT_PATH = Path(__file__).parent

#verificar se o arquivo foi aberto com sucesso

'''try:
    with open(ROOT_PATH /'scrita.txt', 'r') as arquivo: #desta forma conseguimos garantir que o arquivo foi fechado 
        print('trabalhando com o arquivo')
        print(arquivo.read())

except IOError as exc:
    print(f'Erro ao tentar abriro arquivo, {exc}')
'''

try:
    #abrir arquivos e fechar automaticamente com esse pedaço de codigo
    with open(ROOT_PATH/'arquivo-utf-8.txt','r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

except UnicodeDecodeError as exc:
    print(f'Erro de @{exc}@, trocar para UTF-8')