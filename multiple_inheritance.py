class A:
    _a=30
    def display1(self):
        print(self._a)
    def getVal(self)->int:
        return self._a
class B:
    _b=40
    def display2(self):
        print(self._b)
    def getVal(self)->int:
        return self._b
class C(A,B):
    _c=60
    def display3(self):
        print(self._c)
if __name__=='__main__':
    print("multiple inheritance")
    c=C()
    c.display1()
    c.display3()
    c.display2()