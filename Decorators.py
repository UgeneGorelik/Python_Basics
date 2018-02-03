
#Decorators



def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

def decorator_f(o_function):
    def wrapper_f(*args,**kwargs):
        print("here is decorated function")
        o_function(*args,**kwargs)
        return o_function(*args,**kwargs)
    return  wrapper_f

@decorator_f
def display():
    print("display")

@decorator_f
def display2(msg):
    print(msg)

# my_func = outer_function("asd")
# my_func1 = outer_function("aaa")
# my_func()
# my_func1()

#
#
# # display()
# display2("message")

class decorator_class(object):
    def __init__(self,o_function):
        self.ofinction=o_function

    def __call__(self, *args, **kwargs):
        print("wrapper class executed")
        return self.ofinction( *args, **kwargs)


@decorator_class
def display3(msg):
    print(msg)


display3("display3")