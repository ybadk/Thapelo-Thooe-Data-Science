
class Test:
    def __init__(self):
        #1st instance variable inside init function
        self.a = 5
    def f1(self):
        #2nd instance variable inside function f1
        self.b = 10


t1 = Test()

t2 = Test()

t1.f1()

#3rd instance variable
t1.c= 15
print(t1.__dict__)
print(t2.__dict__)
