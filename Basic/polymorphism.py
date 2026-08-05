
#function overloading
class A:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        elif a!=None:
            return a
        else:
            return None

a=A()
y=a.add()
print(y)
#function overriding
class Father:
    def car(self):
        print("Father have alto")
    def dog(self):
        print("Dog name johnny")
class Child1(Father):
    def car(self):
        print("Child have mercedese")
    def dog(self):
        print("Child Dog name johnny and Jully")
class Child2(Father):
    def car(self):
        print("Child1 have bmw")
cx=Child1()
cx.car()