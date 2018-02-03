import copy
from random import shuffle

#deepe copy copies it in a way that when changing
#in the copy the original is not changed
l=[1,2,3]
l1=copy.deepcopy(l)
l[0]=123
# for x in l:
#     print(x)
# for x in l1:
#     print(x)

#when using shallow copies changes made in a copy reflected in original
l2=copy.copy(l)




l2[0]=4444
for x in l:
    print(x)


#how to shuffle/randomize
shuffle(l)

#Monkey patching is adding in rutime a attribute to a class
class MyClass:
    def f(self):
        print("f()")
def monkey_f(self):
    print("monkey_f")
x=MyClass()
x.f()
MyClass.f=monkey_f
obj=MyClass()
obj.f()

