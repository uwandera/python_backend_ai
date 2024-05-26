from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH/'novo diretorio'/'meu_arquivo_que_nao_existe.py', 'r')
except FileNotFoundError as exc: #criando uma chamada costumizada para erro
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo {exc}")

except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo {exc}")




#try:
    #arquivo = open(ROOT_PATH/'novo-diretorio')

















