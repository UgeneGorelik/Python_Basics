#Basic functions Examples

#create empty function
def emptyfunc():
    pass

#basic function
def func():
    print('jeremiah  was a bullfrog')

#function with params second param is not mandatory
def func1(st,additon='oh yeah'):
    print('jeremiah  was a bullfrog '+st+' ' +additon)

#pass to function unknown number of variables *args is like list *kwargs in named like dictionary
def func2(*args,**kwargs):
    print(args)
    print(kwargs)

def func2(*args,**kwargs):
    print(args)
    print(kwargs)


func()

print(func)

func1("he was a friend of mine")

func2('long','live',name='Elthon',lname='john')

saying=['long','live']
whois={'name':'Elthon'}

func2(saying,whois)