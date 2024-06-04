class UsuarioTelefone:
  
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."

# Entrada:
nome = input()  
numero = input()  
plano = input()  

UsuarioTelefone(nome, numero, plano)
