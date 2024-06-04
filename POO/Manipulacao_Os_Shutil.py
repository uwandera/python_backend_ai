import os
import shutil
from pathlib import Path



ROOT_PATH = Path(__file__).parent #deixar o caminho root abaixo do diretorio que esta sendo usado
#print(ROOT_PATH)

os.mkdir(ROOT_PATH/'novodiretorio2')# criar diretorios
#arquivo = open(ROOT_PATH/'novodiretorio'/'novo_arquivo.txt', 'w') #cria um arquivo usando write
#arquivo.close()

#os.rename(ROOT_PATH/'novodiretorio'/'novo_arquivo.txt', ROOT_PATH/'novodiretorio'/'alterado.txt') #renomeia o arquivo

#os.remove(ROOT_PATH/'novodiretorio'/'alterado.txt') # remove o arquivo


shutil.move(ROOT_PATH/'novodiretorio'/'novo_arquivo.txt', ROOT_PATH/'novodiretorio2'/'novo_arquivo.txt') #move o arquivo de diretorios

