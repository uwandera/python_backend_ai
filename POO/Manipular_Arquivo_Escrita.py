
#o caminho pode ser dado a um arquivo inexistente para sua criação
escrita = open(r"C:\Users\TESTE ROSE\Desktop\PythonAIBackEnd\src\python_backend_ai\POO\escrita.txt", 'w')

#escrita.write("@@@@ Criando um arquivo txt e escrevendo dados nele com o comandos python@@@@@@@")
escrita.writelines(['192','.','168','.','77','.','245']) #metofdo em objetos iteraveis
escrita.close()