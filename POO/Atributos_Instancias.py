'''
atributos do objeto
    todos os objetos nascem com o mesmo numero de atributos de classe 
    e de intancia

    atributos de instancia são diferentes para cada objeto(cada objeto tem uma copia)

    atributos de classe são compartilhados entr objetos
'''

class Estudante:
    #variaveis de classe e atributos de classe compartilhados
    escola = "DIO"

    def __init__(self, nome, nro_matricula):
        self.nome = nome #variavel de instancia
        self.nro_matricula = nro_matricula

    def __str__(self):
        return f"{self.nome} ({self.nro_matricula}) - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(f"Assim implementamos: {obj}")



#variavel de instancia e seu atribustos singulares
Aluno_1 = Estudante("Thomas", 13102607)
Aluno_2 = Estudante("gabriel", 12343123)
print(Aluno_1)
print(Aluno_2)

#ao manipular uma variavel de classe, ela muda o atributo de todas as intancias
Estudante.escola = "PYTHON"

Aluno_1.nro_matricula = 1
Aluno_2.nro_matricula = 2
print(Aluno_1)
print(Aluno_2)

mostrar_valores(Aluno_1, Aluno_2)