from abc import ABC, abstractmethod

class TecnologiaFuturista(ABC):
    @abstractmethod
    def usar(self):
        pass

class Phaser(TecnologiaFuturista):
    def usar(self):
        return "Atirando com o phaser!"

class DispositivoMédico(TecnologiaFuturista):
    def usar(self):
        return "Utilizando o dispositivo médico para tratar ferimentos."

# Exemplo de uso:
phaser = Phaser()
dispositivo_medico = DispositivoMédico()

# Abstração: chamando o método 'usar()' sem saber a implementação específica de cada classe
print(phaser.usar())
print(dispositivo_medico.usar())

'''
In this example:

The TecnologiaFuturista class is an abstract 
base class (ABC) representing futuristic technology from Star Trek: Discovery. It defines an abstract method usar() (use) using the abstractmethod decorator from the abc module. This method must be implemented by any concrete subclass.
The Phaser class is a concrete subclass of 
TecnologiaFuturista representing a phaser weapon. 
It provides its own implementation of the usar() method.
The DispositivoMédico class is another concrete 
subclass of TecnologiaFuturista representing a 
medical device. It also provides its own implementation
 of the usar() method.
In the example usage, we create instances of Phaser 
and DispositivoMédico and call the usar() method on each. 
Despite calling the same method, each subclass provides 
its own specific implementation, demonstrating 
abstraction. The caller doesn't need to know the 
specific implementation details, only that it can 
use the usar() method.

'''