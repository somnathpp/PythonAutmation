class Super:
    def __init__(self):
        self._value1 = 100           # protected member single _
        self.__value2 = 200         #private member double __
    def show(self):
        print(self._value1)
        print(self.__value2)
class Sub(Super):
    def show(self):
        print(self._value1)
        print(self.__value2)
s = Super()
s.show()