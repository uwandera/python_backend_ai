class Foo:
    def __init__(self, x=None):
        self._x =x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x  = -1

    


    


foo1 = Foo(10)
print(foo1.x)
print(foo1.x)
del foo1.x
print(foo1.x)