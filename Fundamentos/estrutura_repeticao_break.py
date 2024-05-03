while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


for numero in range(100):
    #ao adicionar o not altomaticamente transformamos no array de multiplos do numero em questão
    if not (numero % 3 == 0):
        continue #comando que paça a execução para o proximo bloco de instrução, nesse caso ele não irá printar os numerto pares --> 2mod0 group
    else: #adicionei o else para melhor entendimento do codigo pois ele pode ser omitido
        print(numero, end=" ")
