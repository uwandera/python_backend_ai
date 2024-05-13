class Animal():
    def __Init__(self, nro_patas, nro_asas):
        self.nro_patas = nro_patas
        self.nro_asas = nro_asas

class Mamifero(Animal):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)
        

class Ave(Animal):
    def __init__(self, nro_patas, nro_asas, cor_bico):
        super().__init__(nro_patas, nro_asas)
        self.cor_bico = cor_bico
        self.nro_patas = nro_patas




class Gato(Mamifero):
    pass

    

class Ornitorrinco(Mamifero, Ave):
    pass


gato1 = Gato(nro_patas=4)
print(gato1)


