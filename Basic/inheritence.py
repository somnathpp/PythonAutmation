#Sinle Inherityence
class A:
    def msg(self):
        print("Hello Well come to A")
class B(A):
    def msg1(self):
        print("Hello Well come to B")
b=B()
b.msg()
b.msg1()
# Multi level Inheritence
class Grandfather:
    def msg(self):
        print("Hello Well come to Grandfather")
class Father(Grandfather):
    def msg1(self):
        print("Hello Well come to Father")
class Son(Father):
    def msg2(self):
        print("Hello Well come to Son")
s=Son()
s.msg()
s.msg1()
s.msg2()
#Multiple Inheritence
class Father:
    def msg(self):
        print("Hello Well come to Father")
class Son1(Father):
    def msg1(self):
        print("Hello Well come to Son1")
class Son2(Father):
    def msg2(self):
        print("Hello Well come to Son2")
s1=Son1()
s1.msg()
s1.msg1()
s2=Son2()
s2.msg()
s2.msg2()
#Hierarchical
class Father:
    def msgF(self):
        print("Hello Well come to Father")
class Mother:
    def msgM(self):
        print("Hello Well come to Mother")
class Child(Father, Mother):
    def msgC(self):
        print("Hello Well come to Child")
c=Child()
c.msgC()
c.msgM()
c.msgF()
