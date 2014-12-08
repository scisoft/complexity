class A(object):
    def __init__(self):
        self.a = 1

    def addone(self, x):
        self.a += 1
        return x + self.a

    def inc(self, x):
        return x + self.a

class B(A):
    def __init__(self):
        super(B,self).__init__()

    def np1np2(self, x):
        a = self.addone(x)
        b = self.inc(x)
        return a * b

b = B()
print b.np1np2(5)
