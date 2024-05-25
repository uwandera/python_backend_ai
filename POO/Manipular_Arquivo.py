# o parametro r no começo da string é pra transformar em um objeto literal para que as backslash não sejam interpretadas como caracteres especiais
leitura = open(r"C:\Users\TESTE ROSE\Desktop\PythonAIBackEnd\src\python_backend_ai\POO\manipular1.txt", 'r')
print(leitura.read())
#print(leitura.readlines())#transforma o arquivo em uma lista
#for linha in leitura.readlines():
    #print(linha)

#while len(linha := leitura.readlines()): # cada linha do arquivo vira um objeto de lista
    #print(linha)

leitura.close()

#escrita = open("asrquivo.txt", 'w')

#anexar = open("asrquivo.txt", 'a')