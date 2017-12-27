#Study of how to Handle Exceptions


#Raise Simple Exception
try:
    f = open('Non Existing file','r')
except Exception:
    print('what did you expected MAN u got and exception')


#raise specific Exception
try:
    f = open('Non Existing file','r')
except FileNotFoundError:
    print('now U got coherent  exception')


#cascading of exception
try:
    f = open('Non Existing file','r')
except FileNotFoundError:
    print('now U got coherent  exception')
except Exception:
    print('now U got another  exception')

print("------------")

#raise original exception on demand
try:
    f=open('nonexitent','r')
except Exception as e:
    print('now u will see original exception')
    print(e)

#finally block will be executed no matter what
try:
    f=open('example.txt','r')
except Exception as e:
    print('now u will see original exception')
    print(e)
else:
    f.close()
finally:
    print("no matter what what in finnaly will execute")

